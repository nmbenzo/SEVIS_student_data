from Handlers.file_imports import SEVIS_initial_status_stud, No_show_UG, No_show_GR, \
    SEV_initial_data, wb_cancel_ug,  ug_sheet, gr_sheet, ug_row_max, \
    gr_row_max, gr_col_max, initial_max_row, sevis_initial_ws

def copy_new_Range(startCol, startRow, endCol, endRow, gr_sheet):
    """
    Copies a range of cells as a nested list
    Takes: start cell, end cell, and the sheet we want to copy from
    """
    rangeSelected = []
    for i in range(startRow, endRow + 1, 1):
        rowSelected = []
        for j in range(startCol, endCol + 1, 1):
            rowSelected.append(gr_sheet.cell(row=i, column=j).value)
        rangeSelected.append(rowSelected)

    return rangeSelected


def paste_new_Range(startCol, startRow, endCol, endRow, sheetReceiving, copiedData):
    """Pastes the selected data from copy_new_Range to your desired output worksheet"""
    countRow = 0
    for i in range(startRow, endRow + 1, 1):
        countCol = 0
        for j in range(startCol, endCol + 1, 1):
            sheetReceiving.cell(row=i, column=j).value = copiedData[countRow][countCol]
            countCol += 1
        countRow += 1


def create_new_Cancel_Data():
    """Pastes copied range to new sheet which needs to be updated"""
    if ug_sheet.cell(row=1, column=1).value == 'Passport Last Name':
        selectedRange = copy_new_Range(1, 2, gr_col_max, gr_row_max, gr_sheet)
        paste_new_Range(1, (ug_row_max+1), gr_col_max, (ug_row_max + gr_row_max-1), ug_sheet, selectedRange)

    wb_cancel_ug.save(No_show_UG)


def build_cancel_campusID(Cancel_SEVISID_CampusID):
    """Adds campus IDs to the SEVIS Initial Status spreadsheet """
    sevis_initial_ws.insert_cols(1)
    title = sevis_initial_ws.cell(row=1, column=1)
    title.value = 'CampusID'
    for rowNum in range(2, initial_max_row):
        sevisid = sevis_initial_ws.cell(row=rowNum, column=2).value
        for x in Cancel_SEVISID_CampusID:
            if x == sevisid:
                sevis_initial_ws.cell(row=rowNum, column=1).value = Cancel_SEVISID_CampusID[sevisid]

    SEV_initial_data.save(SEVIS_initial_status_stud)


def build_cancel_notes(Cancel_SEVISID_banner, Cancel_SEVISID_credits, Cancel_SEVISID_SV):
    """ Builds a brief set of note for each record displaying """
    sevis_initial_ws.insert_cols(1)
    title = sevis_initial_ws.cell(row=1, column=1)
    title.value = 'Cancellation Notes'
    for rowNum in range(2, initial_max_row):
        sevisid = sevis_initial_ws.cell(row=rowNum, column=3).value
        for x in Cancel_SEVISID_banner:
            for i in Cancel_SEVISID_credits:
                for j in Cancel_SEVISID_SV:
                    if x and i and j == sevisid:
                        if Cancel_SEVISID_SV[sevisid] != 'Yes':
                            sevis_initial_ws.cell(row=rowNum, column=1).value = \
                                'SV Status: Not checked in'  + ', Registered Units: ' \
                                + str(Cancel_SEVISID_credits[sevisid]) + ' credits, ' \
                                + 'Banner Status: ' + str(Cancel_SEVISID_banner[sevisid])
                        else:
                            sevis_initial_ws.cell(row=rowNum, column=1).value = \
                                'SV Status: ' + str(Cancel_SEVISID_SV[sevisid]) + ', Registered Units: ' \
                                + str(Cancel_SEVISID_credits[sevisid]) + ' credits, ' \
                                + 'Banner Status: ' + str(Cancel_SEVISID_banner[sevisid])

    SEV_initial_data.save(SEVIS_initial_status_stud)

