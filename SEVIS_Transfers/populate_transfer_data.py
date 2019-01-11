import time
from Handlers.file_imports import current_transfer_data, \
    wb2_trans, old_sheet, new_sheet, row_max_old, col_max_old, final_sheet, \
    row_max_current, col_max_current, row_max_final, col_max_final
from File_Management.copier import copy_new_Range, paste_new_Range


def create_new_Data():
    """Pastes copied range to new sheet which needs to be updated"""
    print(f'Old Row Range = {new_sheet.max_row}')
    print('Processing data...')

    if new_sheet.cell(row=1, column=1).value is None:
        selectedRange = copy_new_Range(1, 1, col_max_old, row_max_old, old_sheet)
        paste_new_Range(1, 1, col_max_old, row_max_old, new_sheet, selectedRange)

    elif new_sheet.cell(row=1, column=1).value == 'SEVIS ID':
        selectedRange = copy_new_Range(1, 2, col_max_old, row_max_old, old_sheet)
        paste_new_Range(1, (row_max_current+1), col_max_old, (row_max_current + row_max_old-1),
                        new_sheet, selectedRange)

    wb2_trans.save(current_transfer_data)
    print('\nRange copied and pasted')
    print(f'New Row Range = {new_sheet.max_row}')


def check_in_fsa():
    """Marks new data that needs to be input into ISSM"""
    title = new_sheet.cell(row=1, column=10)
    title.value = 'ISSM Status'
    for rowNum in range(1, new_sheet.max_row):
        status = new_sheet.cell(row=rowNum, column=9).value
        if status == 'INITIAL':
            new_sheet.cell(row=rowNum, column=10).value = 'Add to ISSM'
    print('\nAdded notes for ISSM')

    wb2_trans.save(current_transfer_data)


def paste_to_final():
    """Pastes copied range from new sheet to final sheet - do this after sorting data"""
    print(f'Final Sheet Initial Row Range = {row_max_current}')
    print('Processing data...')
    wb2_trans.save(current_transfer_data)
    time.sleep(1.5)
    selectedRange = copy_new_Range(1, 1, new_sheet.max_column, new_sheet.max_row, new_sheet)
    paste_new_Range(1, 1, new_sheet.max_column, new_sheet.max_row, final_sheet, selectedRange)
    wb2_trans.save(current_transfer_data)
    print('\nRange copied and pasted')
    print(f'Final Sheet New Row Range = {final_sheet.max_row}')


def find_in_fsa():
    """Checks the status of final data to see if it is already in ISSM"""
    for rowNum in range(1, final_sheet.max_row):
        status = final_sheet.cell(row=rowNum, column=10).value
        if status == 'Add to ISSM':
            final_sheet.cell(row=rowNum, column=10).value = 'Old Data: in ISSM'
    print('\nUpdated ISSM notes for new data')

    wb2_trans.save(current_transfer_data)


def grab_final_data():
    """Copies old "Final" data into new_sheet to allow updated data comparison."""
    print(f'Current Row Range = {final_sheet.max_row}')
    print('Grabbing most recent data...')
    selectedRange = copy_new_Range(1, 1, col_max_final, row_max_final, final_sheet)
    paste_new_Range(1, 1, col_max_final, row_max_final, new_sheet, selectedRange)
    wb2_trans.save(current_transfer_data)
    print('Range copied and pasted')
    print(f'New Row Range = {new_sheet.max_row}')

