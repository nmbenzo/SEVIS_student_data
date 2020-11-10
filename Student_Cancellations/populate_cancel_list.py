import os
import time
import math
import pandas as pd
from Handlers.file_imports import No_show_UG, No_show_GR, \
No_SHOW_students_FINAL,  NO_SHOW_students, \
NOSHOW_students_sheet, SEVIS_initial_status_stud
from tqdm import trange


def rename_worksheets():
    """This function renames the worksheets from No-Show_UG/GR to 'Sheet1'
    The system will throw an error when processing data otherwise
    """
    df = pd.read_excel(No_show_UG)
    with pd.ExcelWriter(No_show_UG, mode='w') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()

    df = pd.read_excel(No_show_GR)
    with pd.ExcelWriter(No_show_GR, mode='w') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()


def merge_no_show_ISSM_data():
    """
    Concatenates data from the No_Show_UG file with the
    No_show_GR file and then saves the concatenated data
    to the No_show_GR file
    """
    merged_data = []
    for f in [No_show_UG, No_show_GR]:
        data = pd.read_excel(f, 'Sheet1').iloc[:-2]
        data.index = [os.path.basename(f)] * len(data)
        merged_data.append(data)
    merged_data = pd.concat(merged_data)
    with pd.ExcelWriter(No_show_GR, mode='w') as writer:
        merged_data.to_excel(writer,'Sheet1', index=False, engine='openpyxl')
        writer.save()


def merge_no_show_data():
    """
    Merges data via pandas merge function and then moves column order to
    provide efficient readability. The function also removes duplicate rows by
    filtering on SEVIS IDs.
    """
    ns_gr = pd.read_excel(No_show_GR)
    ns_sevis = pd.read_excel(SEVIS_initial_status_stud)

    results = pd.merge(ns_sevis, ns_gr[
                ['Campus Id',
                 'SEVIS ID',
                 'Level of Education (display)',
                 'Major Field (display)',
                 '14 CHECK IN I94 or Entry Stamp',
                 '20 ISO Attendance Date',
                 '05 Banner Student Status',
                 '03 Student Status Term',
                 '07 Total Credit Hours',
                 '28 Latest Decision']
                ], on='SEVIS ID', how='left')
               #indicator=True)
    cleaned_results = \
        results.drop_duplicates(subset=['SEVIS ID'], keep='first')
    cleaned_results = cleaned_results[[
               'Campus Id',
               'SEVIS ID',
               'Surname/Primary Name',
               'Given Name',
               '28 Latest Decision',
               'Class of Admission',
               'Level of Education (display)',
               'Major Field (display)',
               '14 CHECK IN I94 or Entry Stamp',
               '20 ISO Attendance Date',
               '05 Banner Student Status',
               '03 Student Status Term',
               '07 Total Credit Hours',
               'Eligible for Registration']]

    # can be a list, a Series, an array or a scalar
    cleaned_results.insert(loc=0, column='Cancellation Notes', value='')
    #*** - df.dropna() won't execute outside a df unless inplace=True
    cleaned_results.dropna(subset=['Campus Id',
                          'Level of Education (display)'], inplace=True)
    with pd.ExcelWriter(No_SHOW_students_FINAL, mode='w') as writer:
        cleaned_results.to_excel(writer,'Sheet1', index=False,
                                 engine='openpyxl')
        writer.save()
    writer.close()


def sort_no_show_data():
    """
    This function uses Panda's sort function to sort data based on
    'Campus Id' values
    It then prints out a statement of what occurred in to the user
    """
    active_data = pd.read_excel(No_SHOW_students_FINAL, sheet_name=0)
    sorted_by_CWID = active_data.sort_values(['14 CHECK IN I94 or Entry Stamp',
                          '20 ISO Attendance Date', '05 Banner Student Status',
                          '03 Student Status Term'], ascending=True)

    writer = pd.ExcelWriter(No_SHOW_students_FINAL, engine='openpyxl')
    writer.book = NO_SHOW_students
    writer.sheets = dict((ws.title, ws) for ws in NO_SHOW_students.worksheets)

    sorted_by_CWID.to_excel(writer, 'Sheet', index=False)
    writer.save()


def build_cancel_notes(Cancel_SEVISID_banner, Cancel_SEVISID_credits,
                       Cancel_SEVISID_SV):
    """
    Builds a brief set of note for each record displaying based on
    several dictionaries that contain SEVIS IDs as their keys
    """
    no_show_sevis = pd.read_excel(No_SHOW_students_FINAL)
    sevis_id_loc = no_show_sevis.columns.get_loc('SEVIS ID') + 1
    for rowNum in trange(2, NOSHOW_students_sheet.max_row):
        sevisid = NOSHOW_students_sheet.cell(row=rowNum,
                                             column=sevis_id_loc).value
        for x in Cancel_SEVISID_banner, Cancel_SEVISID_credits, \
                 Cancel_SEVISID_SV:
            for i in Cancel_SEVISID_credits:
                for j in Cancel_SEVISID_SV:
                    if x and i and j == sevisid:
                        if Cancel_SEVISID_SV[sevisid] != 'Yes':
                            if math.isnan(Cancel_SEVISID_credits[sevisid]):
                                NOSHOW_students_sheet.cell\
                            (row=rowNum,column=1).value = \
                                    'SV Status: Not checked in' + \
                                    ', Registered Units: ' \
                                    + ', Registered Units: 0 credits.' \
                                    + ' credits, ' + 'Banner Status: ' + \
                                    str(Cancel_SEVISID_banner[sevisid])
                            else:
                                NOSHOW_students_sheet.cell \
                                    (row=rowNum, column=1).value = \
                        'SV Status: Not checked in' + ', Registered Units: '\
                            + str(Cancel_SEVISID_credits[sevisid]) \
                            + ' credits, ' + 'Banner Status: ' + \
                            str(Cancel_SEVISID_banner[sevisid])
                        else:
                            NOSHOW_students_sheet.cell(row=rowNum, column=1).\
                            value = 'SV Status: ' + \
                            str(Cancel_SEVISID_SV[sevisid]) \
                            + ', Registered Units: ' \
                            + str(Cancel_SEVISID_credits[sevisid]) + \
                            ' credits, ' + 'Banner Status: ' + \
                            str(Cancel_SEVISID_banner[sevisid])

    NO_SHOW_students.save(No_SHOW_students_FINAL)


def print_no_show_work_done():
    work_output = ["-New Excel workbook built",
                   "-Read ISSM Report",
                   "-Read SEVIS Report",
                   "-Data between reports matched on SEVIS ID",
                   "-Build custom notes for Admissions to work from",
                   "-New Data saved to No_SHOW_Final workbook",
                   "-Sorted by CWID"]
    for work in work_output:
        time.sleep(0.3)
        print(work)


# if __name__ == '__main__':
#      start_time = time.time()
#      rename_worksheets()
#      merge_no_show_ISSM_data()
#      merge_no_show_data()
#      sort_no_show_data()
#      build_cancel_notes(Cancel_SEVISID_banner, Cancel_SEVISID_credits,
#                         Cancel_SEVISID_SV)
#      print_no_show_work_done()
#      print("--- %s seconds ---" % (time.time() - start_time))

