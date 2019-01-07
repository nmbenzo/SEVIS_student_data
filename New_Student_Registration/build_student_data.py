import os
os.getcwd()
import pandas as pd
from Handlers.file_imports import new_stud_issm_data, sevis_inital_student_data

"""
This file builds dictionaries containing the following data: 
campusIDs : SEVISIDs
SEVISIDs : Majors
SEVISIDs : I-94 Check-In Status
SEVISIDs : Registered Units

"""

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
SEVISID = df['SEVIS ID'].tolist()

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
campusID = df['Campus Id'].tolist()

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
major_data = df['Major Field (display)'].tolist()

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
checked_in = df['14 CHECK IN I94 or Entry Stamp'].tolist()

df = pd.ExcelFile(new_stud_issm_data).parse('SEVIS_Registration_Tracking-New')
cr_hours = df['07 Total Credit Hours'].tolist()

df = pd.ExcelFile(sevis_inital_student_data).parse('Sheet1')
sevisid = df['SEVIS ID'].tolist()


# build dict where k = SEVISID, v = campusID
campusID_SEVISID = {}

for i in range(len(SEVISID)):
    campusID_SEVISID[SEVISID[i]] = campusID[i]

# build a dict where k = SEVISID, v = list of majors
SEVISID_major = dict(zip(SEVISID, major_data))

SEVISID_checked_in = dict(zip(SEVISID, checked_in))

SEVISID_cr_hours = dict(zip(SEVISID, cr_hours))

