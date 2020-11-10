import os
os.getcwd()
from Handlers.file_imports import wb2_grad, wb3Live_grad, sheet2_grad, \
sheet3_grad, ws2_grad, ws3_grad, graduated_students


def add_advisor(master_deg_adv, bachelor_deg_adv):
    """match_advisor checks the majors in a column of workbook(ws) and
    then matches them with the advisor in a dictionary from the module:
    build_grad_data
    """
    sheet2_grad.insert_cols(1)
    title = ws2_grad.cell(row=1, column=1)
    title.value = 'Advisor'
    for row in range(2, ws2_grad.max_row):
        major = ws2_grad.cell(row=row, column=6).value
        if major in master_deg_adv:
            ws2_grad.cell(row=row, column=1).value = master_deg_adv[major]
        if major in bachelor_deg_adv:
            ws2_grad.cell(row=row, column=1).value = bachelor_deg_adv[major]

    wb2_grad.save(graduated_students)


def match_SEVISID_grad(campusID_SEVISID):
    """Builds a column of SEVISIDs for students based on the
    campusID_SEVISID dictionary
    """
    sheet2_grad.insert_cols(1)
    title = ws2_grad.cell(row=1, column=1)
    title.value = 'SEVISID'
    for rowNum in range(2, ws2_grad.max_row):
        campusID = ws2_grad.cell(row=rowNum, column=2).value
        for x in campusID_SEVISID:
            if x == campusID:
                ws2_grad.cell(row=rowNum, column=1).value = \
                campusID_SEVISID[campusID]

    wb2_grad.save(graduated_students)

#match_SEVISID_grad(campusID_SEVISID_grad)

def add_work_type(campusID_work_auth):
    """Builds an empty column. Loops through a range of campusIDs and then
    compares these against campusIDs in campusID_work_auth dictionary. When it
    finds a matched campusID in the campusID_work_auth dictionary it populates
    the empty column with the appropriate work authorization type
    """
    sheet2_grad.insert_cols(1)
    title = ws2_grad.cell(row=1, column=1)
    title.value = 'Work Authorization Type'
    for rowNum in range(2, ws2_grad.max_row):
        campusID = ws2_grad.cell(row=rowNum, column=3).value
        for x in campusID_work_auth:
            if x == campusID:
                ws2_grad.cell(row=rowNum, column=1).value = \
                campusID_work_auth[campusID]

    wb2_grad.save(graduated_students)


def add_work_enddate(campusID_workend):
    """Builds an empty column. Loops through a range of campusIDs and then
    compares these against campusIDs in campusID_workend dictionary. When it
    finds a matched campusID in the campusID_workend dictionary it populates
    the empty column with the appropriate work authorization end date.
    """
    sheet2_grad.insert_cols(1)
    title = ws2_grad.cell(row=1, column=1)
    title.value = 'Work Authorization End Date'
    for rowNum in range(2, ws2_grad.max_row):
        campusID = ws2_grad.cell(row=rowNum, column=4).value
        for i in campusID_workend:
            if i == campusID:
                ws2_grad.cell(row=rowNum, column=1).value = \
                campusID_workend[campusID]

    wb2_grad.save(graduated_students)


def add_profile_enddate(campusID_end_date):
    """Builds an empty column. Loops through a range of campusIDs and then
    compares these against campusIDs in campusID_end_date dictionary. When it
    finds a matched campusID in the campusID_end_date dictionary it populates
    the empty column with the appropriate profile end date.
    """
    sheet2_grad.insert_cols(1)
    title = ws2_grad.cell(row=1, column=1)
    title.value = 'Profile End Date'
    for rowNum in range(2, ws2_grad.max_row):
        campusID = ws2_grad.cell(row=rowNum, column=5).value
        for i in campusID_end_date:
            if i == campusID:
                ws2_grad.cell(row=rowNum, column=1).value = \
                campusID_end_date[campusID]

    wb2_grad.save(graduated_students)


def add_emails(campusID_emails):
    sheet3_grad.insert_cols(1)
    title = ws3_grad.cell(row=1, column=1)
    title.value = 'Emails'
    for rowNum in range(2, ws2_grad.max_row):
        campusID = ws3_grad.cell(row=rowNum, column=6).value
        for i in campusID_emails:
            if i == campusID:
                ws3_grad.cell(row=rowNum, column=1).value = \
                campusID_emails[campusID]

    wb3Live_grad.save(graduated_students)


