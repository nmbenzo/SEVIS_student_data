from Handlers.file_imports import SEVIS_initial_status_stud, No_show_UG, No_show_GR, \
    SEV_initial_data, wb_cancel_ug,  ug_sheet, gr_sheet, ug_row_max, \
    gr_row_max, gr_col_max

def copy_new_Range(startCol, startRow, endCol, endRow, gr_sheet):
    """
    Copies a range of cells as a nested list
    Takes: start cell, end cell, and the sheet we want to copy from
    """
    rangeSelected = []
    for i in range(startRow, endRow + 1, 1):
        rowSelected = []
        for j in range(startCol, endCol + 1, 1):
            rowSelected.append(gr_sheet.cell(row=i, column=j).value)
        rangeSelected.append(rowSelected)

    return rangeSelected


def paste_new_Range(startCol, startRow, endCol, endRow, sheetReceiving, copiedData):
    """Pastes the selected data from copy_new_Range to your desired output worksheet"""
    countRow = 0
    for i in range(startRow, endRow + 1, 1):
        countCol = 0
        for j in range(startCol, endCol + 1, 1):
            sheetReceiving.cell(row=i, column=j).value = copiedData[countRow][countCol]
            countCol += 1
        countRow += 1


def create_new_Data():
    """Pastes copied range to new sheet which needs to be updated"""
    print('Processing data...')
    print(f'Data copied: current range = {ug_row_max}')

    if ug_sheet.cell(row=1, column=1).value == 'Passport Last Name':
        selectedRange = copy_new_Range(1, 2, gr_col_max, gr_row_max, gr_sheet)
        paste_new_Range(1, (ug_row_max+1), gr_col_max, (ug_row_max + gr_row_max-1), ug_sheet, selectedRange)

    wb_cancel_ug.save(No_show_UG)
    print('Graduate Cancel range copied and pasted')
    print(f'New Row Range = {ug_sheet.max_row}')
