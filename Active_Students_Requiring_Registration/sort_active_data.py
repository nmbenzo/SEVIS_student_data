import pandas as pd
from Handlers.file_imports import ACTIVE_students_FINAL, ACTIVE_students


# def sort_active_data():
#     active_data = pd.read_excel(ACTIVE_students_FINAL, sheet_name=0, index_col=0)
#     sorted_by_advisor = active_data.sort_values(['Advisor'], ascending=True)
#
#     writer = pd.ExcelWriter(ACTIVE_students_FINAL, engine='openpyxl')
#     writer.book = ACTIVE_students
#     writer.sheets = dict((ws.title, ws) for ws in ACTIVE_students.worksheets)
#
#     sorted_by_advisor.to_excel(writer, 'Sheet')
#     writer.save()
#     print('Data sorted by Advisor')