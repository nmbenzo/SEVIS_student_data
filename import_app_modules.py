import os
os.getcwd()
from import_modules import *


GLBL_USER_CHOICE = """
Please select one of the following:
- 'n' - Access NEW Student Module
- 'a' - Access ACTIVE Student Module
- 'c' - Access COMPLETED Student Module
- 'g' - Access GRADUATED Module
- 's' - Sync Data with Google Sheets
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


# Need to add Completed_student_cleaning


