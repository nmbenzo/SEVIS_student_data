
from SEVIS_Graduated_Data.build_grad_data import campusID_SEVISID, \
    campusID_work_auth, campusID_end_date, campusID_workend, campusID_emails
from Handlers.major_advisor_data import master_deg_adv, bachelor_deg_adv
from SEVIS_Graduated_Data.populate_graduated_data import add_advisor, \
    match_SEVISID, add_work_type, add_emails, add_work_enddate, \
    add_profile_enddate

from Compeleted_Student_Cleaning import build_comp_data, populate_completed_data
from Compeleted_Student_Cleaning.populate_completed_data import match_SEVISID_completed
from Compeleted_Student_Cleaning.build_comp_data import SEVISID_completed

from Active_Students_Requiring_Registration import build_data, maj_adv_data, populate_active_data
from Active_Students_Requiring_Registration.populate_active_data import create_active_Student_Data, active_match_SEVISID, \
match_major_data, match_advisor, match_units
from Active_Students_Requiring_Registration.build_data import active_campusID_SEVISID, active_SEVISID_major, active_SEVISID_units
from Active_Students_Requiring_Registration.sort_active_data import sort_active_data
from Handlers.major_advisor_data import advisor_major_ug, advisor_major_gr

from New_Student_Registration import build_student_data, populate_new_student_notes
from New_Student_Registration.build_student_data import campusID_SEVISID, SEVISID_major, \
SEVISID_checked_in, SEVISID_cr_hours, sevisid
from New_Student_Registration.populate_new_student_notes import create_new_Student_Data, new_match_SEVISID, \
new_match_major_data, new_match_advisor, add_advisor_notes
from New_Student_Registration.sort_new_data import sort_new_data
from Handlers.major_advisor_data import advisor_major_gr, advisor_major_ug

from SEVIS_Transfers.sort_data import sort_data, remove_duplicates
from SEVIS_Transfers.populate_transfer_data import create_new_Data, paste_to_final, \
transfer_match_major_data, grab_final_data, check_in_fsa, find_in_fsa
from SEVIS_Transfers.create_workbook import create_workbook

from Student_Cancellations.build_cancel_data import Cancel_SEVISID_CampusID, \
Cancel_SEVISID_banner, Cancel_SEVISID_credits, Cancel_SEVISID_major, Cancel_SEVISID_SV
from Student_Cancellations.populate_cancel_list import create_new_Cancel_Data, \
create_NoShow_Student_Data, build_cancel_campusID, build_cancel_notes, NOSHOW_students_sheet, ug_row_max, ug_sheet

from File_Management.merge_files import merge_all_workbooks

from DQed_Automation.build_dq_data import campusID_major

from Google_Drive.manage_team_drives import *
from Google_Drive.drive_authorization import *
from Google_Drive.drive_main import *

from Handlers.Google_Drive_IDs import folder_id, Registration_file, SHEET_MIMETYPE, \
FOLDER_MIME, MASTER_FILE, NEW_SOURCE_FILE, ACTIVE_SOURCE_FILE, TRANSFER_SOURCE_FILE, \
REGISTRATION_TIMELINE, DOC_MIMETYPE, Excel, file_name, uploaded_file_name

from Google_Drive.download_files import *

from Emails.authorization import *
from Emails.send_mail import *
from Emails.main import *