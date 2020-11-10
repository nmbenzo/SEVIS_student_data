import os
os.getcwd()
import pandas as pd
try:
    from Handlers.file_imports import active_stud_issm_data_F19
except:
    pass

try:
    df = pd.ExcelFile(active_stud_issm_data_F19).parse\
        ('All_SEVIS-Active_Student_Tracki')
    SEVISID = df['SEVIS ID'].tolist()

    df = pd.ExcelFile(active_stud_issm_data_F19).parse\
        ('All_SEVIS-Active_Student_Tracki')
    campusID = df['Campus Id'].tolist()

    df = pd.ExcelFile(active_stud_issm_data_F19).parse\
        ('All_SEVIS-Active_Student_Tracki')
    major_data = df['Major Field (display)'].tolist()

    df = pd.ExcelFile(active_stud_issm_data_F19).parse\
        ('All_SEVIS-Active_Student_Tracki')
    units = df['07 Total Credit Hours'].tolist()

    df = pd.ExcelFile(active_stud_issm_data_F19).parse\
        ('All_SEVIS-Active_Student_Tracki')
    emails = df['E-mail Address'].tolist()

    df = pd.ExcelFile(active_stud_issm_data_F19).parse\
        ('All_SEVIS-Active_Student_Tracki')
    term = df['03 Student Status Term'].tolist()


    # build dict where k = SEVISID, v = campusID
    active_campusID_SEVISID = dict(zip(SEVISID, campusID))

    # build a dict where k = SEVISID, v = list of majors
    active_SEVISID_major = dict(zip(SEVISID, major_data))

    active_SEVISID_units = dict(zip(SEVISID, units))

    sevisID_emails = dict(zip(SEVISID, emails))

    SEVISID_term = dict(zip(SEVISID, term))
except:
    print('Files no longer available.')
    pass
