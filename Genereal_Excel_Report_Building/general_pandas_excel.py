import pandas as pd
from Banner_Connections.Initialize_Oracle_Connection import read_query_to_df

tds_data_path = '/Users/nbenzschawel/Downloads/TDS_data/'
sevis_reg_path = '/Users/nbenzschawel/Downloads/SEVIS_Reg/'

pod_data = tds_data_path + 'UG Active Students with Departure info.csv'
active_students = tds_data_path + 'all_active_students.csv'
sl_data = tds_data_path + 'Summer 2020 Calls_International - Copy of International - All.csv'

def add_departure_dates():
    active_df = pd.read_csv(pod_data)
    sl_students = pd.read_csv(sl_data)
    pod_students = pd.read_csv(pod_data)

    results = pd.merge(sl_students, pod_students[
        ['EMAIL_USF', 'Date of Departure']],
                       on='EMAIL_USF', how='left')

    results.to_csv(sl_data, index=False)
    print('Aggregation Complete!')



program_end_date = sevis_reg_path + 'Program_End_Date_Report-No_OPT.csv'
banner_202040_units = sevis_reg_path + '202040_registered_students.csv'
ped_audit_202040 = sevis_reg_path + '202040_PED_audit.csv'

banner_202030_units = sevis_reg_path + '202030_registered_students.csv'
ped_audit_202030 = sevis_reg_path + '202030_PED_audit.csv'

def merge_PED_future_reg():
    ped_df = pd.read_csv(program_end_date)
    banner_data = read_query_to_df()
    banner_data['CAMPUS_ID'] = banner_data['CAMPUS_ID'].astype(int)

    #convert column names to match
    ped_df.rename(columns = {'Campus Id': 'CAMPUS_ID'}, inplace = True)
    ped_df.rename(columns = {'Email1': 'SEVIS_PED'}, inplace = True)

    results = pd.merge(ped_df, banner_data[['CAMPUS_ID',
                      'MOST_RECENT_REGISTERED_TERM','BILLING_CREDITS']],
                       on='CAMPUS_ID',how='left')

    sorted_results = results.sort_values(['MOST_RECENT_REGISTERED_TERM'], ascending=True)
    sorted_results.to_csv(ped_audit_202030, index=False)
    print('Auditing Complete')


merge_PED_future_reg()

