import os
os.getcwd()
from Handlers.file_imports import completed_student_wb2, comp_sheet, comp_student_cleanup_report
from Compeleted_Student_Cleaning.build_comp_data import SEVISID_completed


def match_SEVISID_completed(SEVISID_completed):
    """
    match the SEVISID from the SEVIS spreadsheet of completed students with the
    SEVISID from ACTIVE status students report out of Atlas. If there is an ID
    match, populate new column with notes to close.
    """
    comp_sheet.insert_cols(1)
    title = comp_sheet.cell(row=1, column=1)
    title.value = 'Completed Notes'
    for row in range(2, comp_sheet.max_row):
        sevis_ID = comp_sheet.cell(row=row, column=3).value
        for x in SEVISID_completed:
            if x == sevis_ID:
                comp_sheet.cell(row=row, column=1).value = 'Student is COMPLETED in SEVIS, but ACTIVE in ISSM.'

    completed_student_wb2.save(comp_student_cleanup_report)


