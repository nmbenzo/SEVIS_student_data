from openpyxl.styles import NamedStyle, Font, Border, Side
import openpyxl


file2 = '/Users/nbenzschawel/Desktop/stupid_test.xlsx'

wb2 = openpyxl.load_workbook(file2)
new_sheet = wb2.worksheets[1]


highlight = NamedStyle(name='highlight')
highlight.font = Font(bold=True)
bd = Side(style='thin')
highlight.border = Border(left=bd, top=bd, right=bd, bottom=bd)

wb2.add_named_style(highlight)
