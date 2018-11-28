import openpyxl
from SEVIS_Transfers.build_new_student_data import file1, file2, wb, wb2, old_sheet, new_sheet, max_row, max_col


def copyRange(startCol, startRow, endCol, endRow, old_sheet):
    """
    Copies a range of cells as a nested list
    Takes: start cell, end cell, and the sheet we want to copy from
    """
    rangeSelected = []
    for i in range(startRow, endRow+1, 1):
        rowSelected = []
        for j in range(startCol, endCol + 1, 1):
            rowSelected.append(old_sheet.cell(row = i, column = j).value)
        rangeSelected.append(rowSelected)

    return rangeSelected


def pasteRange(startCol, startRow, endCol, endRow, sheetReceiving, copiedData):
    countRow = 0
    for i in range(startRow, endRow+1, 1):
        countCol = 0
        for j in range(startCol, endCol+1, 1):
            sheetReceiving.cell(row=i, column=j).value = copiedData[countRow][countCol]
            countCol += 1
        countRow += 1


def createData():
    print('Processing data...')
    selectedRange = copyRange(1, 1, max_col, max_row, old_sheet)
    pastingRange = pasteRange(1, 1, max_col, max_row, new_sheet, selectedRange)

    wb2.save(file2)
    print("Range copied and pasted")


createData()



