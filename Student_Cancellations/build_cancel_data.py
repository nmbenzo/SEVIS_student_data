import os
os.getcwd()
import pandas as pd
from Handlers.file_imports import No_show_UG

"""
This module builds dictionaries containing the following data:
campusIDs : SEVISIDs
SEVISIDs : Majors

"""

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
SEVISID = df['SEVIS ID'].tolist()

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
campusID = df['Campus Id'].tolist()

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
major_data = df['Major Field (display)'].tolist()

Cancel_SEVISID_CampusID = dict(zip(SEVISID, campusID))

Cancel_SEVISID_major = dict(zip(SEVISID, major_data))
