import pandas as pd
from Handlers.file_imports import current_transfer_data, wb2_trans


def sort_data():
    current_data = pd.read_excel(current_transfer_data, sheet_name=1, index_col=0)
    sorted_by_sevisid = current_data.sort_values(['SEVIS ID', 'Student Status'], ascending=True)

    writer = pd.ExcelWriter(current_transfer_data, engine='openpyxl')
    writer.book = wb2_trans
    writer.sheets = dict((ws.title, ws) for ws in wb2_trans.worksheets)

    sorted_by_sevisid.to_excel(writer, 'Sheet2')
    writer.save()
    print('\nData sorted by SEVIS ID')


def remove_duplicates():
    current_data = pd.read_excel(current_transfer_data, sheet_name=2)
    df = pd.DataFrame(current_data)
    dropped_data = df.drop_duplicates(subset=['SEVIS ID', 'Student Status'], keep='last')

    writer = pd.ExcelWriter(current_transfer_data, engine='openpyxl')
    writer.book = wb2_trans
    writer.sheets = dict((ws.title, ws) for ws in wb2_trans.worksheets)

    dropped_data.to_excel(writer, 'Sheet3')
    writer.save()
    print('Removed duplicate values')

