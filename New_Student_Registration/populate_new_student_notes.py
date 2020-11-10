import time
import os
import pandas as pd
import numpy as np
from Handlers.directories import path_to_final_data_S20
from Handlers.major_advisor_data import ug_final_df, gr_final_df
from Handlers.file_imports import NEW_students_FINAL, \
 NEW_students,  new_stud_issm_data, sevis_inital_student_data, \
issm_reg_data_success, NEW_final_MASTER, issm_add_address_phone


outname = 'data_diff.csv'

outdir = path_to_final_data_S20
if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname = os.path.join(outdir, outname)


def dataframe_difference(which=None):
    """Find rows which are different between two DataFrames."""
    df1 = pd.read_csv(new_stud_issm_data)
    df2 = pd.read_csv(sevis_inital_student_data)

    # filter the data by a date range. Need to set csv file ['Program Start Date'}
    # to Short Date
    filtered = df2[(df2['Program Start Date'] > '1/1/2020')
                   & (df2['Program Start Date'] < '2/1/2020')]
    # compare the data via an outer join to capture all rows from both data sets
    comparison_df = df1.merge(filtered, indicator=True, how='outer')

    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    diff_df.to_csv(fullname)
    return diff_df


def merge_new_data():
    """
    Merges data via pandas merge function and then exports the updated
    Dataframe to an Excel spreadsheet. The function also removes
    duplicates.
    """
    issm_sev_pending = pd.read_csv(new_stud_issm_data)
    sev_pending = pd.read_csv(sevis_inital_student_data)

    # filter the data by a date range
    filtered = sev_pending[(sev_pending['Program Start Date'] > '1/1/2020')
                           & (sev_pending['Program Start Date'] < '2/1/2020')]

    results = pd.merge(filtered, issm_sev_pending[
        ['Campus Id', 'SEVIS ID','Profile Status','Level of Education (display)',
         'Major Field (display)', '03 Student Status Term',
         '07 Total Credit Hours', '04 Transfer From', '06 Transfer In Date',
         '20 ISO Attendance Date', '14 CHECK IN I94 or Entry Stamp',
         '05 Banner Student Status', 'E-mail Address',
         'Phone 1', '26 University advisor','DataLink Active']],
         on='SEVIS ID', how='left')
    # indicator=True)
    cleaned_results = \
        results.drop_duplicates(subset=['SEVIS ID'], keep='last').copy()
    cleaned_results = cleaned_results[[
        'E-mail Address', 'Campus Id', 'SEVIS ID', 'Surname/Primary Name',
        'Given Name', 'Class of Admission', 'Profile Status',
        'Level of Education (display)', 'Program Start Date',
        'Major Field (display)', '04 Transfer From', '06 Transfer In Date',
        '03 Student Status Term', '07 Total Credit Hours',
        '20 ISO Attendance Date', '14 CHECK IN I94 or Entry Stamp',
        '05 Banner Student Status', 'Eligible for Registration',
        'DataLink Active', 'E-mail Address', 'Phone 1', '26 University advisor']]
    # can be a list, a Series, an array or a scalar
    # cleaned_results.insert(loc=0, column='Registration Status', value='')
    cleaned_results.insert(loc=0, column='Registration Notes', value='')

    return cleaned_results


def match_new_advisor(cleaned_results, ug_final_df, gr_final_df):
    """
    match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module:
    major_advisor_data
    """
    cleaned_results = cleaned_results

    ug_final_df.columns = ['Major Field (display)', 'Advisor', 'Level of Education (display)']
    gr_final_df.columns = ['Major Field (display)', 'Advisor', 'Level of Education (display)']

    ug_results = pd.merge(cleaned_results, ug_final_df[
        ['Advisor',
         'Level of Education (display)',
         'Major Field (display)']],
          on=['Level of Education (display)', 'Major Field (display)'],
          how='left')

    gr_results = pd.merge(ug_results, gr_final_df[
        ['Advisor',
         'Level of Education (display)',
         'Major Field (display)']],
          on=['Level of Education (display)', 'Major Field (display)'],
          how='left')

    # combine the two advisor DataFrame columns
    gr_results['Advisor'] = \
        gr_results.pop("Advisor_x").fillna(gr_results.pop("Advisor_y")).astype(str)

    writer = pd.ExcelWriter(NEW_students_FINAL)
    gr_results.to_excel(writer, 'Sheet1', index=False)
    writer.save()


def add_advisor_notes():
    """
    add_advisor_notes fills any null values in Total Credit Hours(TCH),
    CHECK IN I94(CI94) with zeros and Not Complete, respectively, and then
    inserts a Registration Notes column and populates it with a formatted
    string of values from TCH and CI94
    """
    final_workbook = pd.read_excel(NEW_students_FINAL)

    # remove NaN values and replace with readable notes for users
    units = final_workbook['07 Total Credit Hours'].fillna(0)
    check_in = final_workbook['14 CHECK IN I94 or Entry Stamp']. \
        fillna('Not Complete')

    # convert the two Series to numpy char arrays
    a = np.char.array(check_in.values)
    b = np.char.array(units.values)

    # concatenate the two numpy char arrays, b' represents
    # a Boolean check (bytes) for the astype (str) function
    final = final_workbook['Registration Notes'] = \
        (b'SV Status: ' + a + b', Registered Units: ' + b).astype(str)
    # convert the concatenated char array to a DataFrame.
    df_final = pd.DataFrame(final, columns=['Registration Notes'])

    # drop registration column on final workbook
    final_workbook.drop(['Registration Notes'], axis=1, inplace=True)
    # combine the two DataFrames. axis=1 concatenates horizontally
    # rather than vertically
    df_combine = pd.concat([df_final, final_workbook], axis=1)

    with pd.ExcelWriter(NEW_students_FINAL, mode='w') as writer:
        df_combine.to_excel(writer, 'Sheet1', index=False,
                            engine='openpyxl')
        writer.save()


def sort_new_data():
    """
    Function to sort the Dataframe and then spreadsheet by I-94 check-in
    entry and then by campusID
    """
    active_data = pd.read_excel(NEW_students_FINAL, sheet_name=0)
    sorted_by_CWID = active_data.sort_values(['14 CHECK IN I94 or Entry Stamp'], ascending=True)

    writer = pd.ExcelWriter(NEW_students_FINAL, engine='openpyxl')
    writer.book = NEW_students
    writer.sheets = dict((ws.title, ws) for ws in NEW_students.worksheets)
    sorted_by_CWID.to_excel(writer, 'Sheet', index=False)
    writer.save()


def print_new_work_done():
    work_output = ["-Built discrepancy report",
                   "-New Excel workbook built",
                   "-Read ISSM Report",
                   "-Read SEVIS Report",
                   "-Data between reports matched on SEVIS ID",
                   "-Matched Advisors based on Major data",
                   "-New Data saved to NEW_Final workbook",
                   "-Sorted by CWID"]
    for work in work_output:
        time.sleep(0.3)
        print(work)


def update_checkin_status():
    """
    update_checkin_status, will reference a newer workbook with the
    existing final_workbook and update fields defined in the function
    with the most up to date value.
    """
    active_pending_issm = pd.read_excel(issm_add_address_phone)
    final_workbook = pd.read_excel(NEW_final_MASTER)

    # drop columns to merge new data from active_pending_issm worksheet properly
    try:
        final_workbook.drop(['03 Student Status Term',
                             '07 Total Credit Hours',
                             '14 CHECK IN I94 or Entry Stamp'], axis=1,
                            inplace=True)
        # Save workbook to apply changes
        with pd.ExcelWriter(NEW_final_MASTER, mode='w') as writer:
            final_workbook.to_excel(writer, 'Sheet1', index=False,
                                    engine='openpyxl')
            writer.save()
    except:
        print("Columns don't exist. No drop performed.")
    finally:
        results = pd.merge(final_workbook, active_pending_issm[
            ['Campus Id', '03 Student Status Term',
             '07 Total Credit Hours', '14 CHECK IN I94 or Entry Stamp',
             'Address Type', 'Address Line 1', 'Address Line 2',
             'City', 'Phone 1']], how='left', on='Campus Id')
    cleaned_results = \
        results.drop_duplicates(subset=['SEVIS ID'], keep='first')

    # rename_cols = cleaned_results.rename(columns=
    # {'03 Student Status Term_x':'03 Student Status Term',
    #  '07 Total Credit Hours_x':'07 Total Credit Hours',
    #  '14 CHECK IN I94 or Entry Stamp_x':'14 CHECK IN I94 or Entry Stamp'})

    try:
        final_layout = cleaned_results[[
            'Registration Notes', 'Event Name', 'Event Status',
            'Advisor', 'E-mail Address', 'Campus Id', 'SEVIS ID',
            'Surname/Primary Name', 'Given Name', 'Class of Admission',
            'Level of Education (display)', 'Major Field (display)',
            '03 Student Status Term', '07 Total Credit Hours',
            '14 CHECK IN I94 or Entry Stamp', '05 Banner Student Status',
            'Eligible for Registration', 'DataLink Active',
            'Address Type', 'Address Line 1', 'Address Line 2',
            'City', 'Phone 1']]
    except:
        final_layout = cleaned_results[[
            'Registration Notes', 'Advisor', 'E-mail Address', 'Campus Id',
            'SEVIS ID', 'Surname/Primary Name', 'Given Name', 'Class of Admission',
            'Level of Education (display)', 'Major Field (display)',
            '03 Student Status Term', '07 Total Credit Hours',
            '14 CHECK IN I94 or Entry Stamp','05 Banner Student Status',
            'Eligible for Registration', 'DataLink Active',
            'Address Type', 'Address Line 1', 'Address Line 2',
            'City','Phone 1']]
    with pd.ExcelWriter(NEW_final_MASTER, mode='w') as writer:
        final_layout.to_excel(writer, 'Sheet1', index=False,
                              engine='openpyxl')
        writer.save()

def match_registration_event():
    """
    match registration event will add two columns from an ISSM report that
    contains SEVIS Registration event information and join it on the new
    NEW_Students_FINAL workbook
    """
    final_workbook = pd.read_excel(NEW_final_MASTER)
    issm_reg = pd.read_excel(issm_reg_data_success)

    try:
        final_workbook.drop(['Event Name', 'Event Status'], axis=1,
                            inplace=True)
        # Save workbook to apply changes
        with pd.ExcelWriter(NEW_final_MASTER, mode='w') as writer:
            final_workbook.to_excel(writer, 'Sheet1', index=False,
                                    engine='openpyxl')
            writer.save()
    except:
        print("Columns don't exist. No drop performed.")
    finally:
        # perform merge with new data from active_pending_issm
        results = pd.merge(final_workbook, issm_reg[
            ['SEVIS ID', 'Event Name', 'Event Status']],
            on='SEVIS ID', how='left')
        # indicator=True)
        cleaned_results = \
            results.drop_duplicates(subset=['SEVIS ID'], keep='first')

        final_layout = cleaned_results[[
            'Registration Notes', 'Event Name', 'Event Status',
            'E-mail Address', 'Campus Id', 'SEVIS ID',
            'Surname/Primary Name', 'Given Name',
            'Class of Admission', 'Level of Education (display)',
            'Major Field (display)', '03 Student Status Term',
            '07 Total Credit Hours', '14 CHECK IN I94 or Entry Stamp',
            '05 Banner Student Status', 'Eligible for Registration',
            'DataLink Active', 'Advisor']]

    with pd.ExcelWriter(NEW_final_MASTER, mode='w') as writer:
        final_layout.to_excel(writer, 'Sheet1', index=False,
                              engine='openpyxl')
        writer.save()
