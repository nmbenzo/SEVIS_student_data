import time
from Handlers.file_imports import No_show_UG, wb_cancel_ug,  ug_sheet, gr_sheet, ug_row_max, \
    gr_row_max, gr_col_max, sevis_initial, No_SHOW_students_FINAL, NO_SHOW_students, NOSHOW_students_sheet
from File_Management.copier import copy_new_Range, paste_new_Range
from tqdm import trange


def create_new_Cancel_Data():
    """Pastes copied range to new sheet which needs to be updated"""
    if ug_sheet.cell(row=1, column=1).value == 'Passport Last Name':
        selectedRange = copy_new_Range(1, 2, gr_col_max, gr_row_max, gr_sheet)
        paste_new_Range(1, (ug_row_max+1), gr_col_max, (ug_row_max + gr_row_max-1), ug_sheet, selectedRange)

    wb_cancel_ug.save(No_show_UG)


def create_NoShow_Student_Data():
    """Pastes copied range to new sheet which needs to be updated"""
    print(f'\nInitial No Show Student Data Range = {NOSHOW_students_sheet.max_row}')
    print('Processing data...')
    time.sleep(1)
    if NOSHOW_students_sheet.cell(row=1, column=1).value is None:
        selectedRange = copy_new_Range(1, 1, sevis_initial.max_column, sevis_initial.max_row, sevis_initial)
        paste_new_Range(1, 1, sevis_initial.max_column, sevis_initial.max_row, NOSHOW_students_sheet, selectedRange)

    NO_SHOW_students.save(No_SHOW_students_FINAL)
    print(f'Data copied: Current No Show Student Range = {NOSHOW_students_sheet.max_row}')
    time.sleep(2.5)


def build_apdc_notes(Cancel_APDC):
    """Adds APDC codes to the SEVIS Initial Status spreadsheet"""
    NOSHOW_students_sheet.insert_cols(1)
    title = NOSHOW_students_sheet.cell(row=1, column=1)
    title.value = 'APDC Code'
    for rowNum in range(2, NOSHOW_students_sheet.max_row):
        sevisID = NOSHOW_students_sheet.cell(row=rowNum, column=2).value
        for x in Cancel_APDC:
            if x == sevisID:
                NOSHOW_students_sheet.cell(row=rowNum, column=1).value = Cancel_APDC[sevisID]

    NO_SHOW_students.save(No_SHOW_students_FINAL)


def build_level_data(Cancel_Level):
    """Adds education level to the SEVIS Initial Status spreadsheet"""
    NOSHOW_students_sheet.insert_cols(1)
    title = NOSHOW_students_sheet.cell(row=1, column=1)
    title.value = 'Level of Education'
    for rowNum in range(2, NOSHOW_students_sheet.max_row):
        sevisID = NOSHOW_students_sheet.cell(row=rowNum, column=3).value
        for x in Cancel_Level:
            if x == sevisID:
                NOSHOW_students_sheet.cell(row=rowNum, column=1).value = Cancel_Level[sevisID]


def build_cancel_campusID(Cancel_SEVISID_CampusID):
    """Adds campus IDs to the SEVIS Initial Status spreadsheet """
    NOSHOW_students_sheet.insert_cols(1)
    title = NOSHOW_students_sheet.cell(row=1, column=1)
    title.value = 'CampusID'
    for rowNum in range(2, NOSHOW_students_sheet.max_row):
        sevisid = NOSHOW_students_sheet.cell(row=rowNum, column=4).value
        for x in Cancel_SEVISID_CampusID:
            if x == sevisid:
                NOSHOW_students_sheet.cell(row=rowNum, column=1).value = Cancel_SEVISID_CampusID[sevisid]

    NO_SHOW_students.save(No_SHOW_students_FINAL)



def build_cancel_notes(Cancel_SEVISID_banner, Cancel_SEVISID_credits, Cancel_SEVISID_SV):
    """ Builds a brief set of note for each record displaying """
    NOSHOW_students_sheet.insert_cols(1)
    title = NOSHOW_students_sheet.cell(row=1, column=1)
    title.value = 'Cancellation Notes'
    for rowNum in trange(2, NOSHOW_students_sheet.max_row):
        sevisid = NOSHOW_students_sheet.cell(row=rowNum, column=5).value
        for x in Cancel_SEVISID_banner, Cancel_SEVISID_credits, Cancel_SEVISID_SV:
            for i in Cancel_SEVISID_credits:
                for j in Cancel_SEVISID_SV:
                    if x and i and j == sevisid:
                        if Cancel_SEVISID_SV[sevisid] != 'Yes':
                            NOSHOW_students_sheet.cell(row=rowNum,column=1).value = 'SV Status: Not checked in' \
                            + ', Registered Units: ' + str(Cancel_SEVISID_credits[sevisid]) \
                            + ' credits, ' + 'Banner Status: ' + str(Cancel_SEVISID_banner[sevisid])
                        else:
                            NOSHOW_students_sheet.cell(row=rowNum, column=1).value = \
                                'SV Status: ' + str(Cancel_SEVISID_SV[sevisid]) + ', Registered Units: ' \
                                + str(Cancel_SEVISID_credits[sevisid]) + ' credits, ' \
                                + 'Banner Status: ' + str(Cancel_SEVISID_banner[sevisid])

    NO_SHOW_students.save(No_SHOW_students_FINAL)
