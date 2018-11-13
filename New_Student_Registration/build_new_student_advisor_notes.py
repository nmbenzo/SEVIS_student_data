import os
os.getcwd()
from major_advisor_data import advisor_major_ug, advisor_major_gr
from New_Student_Registration.build_student_data import campusID_SEVISID, wb2, ws1, ws2, SEVISID_major


def match_SEVISID(campusID_SEVISID):
    """
    match_SEVISID compares SEVISIDs from two separate workbooks(ws, ws2)
    and then populates a blank column with the appropriate BannerID(campusID)
    """
    ws2.insert_cols(1)
    title = ws2.cell(row=1, column=1)
    title.value = 'campusID'
    for rowNum in range(2, ws2.max_row):
        sevis_ID = ws2.cell(row=rowNum, column=2).value
        for x in campusID_SEVISID:
            if x == sevis_ID:
                ws2.cell(row=rowNum, column=1).value = campusID_SEVISID[sevis_ID]

    wb2.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')


def match_major_data(SEVISID_major):
    """match_major_data compares SEVISIDs against major data and then populates
    a blank column with the appropriate major data when a SEVISID match is found.
    """
    ws2.insert_cols(1)
    title = ws2.cell(row=1, column=1)
    title.value = 'Major'
    for rowNum in range(2, ws2.max_row):
        sevis_ID = ws2.cell(row=rowNum, column=3).value
        for x in SEVISID_major:
            if x == sevis_ID:
                ws2.cell(row=rowNum, column=1).value = SEVISID_major[sevis_ID]

    wb2.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')


def match_advisor(advisor_major_ug, advisor_major_gr):
    """
    match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module: data
    """
    ws2.insert_cols(1)
    title = ws2.cell(row=1, column=1)
    title.value = 'Advisor'
    for rowNum in range(2, ws2.max_row):
        major = ws2.cell(row=rowNum, column=2).value
        if major in advisor_major_ug:
            ws2.cell(row=rowNum, column=1).value = advisor_major_ug[major]
        if major in advisor_major_gr:
            ws2.cell(row=rowNum, column=1).value = advisor_major_gr[major]

    wb2.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')


def add_advisor_notes():
    """
    add_advisor notes references the checked_in columns of workbook(ws)
    and then builds advisor notes based on which columns are populated
    """
    ws2.insert_cols(1)
    title = ws2.cell(row=1, column=1)
    title.value = 'Advisor Notes'
    for rowNum in range(2, ws1.max_row): # skip the first row and go to the last row
     checked_in = ws1.cell(row=rowNum, column=19).value
     cr_hours = ws1.cell(row=rowNum, column=33).value
     if checked_in == 'Yes':
         ws2.cell(row=rowNum, column=1).value = 'SV Completed, '\
         + 'Registered: ' + str(cr_hours) + 'credits'
     else:
         ws2.cell(row=rowNum, column=1).value = 'No SV '\
         + 'Registered, ' + str(cr_hours) + 'credits'

     wb2.save('/Users/nbenzschawel/Downloads/SEVIS_raw_data.xlsx')







