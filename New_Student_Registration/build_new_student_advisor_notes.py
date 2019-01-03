import os
os.getcwd()
from Handlers.file_imports import ws2_new, wb2_new


def new_match_SEVISID(campusID_SEVISID):
    """
    match_SEVISID compares SEVISIDs from two separate workbooks(ws, ws2)
    and then populates a blank column with the appropriate BannerID(campusID)
    """
    ws2_new.insert_cols(1)
    title = ws2_new.cell(row=1, column=1)
    title.value = 'campusID'
    for rowNum in range(2, ws2_new.max_row):
        sevis_ID = ws2_new.cell(row=rowNum, column=2).value
        for x in campusID_SEVISID:
            if x == sevis_ID:
                ws2_new.cell(row=rowNum, column=1).value = campusID_SEVISID[sevis_ID]

    wb2_new.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')


def new_match_major_data(SEVISID_major):
    """match_major_data compares SEVISIDs against major data and then populates
    a blank column with the appropriate major data when a SEVISID match is found.
    """
    ws2_new.insert_cols(1)
    title = ws2_new.cell(row=1, column=1)
    title.value = 'Major'
    for rowNum in range(2, ws2_new.max_row):
        sevis_ID = ws2_new.cell(row=rowNum, column=3).value
        for x in SEVISID_major:
            if x == sevis_ID:
                ws2_new.cell(row=rowNum, column=1).value = SEVISID_major[sevis_ID]

    wb2_new.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')


def new_match_advisor(advisor_major_ug, advisor_major_gr):
    """
    match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module: data
    """
    ws2_new.insert_cols(1)
    title = ws2_new.cell(row=1, column=1)
    title.value = 'Advisor'
    for rowNum in range(2, ws2_new.max_row):
        major = ws2_new.cell(row=rowNum, column=2).value
        if major in advisor_major_ug:
            ws2_new.cell(row=rowNum, column=1).value = advisor_major_ug[major]
        if major in advisor_major_gr:
            ws2_new.cell(row=rowNum, column=1).value = advisor_major_gr[major]

    wb2_new.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')


def add_advisor_notes(SEVISID_checked_in, SEVISID_cr_hours):
    """
    add_advisor notes references the checked_in columns of workbook(ws)
    and then builds advisor notes based on which columns are populated
    """
    ws2_new.insert_cols(1)
    title = ws2_new.cell(row=1, column=1)
    title.value = 'Advisor Notes'
    for rowNum in range(2, ws2_new.max_row):
        sevis_ID = ws2_new.cell(row=rowNum, column=5).value
        for x in SEVISID_checked_in:
            for j in SEVISID_cr_hours:
                if x and j == sevis_ID:
                    ws2_new.cell(row=rowNum, column=1).value = 'SV Status: ' + str(SEVISID_checked_in[sevis_ID]) \
                    + ', Registered Units: ' + str(SEVISID_cr_hours[sevis_ID]) + ' credits'

    wb2_new.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')

