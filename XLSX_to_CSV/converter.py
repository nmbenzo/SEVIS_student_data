import pandas as pd


def newstudent_excel_to_csv():
    data_xls = pd.read_excel('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx', 'Sheet1', index_col=None)
    data_xls.to_csv('new_student.csv', encoding='utf-8')

newstudent_excel_to_csv()