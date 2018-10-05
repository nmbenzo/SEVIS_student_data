import os
os.getcwd()
import openpyxl


wb1 = openpyxl.load_workbook('SEVIS_Registration_Tracking-New_Students-SEVIS_Pending.xlsx')
wb2 = openpyxl.load_workbook('SEVIS_raw_data.xlsx')

ws1 = wb1.active
ws2 = wb2.active

campusID = []
SEVISID = []

for rowNum in range(2, ws1.max_row):  # skip the first row and go to the last row
    id = ws1.cell(row=rowNum, column=5).value
    SEVISID.append(id)

for rowNum in range(2, ws1.max_row):
    id = ws1.cell(row=rowNum, column=1).value
    campusID.append(id)

# build dict where k = SEVISID, v = campusID
campusID_SEVISID = {}

for i in range(len(SEVISID)):
    campusID_SEVISID[SEVISID[i]] = campusID[i]

# build a list of majors
major_data = []

for rowNum in range(2, ws1.max_row):
    major = ws1.cell(row=rowNum, column=13).value
    major_data.append(major)

# build a dict where k = SEVISID, v = list of majors
SEVISID_major = dict(zip(SEVISID, major_data))









