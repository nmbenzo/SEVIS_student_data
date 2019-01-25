import openpyxl


"""Master Upload File"""

Registration_file = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/SEVIS Registration Spring 2019.xlsx'


""" File Location for Google_Drive.drive_main.py"""
location_a = '/Users/nbenzschawel/Library/Mobile Documents/com~apple~CloudDocs/Udemy_Python/SEVIS_Application/SEVIS Registration.xlsx'
location_b = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/SEVIS Registration Live.xlsx'


""" COL Student Data """

COL_students_raw = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/Change_of_Level_(COL)_Students.xlsx'

COL_students_FINAL = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Final Workbooks/COL_Final.xlsx'

COL_wb = openpyxl.Workbook()

try:
	COL_students = openpyxl.load_workbook(COL_students_FINAL)
	COL_students_sheet = COL_students.worksheets[0]
except FileNotFoundError:
	COL_wb.save(COL_students_FINAL)
	COL_students = openpyxl.load_workbook(COL_students_FINAL)
	COL_students_sheet = COL_students.worksheets[0]
	
	
""" New Student Data """

# ISSM Report: SEVIS Registration Tracking-New Students-SEVIS Pending
new_stud_issm_data = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/SEVIS_Registration_Tracking-New_Students-SEVIS_Pending.xlsx'

# SEVIS Report: Initial Status Students
sevis_inital_student_data = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/SEVIS_Raw_Data.xlsx'

NEW_students_FINAL = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Final Workbooks/NEW_Final.xlsx'

NEW_wb = openpyxl.Workbook()

try:
	NEW_students = openpyxl.load_workbook(NEW_students_FINAL)
	NEW_students_sheet = NEW_students.worksheets[0]
except FileNotFoundError:
	NEW_wb.save(NEW_students_FINAL)
	NEW_students = openpyxl.load_workbook(NEW_students_FINAL)
	NEW_students_sheet = NEW_students.worksheets[0]

wb1_new = openpyxl.load_workbook(new_stud_issm_data)  # workbook from ISSM
wb2_new = openpyxl.load_workbook(
	sevis_inital_student_data)  # workbook from SEVIS RTI

ws1_new = wb1_new.active
ws2_new = wb2_new.active


""" SEVIS Active Student Data """

active_stud_issm_data = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/All_SEVIS-Active_Student_Tracking.xlsx'

active_student_req_reg = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/Fall 201840 - Registration.xlsx'

ACTIVE_students_FINAL = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Final Workbooks/ACTIVE_Final.xlsx'

ACTIVE_wb = openpyxl.Workbook()

try:
	ACTIVE_students = openpyxl.load_workbook(ACTIVE_students_FINAL)
	ACTIVE_students_sheet = ACTIVE_students.worksheets[0]
except FileNotFoundError:
	ACTIVE_wb.save(ACTIVE_students_FINAL)
	ACTIVE_students = openpyxl.load_workbook(ACTIVE_students_FINAL)
	ACTIVE_students_sheet = ACTIVE_students.worksheets[0]

wb2_active = openpyxl.load_workbook(active_student_req_reg)
sheet = wb2_active.worksheets[4]
ws2 = wb2_active.active

wb1 = openpyxl.load_workbook(active_stud_issm_data)
ws = wb1.active

""" Transfer Student Data """

new_transfer_data = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/SEVIS - Students Transferring In.xlsx'

current_transfer_data = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/SEVIS_transfer_data.xlsx'

wb_trans = openpyxl.load_workbook(new_transfer_data)
wb2_trans = openpyxl.load_workbook(current_transfer_data)
old_sheet = wb_trans.worksheets[0]
new_sheet = wb2_trans.worksheets[1]
final_sheet = wb2_trans.worksheets[0]

row_max_old = old_sheet.max_row
col_max_old = old_sheet.max_column

row_max_current = new_sheet.max_row
col_max_current = new_sheet.max_column

row_max_final = final_sheet.max_row
col_max_final = final_sheet.max_column


""" No Show-Cancels for Admissions"""

SEVIS_initial_status_stud = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/SEVIS - Initial Status Students.xlsx'

No_show_UG = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/No-Shows-UG.xlsx'

No_show_GR = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/No-Shows-Grad.xlsx'

No_SHOW_students_FINAL = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Final Workbooks/NO_SHOW_Final.xlsx'

No_SHOW_wb = openpyxl.Workbook()

try:
	NO_SHOW_students = openpyxl.load_workbook(No_SHOW_students_FINAL)
	NOSHOW_students_sheet = NO_SHOW_students.worksheets[0]
except FileNotFoundError:
	No_SHOW_wb.save(No_SHOW_students_FINAL)
	NO_SHOW_students = openpyxl.load_workbook(No_SHOW_students_FINAL)
	NOSHOW_students_sheet = NO_SHOW_students.worksheets[0]

SEV_initial_data = openpyxl.load_workbook(SEVIS_initial_status_stud)
wb_cancel_ug = openpyxl.load_workbook(No_show_UG)
wb_cancel_gr = openpyxl.load_workbook(No_show_GR)

sevis_initial = SEV_initial_data.worksheets[0]
ug_sheet = wb_cancel_ug.worksheets[0]
gr_sheet = wb_cancel_gr.worksheets[0]

initial_max_row = sevis_initial.max_row
ug_row_max = ug_sheet.max_row
ug_col_max = ug_sheet.max_column
gr_row_max = gr_sheet.max_row
gr_col_max = gr_sheet.max_column

sevis_initial_ws = SEV_initial_data.active
ws_cancel_ug = wb_cancel_ug.active
ws_cancel_gr = wb_cancel_gr.active


""" Completed Student Data """

comp_student_cleanup_report = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/Completed_Students_Cleanup_Report_201840.xlsx'

sevis_completed_students = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/SEVIS - Completed Status Students (past 18 months).xlsx'

completed_student_wb2 = openpyxl.load_workbook(comp_student_cleanup_report)

comp_sheet = completed_student_wb2.worksheets[0]

comp_ws = completed_student_wb2.active

wb1_complete = openpyxl.load_workbook(sevis_completed_students)

ws1 = wb1_complete.active


""" Graduated Student Data """

graduated_students = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/201820_201830_graduated_students.xlsx'
wb1_grad = openpyxl.load_workbook(active_stud_issm_data)

sheet_grad = wb1_grad.worksheets[0]
ws_grad = wb1_grad.active

# Think about adding a try, except function here to check the file directory.
wb2_grad = openpyxl.load_workbook(
	'/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/201840_graduated_students_test.xlsx'
)
wb3Live_grad = openpyxl.load_workbook(graduated_students)

sheet2_grad = wb2_grad.worksheets[0]
sheet3_grad = wb3Live_grad.worksheets[0]

ws2_grad = wb2_grad.active
ws3_grad = wb3Live_grad.active


"""SEVIS Registration Timelines"""

current_registration_timeline = '/Volumes/ISS/Staff Only/Student Lists/SEVIS Registration/SEVIS Registration Timelines/SEVIS REGISTRATION 19S.docx'


"""DQ'ed Student List"""

DQ_student_list = "/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/International Students DQ'd.xlsx"

DQ_wb = openpyxl.load_workbook(DQ_student_list)

most_recent_term = DQ_wb.worksheets[0]


"""J-1 Students"""

J_students_FINAL = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/Raw_Files/SEVIS_Validation_Tracking - New_EVs.xlsx'
J_wb = openpyxl.Workbook()

try:
	J_students = openpyxl.load_workbook(J_students_FINAL)
	J_students_sheet = J_students.worksheets[0]
except FileNotFoundError:
	J_wb.save(J_students_FINAL)
	J_students = openpyxl.load_workbook(J_students_FINAL)
	J_students_sheet = J_students.worksheets[0]

