import time
import pandas as pd
from tqdm import trange
from Handlers.file_imports import *


def merge_all_workbooks():
    """
    Merges specified Workbooks and then applies minimal formatting using Pandas
    DataFrames
    """
    for i in trange(100):
        time.sleep(0.1)

    COL_student_data = pd.read_excel(COL_students_raw, sheet_name=0, index_col=0)
    df1 = pd.DataFrame(COL_student_data)

    transfer_student_data = pd.read_excel(current_transfer_data, sheet_name=0, index_col=0)
    df2 = pd.DataFrame(transfer_student_data)

    new_student_data = pd.read_excel(NEW_students_FINAL, sheet_name=0, index_col=0)
    df3 = pd.DataFrame(new_student_data)

    active_student_data = pd.read_excel(ACTIVE_students_FINAL, sheet_name=0, index_col=0)
    df4 = pd.DataFrame(active_student_data)

    cancel_students = pd.read_excel(No_SHOW_students_FINAL, sheet_name=0, index_col=0)
    df5 = pd.DataFrame(cancel_students)

    J1_students = pd.read_excel(J_students_FINAL, sheet_name=0, index_col=0)
    df6 = pd.DataFrame(J1_students)


    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(Registration_file, engine='xlsxwriter', date_format='mmm d yyyy')

    # need to write a function that returns a boolean if COL doesn't need to be
    # uploaded for some reason. Split the merge_all_workbooks() into multiple
    # functions. Remember each function should only have one purpose.
    df1.to_excel(writer, sheet_name='COL Students')
    df2.to_excel(writer, sheet_name='Transfer Students')
    df3.to_excel(writer, sheet_name='New Students')
    df4.to_excel(writer, sheet_name='Active Students')
    df5.to_excel(writer, sheet_name='Cancellations')
    df6.to_excel(writer, sheet_name='J-1 Students')

    workbook = writer.book

    worksheet1 = writer.sheets['COL Students']
    worksheet2 = writer.sheets['Transfer Students']
    worksheet3 = writer.sheets['New Students']
    worksheet4 = writer.sheets['Active Students']
    worksheet5 = writer.sheets['Cancellations']
    worksheet6 = writer.sheets['J-1 Students']


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

    for col_num, value in enumerate(df4.columns.values):
        worksheet4.write(0, col_num + 1, value, header_format)

    for col_num, value in enumerate(df5.columns.values):
        worksheet5.write(0, col_num + 1, value, header_format)

    for col_num, value in enumerate(df6.columns.values):
        worksheet6.write(0, col_num + 1, value, header_format)


    #Format columns of COL Students
    worksheet1.set_column('A:X', 16, column_format)

    #Format columns of Transfer Students
    worksheet2.set_column('A:A', 15, column_format)
    worksheet2.set_column('B:C', 18, column_format)
    worksheet2.set_column('D:E', 15, column_format)
    worksheet2.set_column('F:F', 35, column_format)
    worksheet2.set_column('G:G', 17, column_format)
    worksheet2.set_column('H:J', 13, column_format)

    # Format columns of New Students
    worksheet3.set_column('A:A', 48, column_format)
    worksheet3.set_column('C:C', 25, column_format)
    worksheet3.set_column('D:D', 10, column_format)
    worksheet3.set_column('E:G', 16, column_format)
    worksheet3.set_column('H:H', 22, column_format)
    worksheet3.set_column('I:J', 17, column_format)
    worksheet3.set_column('K:K', 25, column_format)

    # Format columns of Active Students
    worksheet4.set_column('A:A', 10, column_format)
    worksheet4.set_column('B:B', 25, column_format)
    worksheet4.set_column('C:C', 15, column_format)
    worksheet4.set_column('D:D', 10, column_format)
    worksheet4.set_column('E:E', 13, column_format)
    worksheet4.set_column('F:F', 16, column_format)
    worksheet4.set_column('G:J', 21, column_format)

    worksheet5.set_column('A:A', 64, column_format)
    worksheet5.set_column('B:B', 11, column_format)
    worksheet5.set_column('C:D', 15, column_format)
    worksheet5.set_column('E:E', 20, column_format)
    worksheet5.set_column('F:H', 16, column_format)
    worksheet5.set_column('I:I', 35, column_format)

    worksheet6.set_column('A:AL', 16, column_format)

    writer.save()


def final_merge_all_workbooks():
    """
    Merges final specified Workbooks from the SEVIS registration file in use
    and then applies minimal formatting using Panda DataFrames
    """
    for i in trange(100):
        time.sleep(0.1)

    COL_student_data = pd.read_excel(SEVIS_Live_Workbook, sheet_name=0, index_col=0)
    df1 = pd.DataFrame(COL_student_data)

    transfer_student_data = pd.read_excel(SEVIS_Live_Workbook, sheet_name=1, index_col=0)
    df2 = pd.DataFrame(transfer_student_data)

    new_student_data = pd.read_excel(SEVIS_Live_Workbook, sheet_name=2, index_col=0)
    df3 = pd.DataFrame(new_student_data)

    active_student_data = pd.read_excel(ACTIVE_students_FINAL, sheet_name=0, index_col=0)
    df4 = pd.DataFrame(active_student_data)

    cancel_students = pd.read_excel(SEVIS_Live_Workbook, sheet_name=4, index_col=0)
    df5 = pd.DataFrame(cancel_students)

    J1_students = pd.read_excel(J_students_FINAL, sheet_name=0, index_col=0)
    df6 = pd.DataFrame(J1_students)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(Registration_file, engine='xlsxwriter',
                            date_format='mmm d yyyy')

    # need to write a function that returns a boolean if COL doesn't need to be
    # uploaded for some reason. Split the merge_all_workbooks() into multiple
    # functions. Remember each function should only have one purpose.
    df1.to_excel(writer, sheet_name='COL Students')
    df2.to_excel(writer, sheet_name='Transfer Students')
    df3.to_excel(writer, sheet_name='New Students')
    df4.to_excel(writer, sheet_name='Active Students')
    df5.to_excel(writer, sheet_name='Cancellations')
    df6.to_excel(writer, sheet_name='J-1 Students')

    workbook = writer.book

    worksheet1 = writer.sheets['COL Students']
    worksheet2 = writer.sheets['Transfer Students']
    worksheet3 = writer.sheets['New Students']
    worksheet4 = writer.sheets['Active Students']
    worksheet5 = writer.sheets['Cancellations']
    worksheet6 = writer.sheets['J-1 Students']

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

    for col_num, value in enumerate(df4.columns.values):
        worksheet4.write(0, col_num + 1, value, header_format)

    for col_num, value in enumerate(df5.columns.values):
        worksheet5.write(0, col_num + 1, value, header_format)

    for col_num, value in enumerate(df6.columns.values):
        worksheet6.write(0, col_num + 1, value, header_format)

    # Format columns of COL Students
    worksheet1.set_column('A:X', 16, column_format)

    # Format columns of Transfer Students
    worksheet2.set_column('A:A', 20, column_format)
    worksheet2.set_column('B:C', 18, column_format)
    worksheet2.set_column('D:E', 18, column_format)
    worksheet2.set_column('F:F', 25, column_format)
    worksheet2.set_column('G:H', 17, column_format)
    worksheet2.set_column('I:I', 35, column_format)
    worksheet2.set_column('J:M', 18, column_format)

    # Format columns of New Students
    worksheet3.set_column('A:A', 24, column_format)
    worksheet3.set_column('B:B', 48, column_format)
    worksheet3.set_column('C:D', 25, column_format)
    worksheet3.set_column('E:G', 16, column_format)
    worksheet3.set_column('H:H', 22, column_format)
    worksheet3.set_column('I:J', 17, column_format)
    worksheet3.set_column('K:K', 25, column_format)

    # Format columns of Active Students
    worksheet4.set_column('A:A', 10, column_format)
    worksheet4.set_column('B:B', 25, column_format)
    worksheet4.set_column('C:C', 15, column_format)
    worksheet4.set_column('D:D', 10, column_format)
    worksheet4.set_column('E:E', 13, column_format)
    worksheet4.set_column('F:F', 16, column_format)
    worksheet4.set_column('G:J', 21, column_format)

    worksheet5.set_column('A:A', 64, column_format)
    worksheet5.set_column('B:B', 11, column_format)
    worksheet5.set_column('C:D', 15, column_format)
    worksheet5.set_column('E:E', 20, column_format)
    worksheet5.set_column('F:H', 16, column_format)
    worksheet5.set_column('I:I', 35, column_format)

    worksheet6.set_column('A:AL', 16, column_format)

    writer.save()
