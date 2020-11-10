import os
os.getcwd()


GLBL_USER_CHOICE = """
Please select one of the following to begin workflow:
- 'M' - View the Main Menu options
- 'R' - View SQL query options"""

QUERY_OUTPUT = """
'Would you like to print a query or port it to a Dataframe?
- 'p' - Print query to console
- 'd' - Port query data to DataFrame
- 'r' - Run query of choice and export to XLSX file
"""


GLBL_MAIN_USER_CHOICE = """
Please select one of the following to begin workflow:
- 'b' - Build Complete SEVIS Registration Worksheet
- 'f' - Build FINAL Complete SEVIS Registration Worksheet
- 's' - Sync Data with Google Sheets
- 'm' - Send SMS Message
- 'e' - Send Emails
- 'n' - Access NEW Student Menu
- 'a' - Access ACTIVE Student Menu
- 'c' - Access CANCELLED Student Menu
- 'g' - Access GRADUATED Student Menu
- 'q' - Quit
"""


BUILD_REG_DATA = """
Would you like to build a COMPLETE list of SEVIS Registration data (y/n)?: 
"""


CHOOSE_QUERY = """
Please select one of the following queries to run:
- 'n' - Get new students query
- 't' - Get single telephone by CWID query
- 'e' - Get single USF email by CWID query
- 'c' - Get list of all AS student cellphones query
- 'cb' - City of Birth query by admit term(s)
- 'loa' - Query LOA / WD students
- 'm' - Query cells by major
- 's' - Get list of all AS student emails query
- 'p' - Run CIPE Student query
- 'b' - Run Banner student query
- 'qm' - Query AS students by major
- 'gr' - Run CIPE graduated students query
- 'bs' - Blast cell test query
- 'cw' - Blast cellphone by CWID
- 'q' - Quit
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
- 'b' - Send SMS Blast from Banner Query
- 'cb' - Send SMS Blast from custom list
- 'ts' - Send single test message from Banner Query
- 'tb' - Send blast test message from Banner Query
- 'bl' - Send blast message from Banner Query
"""


EMAIL_TO_STUDENT_template = """
Choose an email template to send to the student: 
- 'e' - Email to Singular Student
- 'm' - Email to Multiple Students
- 'es' - Send single email message from Banner Query
- 'eb' - Send blast email message from Banner Query
"""

EMAIL_TO_STUDENT_type = """
Which email would you like to send: 
- 'f' - Students who have not paid the I-901 fee
- 'u' - Students who are underenrolled 
- 'p' - Students who have a bad phone number in ISSM
- 'a' - Students who have a bad address in ISSM
- 'lt' - Students whom we've Terminated due to LOA
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
"""


ACTIVEs_USER_CHOICE = """
Please select one of the following:
- 'a' - Run all functions
- 'e' - Match Advisor
"""


BUILD_CANCEL_CHOICE = """
Please select one of the following:
- 'a' - Run all functions
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
