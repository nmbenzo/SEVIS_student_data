from SEVIS_Graduated_Data.build_grad_data import campusID_SEVISID, \
    campusID_work_auth, campusID_end_date, campusID_workend, campusID_emails
from Handlers.major_advisor_data import master_deg_adv, bachelor_deg_adv

from Active_Students_Requiring_Registration.build_data import \
active_campusID_SEVISID, active_SEVISID_major, active_SEVISID_units, \
sevisID_emails

from New_Student_Registration.build_student_data import campusID_SEVISID, \
    SEVISID_major, SEVISID_checked_in, SEVISID_cr_hours, sevisid

from Student_Cancellations.build_cancel_data import Cancel_SEVISID_CampusID, \
Cancel_SEVISID_banner, Cancel_SEVISID_credits, Cancel_SEVISID_major, \
Cancel_SEVISID_SV, Cancel_APDC, Cancel_Level

from Handlers.major_advisor_data import advisor_major_ug, advisor_major_gr