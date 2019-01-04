import pandas as pd
from Handlers.file_imports import *


def merge_all_workbooks():
    transfer_student_data = pd.read_excel(current_transfer_data, sheet_name=0, index_col=0)
    df1 = pd.DataFrame(transfer_student_data)

    new_student_data = pd.read_excel(sevis_inital_student_data, sheet_name=0, index_col=0)
    df2 = pd.DataFrame(new_student_data)


    active_student_data = pd.read_excel(active_student_req_reg, sheet_name=4, index_col=0)
    df3 = pd.DataFrame(active_student_data)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(Registration_file, engine='xlsxwriter', date_format='mmm d yyyy')

    df1.to_excel(writer, sheet_name='Transfer Students')
    df2.to_excel(writer, sheet_name='New Students')
    df3.to_excel(writer, sheet_name='Active Students')

    workbook = writer.book

    worksheet1 = writer.sheets['Transfer Students']
    worksheet2 = writer.sheets['New Students']
    worksheet3 = writer.sheets['Active Students']

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': False,
        'align': 'center',
        'border': 0})

    column_format = workbook.add_format({
        'bold': False,
        'text_wrap': True,
        'align': 'center',
        'valign': 'middle',
        'border': 0})

    # Write the column headers with the defined format.
    for col_num, value in enumerate(df1.columns.values):
        worksheet1.write(0, col_num + 1, value, header_format)

    for col_num, value in enumerate(df2.columns.values):
        worksheet2.write(0, col_num + 1, value, header_format)

    for col_num, value in enumerate(df3.columns.values):
        worksheet3.write(0, col_num + 1, value, header_format)

    #Format columns of Transfer Students
    worksheet1.set_column('A:A', 15, column_format)
    worksheet1.set_column('B:C', 18, column_format)
    worksheet1.set_column('D:E', 15, column_format)
    worksheet1.set_column('F:F', 35, column_format)
    worksheet1.set_column('G:G', 17, column_format)
    worksheet1.set_column('H:J', 13, column_format)

    # Format columns of New Students
    worksheet2.set_column('A:A', 40, column_format)
    worksheet2.set_column('C:C', 25, column_format)
    worksheet2.set_column('D:D', 10, column_format)
    worksheet2.set_column('E:G', 16, column_format)
    worksheet2.set_column('H:H', 22, column_format)
    worksheet2.set_column('I:J', 17, column_format)
    worksheet2.set_column('K:K', 25, column_format)

    # Format columns of Active Students
    worksheet3.set_column('A:A', 10, column_format)
    worksheet3.set_column('B:B', 25, column_format)
    worksheet3.set_column('C:C', 15, column_format)
    worksheet3.set_column('D:D', 10, column_format)
    worksheet3.set_column('E:E', 13, column_format)
    worksheet3.set_column('F:F', 16, column_format)
    worksheet3.set_column('G:J', 21, column_format)

    writer.save()
