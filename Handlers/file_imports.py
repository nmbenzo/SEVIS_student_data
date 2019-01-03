import openpyxl


"""Master Upload File"""

Registration_file = '/Users/nbenzschawel/Downloads/SEVIS_Reg/2019/Spring/SEVIS Registrion Spring 2019.xlsx'


""" SEVIS Active Student Data """
wb2_active = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/Fall 201840 - Registration.xlsx')
sheet = wb2_active.worksheets[4]
ws2 = wb2_active.active

wb1 = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/All_SEVIS-Active_Student_Tracking.xlsx')
ws = wb1.active

active_stud_issm_data = '/Users/nbenzschawel/Downloads/All_SEVIS-Active_Student_Tracking.xlsx'
active_student_req_reg = '/Users/nbenzschawel/Downloads/Fall 201840 - Registration.xlsx'


""" Transfer Student Data """
new_transfer_data = '/Users/nbenzschawel/Desktop/New_sevis_data.xlsx'
current_transfer_data = '/Users/nbenzschawel/Downloads/SEVIS_transfer_data.xlsx'

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


""" Completed Student Data """
wb1_complete = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/SEVIS - Completed Status Students (past 18 months).xlsx')

ws1 = wb1_complete.active


""" New Student Data """
wb1_new = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/SEVIS_Registration_Tracking-New_Students-SEVIS_Pending.xlsx') # workbook from ISSM
wb2_new = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx') # workbook from SEVIS RTI

ws1_new = wb1_new.active
ws2_new = wb2_new.active

new_stud_issm_data = '/Users/nbenzschawel/Downloads/SEVIS_Registration_Tracking-New_Students-SEVIS_Pending.xlsx'
sevis_inital_student_data = '/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx'


""" Graduated Student Data """
wb1_grad = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/All_SEVIS-Active_Student_Tracking.xlsx')
sheet_grad = wb1_grad.worksheets[0]
ws_grad = wb1_grad.active

# Think about adding a try, except function here to check the file directory.
wb2_grad = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/201840_graduated_students_test.xlsx')
wb3Live_grad = openpyxl.load_workbook('/Users/nbenzschawel/Desktop/fsaAtlas - Files/201820_201830_graduated_students.xlsx')

sheet2_grad = wb2_grad.worksheets[0]
sheet3_grad = wb3Live_grad.worksheets[0]

ws2_grad = wb2_grad.active
ws3_grad = wb3Live_grad.active


"""SEVIS Registration Timelines"""
current_registration_timeline = '/Volumes/ISS/Staff Only/Student Lists/SEVIS Registration/SEVIS Registration Timelines/SEVIS REGISTRATION 19S.docx'