import time
import pandas as pd
from Handlers.file_imports import TRANS_students_FINAL, \
transfer_stud_issm_data_S20, transfer_stud_sevis_data_S20, TRANS_students


def merge_trans_data():
    """
    The function reads two csv files in  two separate DataFrames
    and then merges them on a common Series value and returns a
    copy of the sliced DataFrame as an object to be passed as
    an argument.
    """
    transfer_issm = pd.read_csv(transfer_stud_issm_data_S20)
    transfer_sevis = pd.read_csv(transfer_stud_sevis_data_S20)

    results = pd.merge(transfer_sevis, transfer_issm[
             ['Campus Id', 'SEVIS ID', 'Level of Education (display)',
             'Profile Status', 'Profile Start Date', '05 Banner Student Status',
             '03 Student Status Term', '07 Total Credit Hours',
             'Major Field (display)', '14 CHECK IN I94 or Entry Stamp',
             'E-mail Address']], on='SEVIS ID', how='left')
               #indicator=True)
    cleaned_results = \
        results.drop_duplicates(subset=['SEVIS ID'], keep='first').copy()
    # make a copy of the DataFrame to remove SettingWithCopyWarning: A value is trying to be set
    # on a copy of a slice from a DataFrame warning message
    cleaned_results.rename(columns={'Profile Status':'ISSM SEVIS STATUS'},
                           inplace=True)
    return cleaned_results

def organize_merged_data(cleaned_results):
    """
    A function which receives a pd DataFrame object and then rearranges
    the columns for readability and sorts them by the I-94 Entry column
    """
    # rearranges DataFrame object's columns
    cleaned_results = cleaned_results[['SEVIS ID','Campus Id',
    'Class of Admission','Surname/Primary Name','Given Name',
    'ISSM SEVIS STATUS','Profile Start Date','14 CHECK IN I94 or Entry Stamp',
    'Level of Education (display)','Major Field (display)',
    '05 Banner Student Status','03 Student Status Term','07 Total Credit Hours',
    'Release Date','From School Name Campus Name','From School Code',
    'Request Status','Student Status','E-mail Address']]

    cleaned_results.insert(loc=0, column='Registration Status', value='')
    cleaned_results.insert(loc=0, column='Transfer Complete I-20 Issued',
                           value='')
    # sorts DataFrame by I-94 Entry column in ascending values
    sorted_by_I94 = cleaned_results.sort_values(['14 CHECK IN I94 or Entry Stamp'],
                                           ascending=True)
    with pd.ExcelWriter(TRANS_students_FINAL, mode='w') as writer:
        sorted_by_I94.to_excel(writer,'Sheet1', index=False, engine='openpyxl')
        writer.save()
    writer.close()

def sort_trans_data():
    """
    Sorts data by specified coloumn name via the sort_values
    function in pandas
    """
    trans_data = pd.read_excel(TRANS_students_FINAL, sheet_name=0)
    sorted_by_I94 = trans_data.sort_values(['14 CHECK IN I94 or Entry Stamp'],
                                           ascending=True)
    writer = pd.ExcelWriter(TRANS_students_FINAL, engine='openpyxl')
    writer.book = TRANS_students
    writer.sheets = dict((ws.title, ws) for ws in TRANS_students.worksheets)

    sorted_by_I94.to_excel(writer, 'Sheet', index=False)
    writer.save()

def print_trans_work_done():
    """Prints out list of what the functions did did"""
    work_output = ["-New Excel workbook built",
                   "-Read ISSM Report",
                   "-Read SEVIS Report",
                   "-Data between reports matched on SEVIS ID",
                   "-New Data saved to TRANSFER_Final workbook",
                   "-Sorted by I-94 Entry Stamp"]
    for work in work_output:
        time.sleep(0.3)
        print(work)

