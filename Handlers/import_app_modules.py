import os
os.getcwd()

GLBL_USER_CHOICE = """
Please select one of the following:
- 'n' - Access NEW Student Menu
- 'a' - Access ACTIVE Student Menu
- 'c' - Access CANCELLED Student Menu
- 'd' - Access COMPLETED Student Menu
- 'g' - Access GRADUATED Menu
- 'm' - Access Merge Workbook Menu
- 's' - Sync Data with Google Sheets
- 'x' - Convert XLSX to CSV
- 't' - Transfer Student Menu
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


BUILD_CANCEL_CHOICE = """
Please select one of the following:
- 'a' - Run all functions
- 'm' - Merge UG and GR Cancel Lists
- 'p' - Populate Merged Cancel List

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


COMPLETED_STUDENTS = """
Would you like to generate a list of COMPLETED students in SEVIS vs ISSM Profile Status (y/n)?: 

"""


SYNC_GOOGLESHEETS = """
Which file would you like to upload to Google_Drive: 
- 'a' - Upload MASTER File xlsx
- 'n' - NEW Student Reg xlsx
- 'a' - ACTIVE Student Reg xlsx
- 't' - TRANSFER Students xlsx
- 'g' - GRADUATED Student xlsx
- 'c' - COMPLETED Student xlsx
- 'r' - Registration Timeline

"""


MERGE_WORKBOOKS = """
Would you like to merge all Registration Workbooks (y/n)?: 

"""


CONVERT_TO_CSV = """
Which xlsx file would you like to convert to CSV: 
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

MANAGE_TRANSFER_DATA = """
- 'n' - Create New Workbook
- 'a' - Add New Data to Sheet1
- 's' - Sort Data by SEVIS ID
- 'p' - Add notes for ISSM
- 'f' - Copy data to Final for Atlas Sheet
- 'u' - Update ISSM notes in Final for Atlas Sheet
- 'c' - Copy & Paste final data in Sheet1

"""

# Need to add Completed_student_cleaning


