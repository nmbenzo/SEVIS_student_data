import os
os.getcwd()
from Handlers.file_imports import wb2_active, sheet


def active_match_SEVISID(active_campusID_SEVISID):
    """
    match_SEVISID compares SEVISIDs from two separate workbooks(ws, ws2) 
    and then populates a blank column with the appropriate BannerID(campusID)
    """
    sheet.insert_cols(1)
    title = sheet.cell(row=1, column=1)
    title.value = 'campusID'
    for rowNum in range(2, sheet.max_row):
        sevis_ID = sheet.cell(row=rowNum, column=2).value
        for x in active_campusID_SEVISID:
            if x == sevis_ID:
                sheet.cell(row=rowNum, column=1).value = active_campusID_SEVISID[sevis_ID]

    wb2_active.save('/Users/nbenzschawel/Downloads/Fall 201840 - Registration.xlsx')


def match_units(active_SEVISID_units):
    """match_units compares SEVISIDs against unit data and then populates
        a blank column with the appropriate unit data when a SEVISID match is found.
        """
    sheet.insert_cols(1)
    title = sheet.cell(row=1, column=1)
    title.value = 'Unit Registration'
    for rowNum in range(2, sheet.max_row):
        sevis_ID = sheet.cell(row=rowNum, column=3).value
        for x in active_SEVISID_units:
            if x == sevis_ID:
                sheet.cell(row=rowNum, column=1).value = active_SEVISID_units[sevis_ID]

    wb2_active.save('/Users/nbenzschawel/Downloads/Fall 201840 - Registration.xlsx')


def match_major_data(active_SEVISID_major):
    """match_major_data compares SEVISIDs against major data and then populates
    a blank column with the appropriate major data when a SEVISID match is found.
    """
    sheet.insert_cols(1)
    title = sheet.cell(row=1, column=1)
    title.value = 'Major'
    for rowNum in range(2, sheet.max_row):
        sevis_ID = sheet.cell(row=rowNum, column=4).value
        for x in active_SEVISID_major:
            if x == sevis_ID:
                sheet.cell(row=rowNum, column=1).value = active_SEVISID_major[
                    sevis_ID]

    wb2_active.save('/Users/nbenzschawel/Downloads/Fall 201840 - Registration.xlsx')


def match_advisor(advisor_major_ug, advisor_major_gr):
    """
    match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module: data
    """
    sheet.insert_cols(1)
    title = sheet.cell(row=1, column=1)
    title.value = 'Advisor'
    for rowNum in range(2, sheet.max_row):
        major = sheet.cell(row=rowNum, column=2).value
        if major in advisor_major_ug:
            sheet.cell(row=rowNum, column=1).value = advisor_major_ug[major]
        if major in advisor_major_gr:
            sheet.cell(row=rowNum, column=1).value = advisor_major_gr[major]

    wb2_active.save('/Users/nbenzschawel/Downloads/Fall 201840 - Registration.xlsx')
