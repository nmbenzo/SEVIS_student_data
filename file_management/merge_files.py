import pandas as pd
from Handlers.file_imports import *

def merge_all_workbooks():
    transfer_student_data = pd.read_excel(current_transfer_data, sheet_name=1, index_col=0)
    df1 = pd.DataFrame(transfer_student_data)

    new_student_data = pd.read_excel(sevis_inital_student_data, sheet_name=0, index_col=0)
    df2 = pd.DataFrame(new_student_data)


    active_student_data = pd.read_excel(active_student_req_reg, sheet_name=4, index_col=0)
    df3 = pd.DataFrame(active_student_data)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(Registration_file, engine='xlsxwriter', date_format='mmmm dd yyyy')

    workbook  = writer.book

    df1.to_excel(writer, sheet_name='Transfer Students')
    df2.to_excel(writer, sheet_name='New Students')
    df3.to_excel(writer, sheet_name='Active Students')

    writer.save()
