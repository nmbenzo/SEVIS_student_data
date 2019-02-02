import time
from tqdm import trange
"""File to extract the copier functions for workbooks"""

def copy_new_Range(startCol, startRow, endCol, endRow, sheet):
    """
    Copies a range of cells as a nested list
    Takes: start cell, end cell, and the sheet we want to copy from
    """
    rangeSelected = []
    for i in range(startRow, endRow + 1, 1):
        rowSelected = []
        for j in range(startCol, endCol + 1, 1):
            rowSelected.append(sheet.cell(row=i, column=j).value)
        rangeSelected.append(rowSelected)

    return rangeSelected


def paste_new_Range(startCol, startRow, endCol, endRow, sheetReceiving, copiedData):
    """Pastes the selected data from copy_new_Range to your desired output worksheet"""
    countRow = 0
    for i in trange(startRow, endRow + 1, 1):
        time.sleep(0.01)
        countCol = 0
        for j in range(startCol, endCol + 1, 1):
            sheetReceiving.cell(row=i, column=j).value = copiedData[countRow][countCol]
            countCol += 1
        countRow += 1