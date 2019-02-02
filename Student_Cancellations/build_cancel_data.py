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

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
banner_status = df['05 Banner Student Status'].tolist()

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
cr_hours = df['07 Total Credit Hours'].tolist()

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
check_in_status = df['14 CHECK IN I94 or Entry Stamp'].tolist()

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
apdc_code = df['28 Latest Decision'].tolist()

df = pd.ExcelFile(No_show_UG).parse('No-Shows-UG')
level_of_ed = df['Level of Education (display)'].tolist()


Cancel_SEVISID_CampusID = dict(zip(SEVISID, campusID))

Cancel_SEVISID_major = dict(zip(SEVISID, major_data))

Cancel_SEVISID_banner = dict(zip(SEVISID, banner_status))

Cancel_SEVISID_credits = dict(zip(SEVISID, cr_hours))

Cancel_SEVISID_SV = dict(zip(SEVISID, check_in_status))

Cancel_APDC = dict(zip(SEVISID, apdc_code))

Cancel_Level = dict(zip(SEVISID, level_of_ed))

