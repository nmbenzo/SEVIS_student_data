import time
from Handlers.import_app_modules import *
from Handlers.import_modules import *


def build_it_all(GLBL_USER_CHOICE):
    """
    This function is a type of a master function that runs all necessary
    functions to build populate spreadsheets, merge them into one workbook,
    and then upload them with a specified naming convention to a Google Team
    Drive
     """
    user_input = input(BUILD_REG_DATA)
    while user_input != 'q':
        if user_input == 'y':
            time.sleep(1.0)
            create_new_Student_Data()
            time.sleep(1.5)
            new_match_SEVISID(campusID_SEVISID)
            new_match_major_data(SEVISID_major)
            new_match_advisor(advisor_major_ug, advisor_major_gr)
            add_advisor_notes(SEVISID_checked_in, SEVISID_cr_hours)
            time.sleep(0.3)
            sort_new_data()
            print('\n*** Ran all functions for building NEW student registration notes: ***')
            time.sleep(1)
            print("Added student's advisor" + '\nAdded campusIDs' + '\nAdded student majors' \
            + '\nAdded SV & unit registration notes')
            time.sleep(1)

            print('\nBeginning data aggregation for ACTIVE Status students...')
            create_active_Student_Data()
            time.sleep(1.3)
            active_match_SEVISID(active_campusID_SEVISID)
            time.sleep(0.3)
            match_units(active_SEVISID_units)
            time.sleep(0.3)
            match_major_data(active_SEVISID_major)
            time.sleep(0.3)
            match_advisor(advisor_major_ug, advisor_major_gr)
            time.sleep(0.3)
            sort_active_data()
            print('\n*** Ran all functions for building notes for SEVIS Active students: ***')
            time.sleep(0.5)
            print("Added student's advisor" + '\nAdded campusIDs' + "\nAdded student's majors" \
                + '\nAdded Unit registration notes')

            time.sleep(1)
            print('\nBeginning data aggregation for NO SHOW Students...')
            time.sleep(0.5)
            create_new_Cancel_Data()
            time.sleep(0.5)
            create_NoShow_Student_Data()
            time.sleep(0.5)
            print('\nGraduate No Show range copied and pasted')
            time.sleep(1.5)
            build_cancel_campusID(Cancel_SEVISID_CampusID)
          
            time.sleep(1)
            build_cancel_notes(Cancel_SEVISID_banner, Cancel_SEVISID_credits,
                               Cancel_SEVISID_SV)
            print('\n*** Ran all functions for building Cancel List notes: ***')
            time.sleep(1)
            print('\nAdded Campus IDs and student notes:' + \
                  '\nBanner Status' + '\nCredits' + '\nCheck-in Status')

            time.sleep(0.5)
            print('\nMerging all SEVIS Registration Workbooks...')
            merge_all_workbooks()
            print('\n*** Final Workbook created titled: SEVIS Registration ***')
            time.sleep(0.5)
            print('\nPreparing upload...')

            time.sleep(1.5)
            drive_sheet_upload()
            print('\nSyncing file with Google_Drive')
            time.sleep(1.0)
            print(f'\n** {uploaded_file_name} MASTER file imported into Team Drives folder **')
            time.sleep(1.5)
            print('\n*** Data building and processing COMPLETE ***')

        return GLBL_USER_CHOICE


def new_menu(GLBL_USER_CHOICE):
    """
    menu where users can select a section of the
    spreadsheet to populate about new students requiring registration
     """
    user_input = input(NEWs_USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            create_new_Student_Data()
            time.sleep(2)
            new_match_SEVISID(campusID_SEVISID)
            new_match_major_data(SEVISID_major)
            new_match_advisor(advisor_major_ug, advisor_major_gr)
            add_advisor_notes(SEVISID_checked_in, SEVISID_cr_hours)
            print('Ran all functions for building new student registration notes:' + "\nAdded student's advisor" + \
                  '\nAdded campusIDs' + '\nAdded student majors' + '\nAdded SV & unit registration notes')
        elif user_input == 'ad':
            new_match_advisor(advisor_major_ug, advisor_major_gr)
            print("Added student's advisor")
        elif user_input == 'm':
            new_match_SEVISID(campusID_SEVISID)
            print('Added campusIDs')
        elif user_input == 'w':
            new_match_major_data(SEVISID_major)
            print('Added student majors')
        elif user_input == 'c':
            add_advisor_notes(SEVISID_checked_in, SEVISID_cr_hours)
            print('Added SV & unit registration notes')

        return GLBL_USER_CHOICE


def active_menu(GLBL_USER_CHOICE):
    """
    menu where users can select a section of the
    spreadsheet to populate about new students requiring registration
    """
    user_input = input(ACTIVEs_USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            create_active_Student_Data()
            time.sleep(1)
            active_match_SEVISID(active_campusID_SEVISID)
            time.sleep(0.5)
            match_units(active_SEVISID_units)
            time.sleep(0.5)
            match_major_data(active_SEVISID_major)
            time.sleep(0.5)
            match_advisor(advisor_major_ug, advisor_major_gr)
            print('Ran all functions for building notes for SEVIS Active students:')
        elif user_input == 'm':
            active_match_SEVISID(active_campusID_SEVISID)
            print('Added campusIDs')
        elif user_input == 'w':
            match_major_data(active_SEVISID_major)
            print('Added student majors')
        elif user_input == 'e':
            match_advisor(advisor_major_ug, advisor_major_gr)
            print("Added student's advisor")

        return GLBL_USER_CHOICE


def cancellation_menu(GLBL_USER_CHOICE):
    """
    menu where users can merge UG and GR cancellation lists from ISSM and then
    poplate data relevant to students that haven't checked in or are not registered
    """
    user_input = input(BUILD_CANCEL_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            create_new_Cancel_Data()
            print('Processing data...')
            time.sleep(1)
            create_NoShow_Student_Data()
            print(f'Data copied: current range = {NOSHOW_students_sheet.max_row}')
            print('Range copied and pasted')
            time.sleep(1.5)
            print(f'New Row Range = {NOSHOW_students_sheet.max_row}')
            time.sleep(0.5)
            build_cancel_campusID(Cancel_SEVISID_CampusID)
            time.sleep(0.2)
            build_cancel_notes(Cancel_SEVISID_banner, Cancel_SEVISID_credits,
                               Cancel_SEVISID_SV)
            print('Added Campus IDs and student notes')
        elif user_input == 'm':
            create_new_Cancel_Data()
            print('Processing data...')
            time.sleep(1)
            print(f'Data copied: current range = {ug_row_max}')
            print('Graduate Cancel range copied and pasted')
            time.sleep(0.5)
            print(f'New Row Range = {ug_row_max}')

        return GLBL_USER_CHOICE


def completed_menu(GLBL_USER_CHOICE):
    """
    menu where users can elect to match SEVIS COMPLETED students with their ISSM
    Profile Status
    """
    user_input = input(COMPLETED_STUDENTS)
    while user_input != 'n':
        if user_input == 'y':
            match_SEVISID_completed(SEVISID_completed)
            print('Matching SEVIS IDs and building notes for discrepancies')

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


def merge_workbooks(GLBL_USER_CHOICE):
    """
    menu where users can elect to merge all registration workbooks
    """
    user_input = input(MERGE_WORKBOOKS)
    while user_input != 'n':
        if user_input == 'y':
            merge_all_workbooks()
            print('Merging all SEVIS Registration Workbooks')

        return GLBL_USER_CHOICE


def sync_googlesheets(GLBL_USER_CHOICE):
    """
    menu where users can select a spreadsheet to sync with Google_Drive
    """
    user_input = input(SYNC_GOOGLESHEETS)
    while user_input != 'q':
        if user_input == 'a':
            drive_sheet_upload()
            print('Syncing with Google_Drive')
            time.sleep(1)
            print(f'** {Registration_file} file imported in Team Drives folder **')
        elif user_input == 'd':
            download_file()
        elif user_input == 'r':
            drive_doc_upload()
            print('Syncing with Google_Drive')
            time.sleep(1)
            print(f'** {REGISTRATION_TIMELINE} file imported in Team Drives folder **')

        return GLBL_USER_CHOICE


def emails(GLBL_USER_CHOICE):
    """Menu where users can elect to send emails to students"""
    user_input = input(EMAIL_TO_STUDENT_template)
    while user_input != 'q':
        if user_input == 'e':
            time.sleep(0.5)
            print('Please choose an email recipient...')
            time.sleep(0.5)
            singular_email()
            time.sleep(0.75)
            print('\nEmail sent!')
        elif user_input == 'm':
            new_user_input = input(EMAIL_TO_STUDENT_type)
            if new_user_input == 'f':
                time.sleep(0.5)
                print('Sending email to students who need to pay the I-901 fee...')
                time.sleep(0.5)
                multiple_emails(emails='')
                time.sleep(0.75)
                print('\nEmails sent to users in email list!')
            elif new_user_input == 'u':
                time.sleep(0.5)
                print('Sending email to students who are underenrolled...')
                time.sleep(0.5)
                multiple_emails(emails='')
                time.sleep(0.75)
                print('\nEmails sent to users in email list!')
            elif new_user_input == 'p':
                time.sleep(0.5)
                print('Sending email to students who have a bad phone number for registration...')
                time.sleep(0.5)
                multiple_emails(emails='')
                time.sleep(0.75)
                print('\nEmails sent to users in email list!')
            elif new_user_input == 'a':
                time.sleep(0.5)
                print('Sending email to students who have a bad address for registration...')
                time.sleep(0.5)
                multiple_emails(emails='')
                time.sleep(0.75)
                print('\nEmails sent to users in email list!')

        return GLBL_USER_CHOICE


def transfer_menu(GLBL_USER_CHOICE):
    """
    Menu to access and modify transfer student data

    """
    user_input = input(MANAGE_TRANSFER_DATA)
    while user_input != 'q':
        if user_input == 'n':
            create_workbook()
        elif user_input == 'a':
            create_new_Data()
            time.sleep(3)
            transfer_match_major_data(SEVISID_major)
            print("\nAdded Student's Major")
            time.sleep(0.5)
            sort_data()
            time.sleep(2)
            check_in_fsa()
            time.sleep(2)
            paste_to_final()
            time.sleep(2)
        elif user_input == 's':
            sort_data()
        elif user_input == 'p':
            check_in_fsa()
        elif user_input == 'f':
            paste_to_final()
        elif user_input == 'u':
            find_in_fsa()
        elif user_input == 'c':
            grab_final_data()

        return GLBL_USER_CHOICE

