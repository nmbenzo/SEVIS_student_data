import pandas as pd
from pandas import ExcelWriter
import openpyxl
import xlsxwriter


file2 = '/Users/nbenzschawel/Desktop/stupid_test.xlsx'
wb2 = openpyxl.load_workbook(file2)

new_sheet = wb2.worksheets[1]
final_sheet = wb2.worksheets[0]

current_data = pd.read_excel(file2, sheet_name=1, index_col=0)

sorted_by_sevisid = current_data.sort_values(['SEVIS ID'], ascending=True)

writer = pd.ExcelWriter(file2, engine='openpyxl')
writer.book = wb2
writer.sheets = dict((ws.title, ws) for ws in wb2.worksheets)

sorted_by_sevisid.to_excel(writer, 'Sheet2')
writer.save()




