import pandas as pd
from Handlers.file_imports import NEW_students_FINAL, NEW_students


def sort_data():
    new_data = pd.read_excel(NEW_students_FINAL, sheet_name=0, index_col=0)
    sorted_by_advisor = new_data.sort_values(['Advisor'], ascending=True)

    writer = pd.ExcelWriter(NEW_students_FINAL, engine='openpyxl')
    writer.book = NEW_students
    writer.sheets = dict((ws.title, ws) for ws in NEW_students.worksheets)

    sorted_by_advisor.to_excel(writer, 'Sheet', index=False)
    writer.save()
    print('Data sorted by Advisor')