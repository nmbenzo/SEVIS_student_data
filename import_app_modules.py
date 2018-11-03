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
