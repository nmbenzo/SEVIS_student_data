import time
import pandas as pd
from Handlers.file_imports import ACTIVE_students_FINAL, \
    ACTIVE_students
from Handlers.file_imports import active_stud_issm_data, active_student_req_reg
from Handlers.major_advisor_data import ug_final_df, gr_final_df


def merge_active_data():
    """
    Merges data via pandas merge function and then exports the updated
    Dataframe to an Excel spreadsheet. The function also removes
    duplicates.
    """
    active_issm = pd.read_csv(active_stud_issm_data)
    active_sevis = pd.read_csv(active_student_req_reg)

    results = pd.merge(active_sevis, active_issm[
        ['Campus Id', 'SEVIS ID', 'Level of Education (display)',
         'Major Field (display)', '03 Student Status Term',
         '07 Total Credit Hours','Phone 1', 'E-mail Address']],
         on='SEVIS ID', how='left')
    # indicator=True)
    cleaned_results = \
        results.drop_duplicates(subset=['SEVIS ID'], keep='first').copy()
    cleaned_results = cleaned_results[
        ['Surname/Primary Name', 'Given Name', 'Campus Id',
        'SEVIS ID', 'Class of Admission', 'Level of Education (display)',
        'Major Field (display)', '03 Student Status Term',
        '07 Total Credit Hours', 'Next Session Start Date',
        'Eligible for Registration', 'Phone 1','E-mail Address']]
    # can be a list, a Series, an array or a scalar
    cleaned_results.insert(loc=0, column='Notes', value='')
    cleaned_results.insert(loc=1, column='Registration', value='')

    return cleaned_results


def match_active_advisor(cleaned_results, ug_final_df, gr_final_df):
    """
    match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module:
    major_advisor_data.
    """
    cleaned_results = cleaned_results

    ug_final_df.columns = ['Major Field (display)', 'Advisor', 'Level of Education (display)']
    gr_final_df.columns = ['Major Field (display)', 'Advisor', 'Level of Education (display)']

    ug_results = pd.merge(cleaned_results, ug_final_df[[
        'Advisor',
        'Level of Education (display)',
        'Major Field (display)']],
         on=['Level of Education (display)', 'Major Field (display)'],
         how='left')

    gr_results = pd.merge(ug_results, gr_final_df[[
        'Advisor',
        'Level of Education (display)',
        'Major Field (display)']],
         on=['Level of Education (display)', 'Major Field (display)'],
         how='left')

    # combine the two advisor DataFrame columns
    gr_results['Advisor'] = \
        gr_results.pop("Advisor_x").fillna(gr_results.pop("Advisor_y")).astype(str)

    writer = pd.ExcelWriter(ACTIVE_students_FINAL)
    gr_results.to_excel(writer, 'Sheet1', index=False)
    writer.save()


def sort_active_data():
    """
    Function to sort the Dataframe and then spreadsheet by Campus ID
    entry and then by campusID
    """
    active_data = pd.read_excel(ACTIVE_students_FINAL, sheet_name=0)
    sorted_by_CWID = active_data.sort_values(['Campus Id'], ascending=True)

    writer = pd.ExcelWriter(ACTIVE_students_FINAL, engine='openpyxl')
    writer.book = ACTIVE_students
    writer.sheets = dict((ws.title, ws) for ws in ACTIVE_students.worksheets)

    sorted_by_CWID.to_excel(writer, 'Sheet', index=False)
    writer.save()


def print_active_work_done():
    work_output = ["-New Excel workbook built",
                   "-Read ISSM Report",
                   "-Read SEVIS Report",
                   "-Data between reports matched on SEVIS ID",
                   "-Matched Advisors based on Major data",
                   "-Build custom notes for Advisors to work from",
                   "-New Data saved to ACTIVE_Final workbook",
                   "-Sorted by CWID"]
    for work in work_output:
        time.sleep(0.3)
        print(work)


if __name__ == '__main__':
    start_time = time.time()
    match_active_advisor(merge_active_data(), ug_final_df, gr_final_df)
    sort_active_data()
    print("--- %s seconds ---" % (time.time() - start_time))
