import os
os.getcwd()
import openpyxl
import pandas as pd
from Handlers.file_imports import active_stud_issm_data


df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
SEVISID = df['SEVIS ID'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
campusID = df['Campus Id'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
major_data = df['Major Field (display)'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
units = df['07 Total Credit Hours'].tolist()


# build dict where k = SEVISID, v = campusID
active_campusID_SEVISID = dict(zip(SEVISID, campusID))

# build a dict where k = SEVISID, v = list of majors
active_SEVISID_major = dict(zip(SEVISID, major_data))

active_SEVISID_units = dict(zip(SEVISID, units))





