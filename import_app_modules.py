import os
os.getcwd()

from SEVIS_grad_data.build_grad_data import ws, campusID_SEVISID, \
    campusID_work_auth, campusID_end_date, campusID_workend, campusID_emails
from major_advisor_data import master_deg_adv, bachelor_deg_adv
from SEVIS_grad_data.build_graduated_student_data import add_advisor, \
    match_SEVISID, add_work_type, add_emails, add_work_enddate, \
    add_profile_enddate

from Compeleted_student_cleaning import build_comp_data, populate_data

from Active_students_requiring_registration import build_data, maj_adv_data, populate_data
from Active_students_requiring_registration.populate_data import match_SEVISID, \
match_major_data, match_advisor, advisor_major_ug, advisor_major_gr

from New_Student_Registration import build_student_data, build_new_student_advisor_notes
from New_Student_Registration.build_student_data import campusID_SEVISID, wb2, ws1, ws2, SEVISID_major
from New_Student_Registration.build_new_student_advisor_notes import match_SEVISID, \
match_major_data, match_advisor, add_advisor_notes, advisor_major_gr, advisor_major_ug


GLBL_USER_CHOICE = """
Please select one of the following:
- 'n' - Access NEW Student Module
- 'a' - Access ACTIVE Student Module
- 'c' - Access COMPLETED Student Module
- 'g' - Access GRADUATED Module
- 's' - Sync XLSX with Google Sheets
- 'e' - Send Email
- 'q' - Quit

"""


NEWs_USER_CHOICE = """
Please select one of the following:
- 'a' - Run all functions
- 'ad' - Add Advisor
- 'm' - Match SEVISID with CampusID
- 'w' - Match Major Data
- 'n' - Add Advisor Notes

"""


ACTIVEs_USER_CHOICE = """
Please select one of the following:
- 'a' - Run all functions
- 'm' - Match SEVISID with CampusID
- 'w' - Match Major Data
- 'e' - Match Advisor

"""


GRADUATEs_USER_CHOICE = """
Please select one of the following:
- 'a' - Run all functions
- 'ad' - Add Advisor
- 'm' - Match SEVISID with CampusID
- 'w' - Add Work Authorization Type
- 'e' - Add Work End Date
- 'p' - Add Profile End Date
- 's' - Update Cell Email

"""

SYNC_GOOGLESHEETS = """
Which xlsx file would you like to upload to GoogleSheets: 
- 'n' - NEW Student Reg xlsx
- 'a' - ACTIVE Student Reg xlsx
- 'g' - GRADUATED Student xlsx
- 'c' - COMPLETED Student xlsx

"""

EMAIL_TO_STUDENT_template = """
Choose an email template to send to the student: 
- 'c' - MANDATORY CHECK-IN INCOMPLETE
- 'o' - ISSS ORIENTATION INCOMPLETE
- 'a' - INSUFFICIENT / INACCURATE STUDENT DATA
- 'i' - I-901 FEE DUE

"""

EMAIL_TO_STUDENT_population = """
Which population would you like to send this email to: 
- 'n' - NEW Student Reg xlsx
- 'a' - ACTIVE Student Reg xlsx

"""


# Need to add Completed_student_cleaning


