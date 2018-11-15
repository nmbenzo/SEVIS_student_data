import pandas as pd


def newstudent_excel_to_csv():
    data_xls = pd.read_excel('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx', 'Sheet1', index_col=None)
    data_xls.to_csv('new_student.csv', encoding='utf-8')


def activestud_excel_to_cvs():
    data_xls = pd.read_excel('', 'Sheet1', index_col=None)
    data_xls.to_csv('contstud.csv', encoding='utf-8')


def completedstud_excel_to_cvs():
    data_xls = pd.read_excel('', 'Sheet1', index_col=None)
    data_xls.to_csv('completedstud.csv', encoding='utf-8')


def gradstud_excel_to_cvs():
    data_xls = pd.read_excel('', 'Sheet1', index_col=None)
    data_xls.to_csv('graduatedstud.csv', encoding='utf-8')
