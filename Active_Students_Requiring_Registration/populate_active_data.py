import os
os.getcwd()
import time
from Handlers.file_imports import ws2, sheet, ACTIVE_students_FINAL, ACTIVE_students, \
ACTIVE_students_sheet
from File_Management.copier import copy_new_Range, paste_new_Range
from tqdm import trange


def create_active_Student_Data():
    """Pastes copied range to new sheet which needs to be updated"""
    print(f'\nCurrent Row Range = {ACTIVE_students_sheet.max_row}')
    time.sleep(0.5)
    print('Processing data...')

    if ACTIVE_students_sheet.cell(row=1, column=1).value is None:
        selectedRange = copy_new_Range(1, 1, sheet.max_column, sheet.max_row, ws2)
        paste_new_Range(1, 1, sheet.max_column, sheet.max_row, ACTIVE_students_sheet, selectedRange)

    ACTIVE_students.save(ACTIVE_students_FINAL)
    time.sleep(0.5)
    print(f'Data copied: Current Range = {ACTIVE_students_sheet.max_row}')


def active_match_SEVISID(active_campusID_SEVISID):
    """
    match_SEVISID compares SEVISIDs from two separate workbooks(ws, ws2) 
    and then populates a blank column with the appropriate BannerID(campusID)
    """
    ACTIVE_students_sheet.insert_cols(1)
    title = ACTIVE_students_sheet.cell(row=1, column=1)
    title.value = 'campusID'
    for rowNum in range(2, ACTIVE_students_sheet.max_row):
        sevis_ID = ACTIVE_students_sheet.cell(row=rowNum, column=2).value
        for x in active_campusID_SEVISID:
            if x == sevis_ID:
                ACTIVE_students_sheet.cell(row=rowNum, column=1).value = active_campusID_SEVISID[sevis_ID]

    ACTIVE_students.save(ACTIVE_students_FINAL)


def match_units(active_SEVISID_units):
    """
    match_units compares SEVISIDs against unit data and then populates
    a blank column with the appropriate unit data when a SEVISID match is found.
    """
    ACTIVE_students_sheet.insert_cols(1)
    title = ACTIVE_students_sheet.cell(row=1, column=1)
    title.value = 'Unit Registration'
    for rowNum in range(2, ACTIVE_students_sheet.max_row):
        sevis_ID = ACTIVE_students_sheet.cell(row=rowNum, column=3).value
        for x in active_SEVISID_units:
            if x == sevis_ID:
                ACTIVE_students_sheet.cell(row=rowNum, column=1).value = active_SEVISID_units[sevis_ID]

    ACTIVE_students.save(ACTIVE_students_FINAL)


def match_major_data(active_SEVISID_major):
    """
    match_major_data compares SEVISIDs against major data and then populates
    a blank column with the appropriate major data when a SEVISID match is found.
    """
    ACTIVE_students_sheet.insert_cols(1)
    title = ACTIVE_students_sheet.cell(row=1, column=1)
    title.value = 'Major'
    for rowNum in range(2, ACTIVE_students_sheet.max_row):
        sevis_ID = ACTIVE_students_sheet.cell(row=rowNum, column=4).value
        for x in active_SEVISID_major:
            if x == sevis_ID:
                ACTIVE_students_sheet.cell(row=rowNum, column=1).value = active_SEVISID_major[sevis_ID]

    ACTIVE_students.save(ACTIVE_students_FINAL)


def match_advisor(advisor_major_ug, advisor_major_gr):
    """
    match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module: data
    """
    ACTIVE_students_sheet.insert_cols(1)
    title = ACTIVE_students_sheet.cell(row=1, column=1)
    title.value = 'Advisor'
    for rowNum in trange(2, ACTIVE_students_sheet.max_row):
        major = ACTIVE_students_sheet.cell(row=rowNum, column=2).value
        if major in advisor_major_ug:
            ACTIVE_students_sheet.cell(row=rowNum, column=1).value = advisor_major_ug[major]
        if major in advisor_major_gr:
            ACTIVE_students_sheet.cell(row=rowNum, column=1).value = advisor_major_gr[major]

    ACTIVE_students.save(ACTIVE_students_FINAL)


def add_graduated_student_emails(sevisID_emails):
    """
    This function populates a student's OPT Type from the sevis_opt_report
    to the graduated student list by matching it with a campusID
    from active_stud_issm_data
    """
    ACTIVE_students_sheet.insert_cols(1)
    title = ACTIVE_students_sheet.cell(row=1, column=1)
    title.value = 'Emails'
    for rowNum in range(2, ACTIVE_students_sheet.max_row):
        sevisID = ACTIVE_students_sheet.cell(row=rowNum, column=7).value
        for x in sevisID_emails:
            if x == sevisID:
                ACTIVE_students_sheet.cell(row=rowNum, column=1).value = sevisID_emails[x]

    ACTIVE_students.save(ACTIVE_students_FINAL)


def add_notes_column():
    ACTIVE_students_sheet.insert_cols(1)
    title1 = ACTIVE_students_sheet.cell(row=1, column=1)
    title1.value = 'Notes'
    ACTIVE_students.save(ACTIVE_students_FINAL)


def add_registration_status_column():
    ACTIVE_students_sheet.insert_cols(1)
    title1 = ACTIVE_students_sheet.cell(row=1, column=1)
    title1.value = 'Registration Status'
    ACTIVE_students.save(ACTIVE_students_FINAL)


def add_graduation_status_column():
    ACTIVE_students_sheet.insert_cols(1)
    title1 = ACTIVE_students_sheet.cell(row=1, column=1)
    title1.value = 'Graduation Status'
    ACTIVE_students.save(ACTIVE_students_FINAL)
