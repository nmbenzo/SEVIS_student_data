import pandas as pd
from Handlers.file_imports import No_show_UG, No_show_GR

"""
This module builds dictionaries containing the following data:
campusIDs : SEVISIDs
SEVISIDs : Majors

"""


df = pd.read_excel(No_show_UG)
with pd.ExcelWriter(No_show_UG, mode='w') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()

df = pd.read_excel(No_show_GR)
with pd.ExcelWriter(No_show_GR, mode='w') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()


df = pd.ExcelFile(No_show_GR).parse('Sheet1')
SEVISID = df['SEVIS ID'].tolist()

df = pd.ExcelFile(No_show_GR).parse('Sheet1')
campusID = df['Campus Id'].tolist()


df = pd.ExcelFile(No_show_GR).parse('Sheet1')
banner_status = df['05 Banner Student Status'].tolist()

df = pd.ExcelFile(No_show_GR).parse('Sheet1')
cr_hours = df['07 Total Credit Hours'].tolist()

df = pd.ExcelFile(No_show_GR).parse('Sheet1')
check_in_status = df['14 CHECK IN I94 or Entry Stamp'].tolist()


Cancel_SEVISID_banner = dict(zip(SEVISID, banner_status))

Cancel_SEVISID_credits = dict(zip(SEVISID, cr_hours))

Cancel_SEVISID_SV = dict(zip(SEVISID, check_in_status))


