import os
os.getcwd()
import time
from Handlers.file_imports import ws2_new, NEW_students_FINAL, NEW_students, NEW_students_sheet
from File_Management.copier import copy_new_Range, paste_new_Range


def create_new_Student_Data():
    """Pastes copied range to new sheet which needs to be updated"""
    print('\nProcessing NEW Student data...')

    if NEW_students_sheet.cell(row=1, column=1).value is None:
        selectedRange = copy_new_Range(1, 1, ws2_new.max_column, ws2_new.max_row, ws2_new)
        paste_new_Range(1, 1, ws2_new.max_column, ws2_new.max_row, NEW_students_sheet, selectedRange)

    NEW_students.save(NEW_students_FINAL)
    time.sleep(0.5)
    print(f'Raw data copied: current range = {NEW_students_sheet.max_row}')


def new_match_SEVISID(campusID_SEVISID):
    """
    match_SEVISID compares SEVISIDs from two separate workbooks(ws, ws2)
    and then populates a blank column with the appropriate BannerID(campusID)
    """
    NEW_students_sheet.insert_cols(1)
    title = NEW_students_sheet.cell(row=1, column=1)
    title.value = 'campusID'
    for rowNum in range(2, NEW_students_sheet.max_row):
        sevis_ID = NEW_students_sheet.cell(row=rowNum, column=2).value
        for x in campusID_SEVISID:
            if x == sevis_ID:
                NEW_students_sheet.cell(row=rowNum, column=1).value = campusID_SEVISID[sevis_ID]

    NEW_students.save(NEW_students_FINAL)


def new_match_major_data(SEVISID_major):
    """match_major_data compares SEVISIDs against major data and then populates
    a blank column with the appropriate major data when a SEVISID match is found.
    """
    NEW_students_sheet.insert_cols(1)
    title = NEW_students_sheet.cell(row=1, column=1)
    title.value = 'Major'
    for rowNum in range(2, NEW_students_sheet.max_row):
        sevis_ID = NEW_students_sheet.cell(row=rowNum, column=3).value
        for x in SEVISID_major:
            if x == sevis_ID:
                NEW_students_sheet.cell(row=rowNum, column=1).value = SEVISID_major[sevis_ID]

    NEW_students.save(NEW_students_FINAL)


def new_match_advisor(advisor_major_ug, advisor_major_gr):
    """
    match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module: data
    """
    NEW_students_sheet.insert_cols(1)
    title = NEW_students_sheet.cell(row=1, column=1)
    title.value = 'Advisor'
    for rowNum in range(2, NEW_students_sheet.max_row):
        major = NEW_students_sheet.cell(row=rowNum, column=2).value
        if major in advisor_major_ug:
            NEW_students_sheet.cell(row=rowNum, column=1).value = advisor_major_ug[major]
        if major in advisor_major_gr:
            NEW_students_sheet.cell(row=rowNum, column=1).value = advisor_major_gr[major]

    NEW_students.save(NEW_students_FINAL)


def add_advisor_notes(SEVISID_checked_in, SEVISID_cr_hours):
    """
    add_advisor notes references the checked_in columns of workbook(ws)
    and then builds advisor notes based on which columns are populated
    """
    NEW_students_sheet.insert_cols(1)
    title = NEW_students_sheet.cell(row=1, column=1)
    title.value = 'Advisor Notes'
    for rowNum in range(2, NEW_students_sheet.max_row):
        sevis_ID = NEW_students_sheet.cell(row=rowNum, column=5).value
        for x in SEVISID_checked_in:
            for j in SEVISID_cr_hours:
                if x and j == sevis_ID:
                    if SEVISID_checked_in[sevis_ID] != 'Yes':
                        NEW_students_sheet.cell(row=rowNum, column=1).value = 'SV Status: Not checked in' + \
                        ', Registered Units: ' + str(SEVISID_cr_hours[sevis_ID]) + ' credits'
                    else:
                        NEW_students_sheet.cell(row=rowNum, column=1).value = 'SV Status: ' + str(SEVISID_checked_in[sevis_ID]) \
                    + ', Registered Units: ' + str(SEVISID_cr_hours[sevis_ID]) + ' credits'

    NEW_students.save(NEW_students_FINAL)
