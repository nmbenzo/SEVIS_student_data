import openpyxl


file1 = '/Users/nbenzschawel/Desktop/New_sevis_data_test.xlsx'
file2 = '/Users/nbenzschawel/Desktop/stupid_test.xlsx'

wb = openpyxl.load_workbook(file1)
wb2 = openpyxl.load_workbook(file2)
old_sheet = wb.worksheets[0]
new_sheet = wb2.worksheets[1]

max_row = old_sheet.max_row
max_col = old_sheet.max_column

