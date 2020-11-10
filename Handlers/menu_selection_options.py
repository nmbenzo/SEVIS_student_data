import os
os.getcwd()

GLBL_USER_CHOICE = """
Please select one of the following to begin workflow:
- 'b' - Build Complete SEVIS Registration Worksheet
- 'f' - Build FINAL Complete SEVIS Registration Worksheet
- 's' - Sync Data with Google Sheets
- 'm' - Send SMS Message
- 'e' - Send Emails
- 't' - Transfer Student Menu
- 'n' - Access NEW Student Menu
- 'a' - Access ACTIVE Student Menu
- 'c' - Access CANCELLED Student Menu
- 'd' - Access COMPLETED Student Menu
- 'g' - Access GRADUATED Menu
- 'q' - Quit
"""

BUILD_REG_DATA = """
Would you like to build a COMPLETE list of SEVIS Registration data (y/n)?: 
"""

SYNC_GOOGLESHEETS = """
Select what you would like to do with the Google_Drive: 
- 'a' - Upload MASTER File xlsx
- 'd' - Download Updated G-Drive File
- 'r' - Registration Timeline
"""

SMS_MESSAGE = """
Please select one of the following:
- 's' - Send singular SMS Message
- 'b' - Send SMS Blast
"""

EMAIL_TO_STUDENT_template = """
Choose an email template to send to the student: 
- 'e' - Email to Singular Student
- 'm' - Email to Multiple Students
"""

EMAIL_TO_STUDENT_type = """
Which which email would you like to send: 
- 'f' - Students who have not paid the I-901 fee
- 'u' - Students who are underenrolled 
- 'p' - Students who have a bad phone number in ISSM
- 'a' - Students who have a bad address in ISSM
"""

MANAGE_TRANSFER_DATA = """
Please select one of the following:
- 'n' - Create New Workbook
- 'a' - Run all functions for copying and sorting Transfer data
- 's' - Sort Data by SEVIS ID
- 'p' - Add notes for ISSM
- 'f' - Copy data to Final for Atlas Sheet
- 'u' - Update ISSM notes in Final for Atlas Sheet
- 'c' - Copy & Paste final data in Sheet1
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
