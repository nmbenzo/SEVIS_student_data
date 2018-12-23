import os
os.getcwd()
import pandas as pd
from Handlers.file_imports import new_stud_issm_data, sevis_initalstat_data

"""
This file builds dictionaries containing the following data: 
campusIDs : SEVISIDs
SEVISIDs : Majors

"""

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
SEVISID = df['SEVIS ID'].tolist()

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
campusID = df['Campus Id'].tolist()

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
major_data = df['Major Field (display)'].tolist()

df = pd.ExcelFile(sevis_initalstat_data).parse('Sheet1')
sevisid = df['SEVIS ID'].tolist()


# build dict where k = SEVISID, v = campusID
campusID_SEVISID = {}

for i in range(len(SEVISID)):
    campusID_SEVISID[SEVISID[i]] = campusID[i]


# build a dict where k = SEVISID, v = list of majors
SEVISID_major = dict(zip(SEVISID, major_data))


# Old OPENPYXL methods
# campusID = []
# SEVISID = []
# for rowNum in range(2, ws1_new.max_row):  # skip the first row and go to the last row
    # id = ws1_new.cell(row=rowNum, column=5).value
    # SEVISID.append(id)

# for rowNum in range(2, ws1_new.max_row):
    # id = ws1_new.cell(row=rowNum, column=1).value
    # campusID.append(id)

# build a list of majors
# major_data = []

# for rowNum in range(2, ws1_new.max_row):
   # major = ws1_new.cell(row=rowNum, column=13).value
   # major_data.append(major)