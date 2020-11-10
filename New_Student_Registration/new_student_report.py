import os
import pandas as pd
from Banner_Connections.queries import get_new_students
from Banner_Connections.Initialize_Oracle_Connection import banner_ods_handler


try:
    data_path = '/Users/nbenzschawel/Downloads/Student I-20s'

    ISSM_data = os.path.join(data_path, 'All_SEVIS-Pending_Student_Tracking.csv')

    SEVIS_data = os.path.join(data_path, '202020_Starts.csv')

    export_path = '/Users/nbenzschawel/Downloads/New_Students_Report.xlsx'

    cipe_export = '/Users/nbenzschawel/Downloads/CIPE_list.xlsx'
except IOError:
    print("One or more files not found")


def build_new_student_report():
    """
    A function that reads csv files to a pandas dataframe
    and then merges this with a report of new students for a given date range
    pulled from SEVIS
    """
    pending_issm = pd.read_csv(ISSM_data)
    initial_sevis = pd.read_csv(SEVIS_data)

    # strip whitespace from SEVIS copy and paste
    initial_sevis['SEVIS ID'] = initial_sevis['SEVIS ID'].str.strip()
    # rename ISSM 'Campus Id' to 'CAMPUS_ID' to successfully merge with CIPE query
    pending_issm.rename(columns = {'Campus Id': 'CAMPUS_ID'}, inplace = True)
    pending_issm = pending_issm.drop_duplicates(subset='SEVIS ID', keep='first')

    results = pd.merge(initial_sevis, pending_issm[['SEVIS ID', 'CAMPUS_ID', 'Level of Education (display)',
        'Major Field (display)','04 Transfer From','06 Transfer In Date',
        '00 Banner I20 Remarks','03 Student Status Term','07 Total Credit Hours',
        '05 Banner Student Status','E-mail Address']], on='SEVIS ID', how='left')
    # indicator=True)
    sorted = results.sort_values(['CAMPUS_ID'], ascending=True)

    with pd.ExcelWriter(export_path, mode='w') as writer:
        sorted.to_excel(writer, 'Sheet1', index=False,
                                 engine='openpyxl')
        writer.save()


def build_new_student_cipe_report():
    """
    A function that reads an Oracle SQL query to a pandas dataframe
    and then merges this with a report of new students for a given date range
    pulled from SEVIS
    """
    pending_issm = pd.read_csv(ISSM_data)
    initial_sevis = pd.read_csv(SEVIS_data)

    # strip whitespace from SEVIS copy and paste
    initial_sevis['SEVIS ID'] = initial_sevis['SEVIS ID'].str.strip()
    # rename ISSM 'Campus Id' to 'CAMPUS_ID' to successfully merge with CIPE query
    pending_issm.rename(columns = {'Campus Id': 'CAMPUS_ID'}, inplace = True)
    pending_issm = pending_issm.drop_duplicates(subset='SEVIS ID', keep='first')

    CIPE = pd.read_sql_query(get_new_students(), banner_ods_handler())

    # convert CIPE CAMPUS_ID values to floats so you can merge with ISSM data
    CIPE['CAMPUS_ID'] = CIPE['CAMPUS_ID'].astype(float)

    cipe_merge = pd.merge(CIPE, pending_issm[['SEVIS ID', 'CAMPUS_ID']], on='CAMPUS_ID', how='left')

    cols = list(cipe_merge)
    # move the column to head of list using index, pop and insert
    cols.insert(0, cols.pop(cols.index('SEVIS ID')))
    # use loc to reorder
    cipe_merge = cipe_merge.loc[:, cols]

    with pd.ExcelWriter(cipe_export, mode='w') as writer:
        cipe_merge.to_excel(writer, 'Sheet1', index=False,
                                 engine='openpyxl')
        writer.save()

