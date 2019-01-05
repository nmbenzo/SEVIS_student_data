import os
os.getcwd()
import pandas as pd
from Handlers.file_imports import active_stud_issm_data

"""
This file builds dictionaries containing the following data: 
campusIDs : SEVISIDs
campusIDs : Work Authorization Types
campusIDs : Work Authorization End Dates
campusIDs : Profile End Dates
campusIDs : Student Emails

"""

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
SEVISID = df['SEVIS ID'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
campusID = df['Campus Id'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
major_data = df['Major Field (display)'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
work_auth_type = df['F Work Authorization Type'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
work_auth_enddate = df['Work Auth End Date'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
profile_end_date = df['Profile End Date'].tolist()

df = pd.ExcelFile(active_stud_issm_data).parse('All_SEVIS-Active_Student_Tracki')
emails = df['E-mail Address'].tolist()


# Dictionary building
campusID_SEVISID = {}

for i in range(len(campusID)): # verbose dict building
    campusID_SEVISID[campusID[i]] = SEVISID[i]

campusID_work_auth = dict(zip(campusID, work_auth_type))

campusID_workend = dict(zip(campusID, work_auth_enddate))

campusID_end_date = dict(zip(campusID, profile_end_date))

campusID_emails = dict(zip(campusID, emails))





