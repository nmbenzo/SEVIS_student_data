import pandas as pd
from SEVIS_Transfers.build_new_student_data import file2, wb2


def sort_data():
    current_data = pd.read_excel(file2, sheet_name=1, index_col=0)
    sorted_by_sevisid = current_data.sort_values(['SEVIS ID', 'Student Status'], ascending=True)

    writer = pd.ExcelWriter(file2, engine='openpyxl')
    writer.book = wb2
    writer.sheets = dict((ws.title, ws) for ws in wb2.worksheets)

    sorted_by_sevisid.to_excel(writer, 'Sheet2')
    writer.save()
    print('Data sorted by SEVIS ID')


def remove_duplicates():
    current_data = pd.read_excel(file2, sheet_name=2)
    df = pd.DataFrame(current_data)
    dropped_data = df.drop_duplicates(subset=['SEVIS ID', 'Student Status'], keep='last')

    writer = pd.ExcelWriter(file2, engine='openpyxl')
    writer.book = wb2
    writer.sheets = dict((ws.title, ws) for ws in wb2.worksheets)

    dropped_data.to_excel(writer, 'Sheet3')
    writer.save()
    print('Removed duplicate values')

