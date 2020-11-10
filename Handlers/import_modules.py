"""
Centralized file for importing program functions used by Handlers.menus.py
"""

from SEVIS_Graduated_Data.populate_graduated_data import add_advisor, \
    match_SEVISID, add_work_type, add_emails, add_work_enddate, \
    add_profile_enddate

from Compeleted_Student_Cleaning import build_comp_data, populate_completed_data
from Compeleted_Student_Cleaning.populate_completed_data import \
match_SEVISID_completed
from Compeleted_Student_Cleaning.build_comp_data import SEVISID_completed

from Active_Students_Requiring_Registration import build_data, \
populate_active_data
from Active_Students_Requiring_Registration.populate_active_data import \
create_active_Student_Data, active_match_SEVISID, match_major_data, \
match_advisor, match_units, add_graduated_student_emails, add_notes_column, \
add_registration_status_column, add_graduation_status_column
from Active_Students_Requiring_Registration.sort_active_data import \
sort_active_data

from New_Student_Registration import build_student_data, \
populate_new_student_notes
from New_Student_Registration.populate_new_student_notes import \
create_new_Student_Data, new_match_SEVISID, new_match_major_data, \
new_match_advisor, add_advisor_notes, add_registration_column
from New_Student_Registration.sort_new_data import sort_new_data

from SEVIS_Transfers.sort_data import sort_data, remove_duplicates
from SEVIS_Transfers.populate_transfer_data import create_new_Data, \
paste_to_final, \
transfer_match_major_data, grab_final_data, check_in_fsa, find_in_fsa
from SEVIS_Transfers.create_workbook import create_workbook

from Student_Cancellations.populate_cancel_list import create_new_Cancel_Data, \
create_NoShow_Student_Data, build_apdc_notes, build_cancel_campusID, \
build_cancel_notes, build_level_data, NOSHOW_students_sheet, ug_row_max, ug_sheet

from File_Management.merge_files import merge_all_workbooks, \
final_merge_all_workbooks

from DQed_Automation.build_dq_data import campusID_major

from Google_Drive.drive_main import *

from Handlers.Google_Drive_IDs import folder_id, Registration_file, \
SHEET_MIMETYPE, FOLDER_MIME, MASTER_FILE, NEW_SOURCE_FILE, ACTIVE_SOURCE_FILE, \
TRANSFER_SOURCE_FILE, REGISTRATION_TIMELINE, DOC_MIMETYPE, Excel, file_name, \
uploaded_file_name, drive_file_name

from Emails.gmail_main import *

from Twilio_SMS.send_sms import *

