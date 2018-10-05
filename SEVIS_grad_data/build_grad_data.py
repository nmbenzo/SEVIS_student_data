import os
os.getcwd()
import openpyxl
from openpyxl.styles import NamedStyle

wb1 = openpyxl.load_workbook('/Users/nbenzschawel/Downloads/All_SEVIS-Active_Student_Tracking.xlsx')


sheet = wb1.worksheets[0]

ws = wb1.active


campusID = []

for rowNum in range(2, ws.max_row):
    id = ws.cell(row=rowNum, column=1).value
    campusID.append(id)

SEVISID = []

for rowNum in range(2, ws.max_row):
    id = ws.cell(row=rowNum, column=5).value
    SEVISID.append(id)


campusID_SEVISID = {}

for i in range(len(campusID)): # verbose dict building
    campusID_SEVISID[campusID[i]] = SEVISID[i]


work_auth_type = []

for rowNum in range(2, ws.max_row):
    type = ws.cell(row=rowNum, column=31).value # need to check column in spreadsheet
    work_auth_type.append(type)

campusID_work_auth = dict(zip(campusID, work_auth_type))


profile_end_date = []

for rowNum in range(2, ws.max_row):
    end_date = ws.cell(row=rowNum, column=10).value # need to check column in spreadsheet
    profile_end_date.append(end_date)

campusID_end_date = dict(zip(campusID, profile_end_date))


work_auth_enddate = []

for x in range(2, ws.max_row):
    work_end = ws.cell(row=x, column=33).value # need to check column in spreadsheet
    work_auth_enddate.append(work_end)

campusID_workend = dict(zip(campusID, work_auth_enddate))


emails = []
email_campID = []

for x in range(2, ws.max_row):
    email = ws.cell(row=x, column=30).value # need to check column in spreadsheet
    emails.append(email)

for x in range(2, ws.max_row):
    campusID = ws.cell(row=x, column=1).value
    email_campID.append(campusID)

campusID_emails = dict(zip(email_campID, emails))




