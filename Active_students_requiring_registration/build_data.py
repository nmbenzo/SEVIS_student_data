import os
os.getcwd()
import openpyxl
from Handlers.file_imports import wb1, ws

campusID = []

for rowNum in range(2, ws.max_row):
    id = ws.cell(row=rowNum, column=1).value
    campusID.append(id)

SEVISID = []

for rowNum in range(2, ws.max_row):
    id = ws.cell(row=rowNum, column=5).value
    SEVISID.append(id)


campusID_SEVISID = dict(zip(SEVISID, campusID))


major_data = []

for rowNum in range(2, ws.max_row):
    major = ws.cell(row=rowNum, column=13).value
    major_data.append(major)


# build a dict where k = SEVISID, v = list of majors
SEVISID_major = dict(zip(SEVISID, major_data))


