import pandas as pd
import csv
from Handlers.directories import path_to_raw_data
from Banner_Connections.queries import cipe_graduated_students_query
from Banner_Connections.Initialize_Oracle_Connection import banner_ods_handler


issm_opt_data = path_to_raw_data + '2020/Spring/Raw_Files/Program_End_Date_Report_with_OPT.csv'
cipe_export = '/Users/nbenzschawel/Downloads/CIPE_grad_OPT_list.xlsx'
issm_all_data = path_to_raw_data +\
				'2020/Spring/Raw_Files/Active_Status_Students - no_PED_limitation.csv'


def build_grad_opt_status():
    """
    A function that merges data from a CIPE Academic Outcome query
    with OPT data out of ISSM for a given term
    """
    issm_data = pd.read_csv(issm_opt_data) # only OPT data
    issm_data.rename(columns={'Campus Id': 'CAMPUS_ID'}, inplace=True)
    issm_data_all = pd.read_csv(issm_all_data) # all SEVIS active ISSM data
    issm_data_all.rename(columns={'Campus Id': 'CAMPUS_ID'}, inplace=True)
    cipe_grad_data = pd.read_sql_query(cipe_graduated_students_query(), banner_ods_handler())

    # convert CIPE and ISSM CAMPUS_ID values to integer so you can merge with ISSM data
    cipe_grad_data['CAMPUS_ID'] = cipe_grad_data['CAMPUS_ID'].astype(int)
    # issm_data_all['CAMPUS_ID'] = issm_data_all['CAMPUS_ID'].astype(int)

    add_PED = pd.merge(cipe_grad_data, issm_data_all[['CAMPUS_ID','SEVIS ID',
                        'Profile End Date']], on='CAMPUS_ID', how='left')

    cipe_merge = pd.merge(add_PED, issm_data[['CAMPUS_ID',
                        'F Work Authorization Type',
                        'Work Auth Begin Date', 'Work Auth Begin Date','EMail']],
                          on='CAMPUS_ID', how='left')

    sorted = cipe_merge.sort_values(['SEVIS ID', 'GRADUATION_STATUS'], ascending=True)

    sorted.to_csv(cipe_export, header=True, index=None, sep=' ',
                  quoting=csv.QUOTE_NONE, escapechar=' ', mode='a')

    with pd.ExcelWriter(cipe_export, mode='w') as writer:
        sorted.to_excel(writer, 'Sheet1', index=False,
                                 engine='openpyxl')
        writer.save()
