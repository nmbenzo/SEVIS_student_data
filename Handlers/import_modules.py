from tqdm import trange
import time


"""
Centralized file for importing program functions used by Handlers.menus.py
"""
print('Loading Code for Advisor Module')
for t in trange(100):
    time.sleep(0.01)
from Handlers.major_advisor_data import ug_major_advisor_df,\
gr_major_advisor_df

print('Loading Code for Active Students Module')
for t in trange(100):
    time.sleep(0.01)
from Active_Students_Requiring_Registration import populate_active_data
from Active_Students_Requiring_Registration.populate_active_data import \
merge_active_data, match_active_advisor, sort_active_data, \
print_active_work_done

print('Loading Code for Initial Students Module ')
for t in trange(100):
    time.sleep(0.01)
from New_Student_Registration import populate_new_student_notes
from New_Student_Registration.populate_new_student_notes import \
merge_new_data, match_new_advisor, add_advisor_notes, \
sort_new_data, print_new_work_done, dataframe_difference
# create_new_Student_Data, new_match_SEVISID, new_match_status_data, \
# new_match_term_data, new_match_major_data, add_columns, \
# new_match_advisor, new_match_level_data, add_advisor_notes

print('Loading Code for Transfer Students Module')
for t in trange(100):
    time.sleep(0.01)
from SEVIS_Transfers.populate_transfer_data import merge_trans_data, \
sort_trans_data, print_trans_work_done

print('Loading Code for Cancellations Module')
for t in trange(100):
    time.sleep(0.01)
from Student_Cancellations.populate_cancel_list import rename_worksheets, \
merge_no_show_data, sort_no_show_data, build_cancel_notes, \
print_no_show_work_done

print('Loading Code for Excel Module')
for t in trange(100):
    time.sleep(0.01)
from File_Management.merge_files import merge_all_workbooks, \
final_merge_all_workbooks

print('Loading Code for Graduated Students Module')
for t in trange(100):
    time.sleep(0.01)
from SEVIS_Graduated_Data.populate_graduated_data import build_grad_opt_status

print('Loading Code for GoogleDrive Module')
for t in trange(100):
    time.sleep(0.01)
from Google_Drive.drive_main import *

print('Loading Code for Authentications Module')
for t in trange(100):
    time.sleep(0.01)
from Handlers.Google_Drive_IDs import folder_id20, Registration_file, \
SHEET_MIMETYPE, FOLDER_MIME, MASTER_FILE, NEW_SOURCE_FILE, ACTIVE_SOURCE_FILE, \
TRANSFER_SOURCE_FILE, REGISTRATION_TIMELINE, DOC_MIMETYPE, Excel, file_name, \
uploaded_file_name, drive_file_name

print('Loading Code for Banner ODSP Module')
for t in trange(100):
    time.sleep(0.01)
from Banner_Connections.Initialize_Oracle_Connection import banner_ods_handler, \
banner_ODSP_tele, query_results_xlsx, read_query_to_df, print_query_results
from Banner_Connections.queries import choose_query

print('Loading Code for Gmail Module')
for t in trange(100):
    time.sleep(0.01)
from Emails.gmail_main import *

print('Loading Code for Twilio SMS Module')
for t in trange(100):
    time.sleep(0.01)
from Twilio_SMS.send_sms import *

print('Loading Complete!')
time.sleep(0.5)
print('Preparing menu options...')