from import_app_modules import *
from GoogleSheets.spreadsheet import *


def new_menu(GLBL_USER_CHOICE):
    """
    menu where users can select a section of the
    spreadsheet to populate about new students requiring registration
     """
    user_input = input(NEWs_USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            match_SEVISID(campusID_SEVISID)
            match_major_data(SEVISID_major)
            match_advisor(advisor_major_ug, advisor_major_gr)
            add_advisor_notes()
            print('Ran all functions')
        elif user_input == 'ad':
            match_advisor(advisor_major_ug, advisor_major_gr)
            print("Added student's advisor")
        elif user_input == 'm':
            match_SEVISID(campusID_SEVISID)
            print('Added campusIDs')
        elif user_input == 'w':
            match_major_data(SEVISID_major)
            print('Added student majors')
        elif user_input == 'n':
            add_advisor_notes()
            print('Added advisor notes based on available data')

        return GLBL_USER_CHOICE


def active_menu(GLBL_USER_CHOICE):
    """
    menu where users can select a section of the
    spreadsheet to populate about new students requiring registration
    """
    user_input = input(ACTIVEs_USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            match_SEVISID(campusID_SEVISID)
            match_major_data(SEVISID_major)
            match_advisor(advisor_major_ug, advisor_major_gr)
            print('Ran all functions')
        elif user_input == 'm':
            match_SEVISID(campusID_SEVISID)
            print('Added campusIDs')
        elif user_input == 'w':
            match_major_data(SEVISID_major)
            print('Added student majors')
        elif user_input == 'e':
            match_advisor(advisor_major_ug, advisor_major_gr)
            print("Added student's advisor")

        return GLBL_USER_CHOICE


def grad_menu(GLBL_USER_CHOICE):
    """
    menu where users can select a section of the
    spreadsheet to populate about graduated students
    """
    user_input = input(GRADUATEs_USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            add_advisor(master_deg_adv, bachelor_deg_adv)
            match_SEVISID(campusID_SEVISID)
            add_work_type(campusID_work_auth)
            add_work_enddate(campusID_workend)
            add_profile_enddate(campusID_end_date)
            add_emails(campusID_emails)
            print('Ran all functions')
        elif user_input == 'ad':
            add_advisor(master_deg_adv, bachelor_deg_adv)
            print("Added student's advisor")
        elif user_input == 'm':
            match_SEVISID(campusID_SEVISID)
            print('Added campusIDs')
        elif user_input == 'w':
            add_work_type(campusID_work_auth)
            print('Added work authorization types')
        elif user_input == 'e':
            add_work_enddate(campusID_workend)
            print('Added work end dates')
        elif user_input == 'p':
            add_profile_enddate(campusID_end_date)
            print('Added profile end dates')
        elif user_input == 's':
            add_emails(campusID_emails)
            print('Added student emails')

        return GLBL_USER_CHOICE


def sync_googlesheets(GLBL_USER_CHOICE):
    """
    menu where users can select a spreadsheet to sync with GoogleSheets
    """
    user_input = input(SYNC_GOOGLESHEETS)
    while user_input != 'q':
        if user_input == 'n':
            update_new_students(sh)
            print('Syncing with GoogleSheets')
        elif user_input == 'a':
            pass
            print('Syncing with GoogleSheets')
        elif user_input == 'g':
            pass
            print('Syncing with GoogleSheets')
        elif user_input == 'c':
            pass
            print('Syncing with GoogleSheets')

        return GLBL_USER_CHOICE


def run_converter(GLBL_USER_CHOICE):
    """
    menu to convert choose which xlsx files to convert to csv

    """
    user_input = input(CONVERT_TO_CSV)
    while user_input != 'q':
        if user_input == 'n':
            newstudent_excel_to_csv()
            print('Converted file from XLSX to CSV')
        elif user_input == 'a':
            activestud_excel_to_cvs()
            print('Converted file from XLSX to CSV')
        elif user_input == 'g':
            gradstud_excel_to_cvs()
            print('Converted file from XLSX to CSV')
        elif user_input == 'c':
            completedstud_excel_to_cvs()
            print('Converted file from XLSX to CSV')

        return GLBL_USER_CHOICE