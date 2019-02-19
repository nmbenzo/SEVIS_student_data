import time
import Handlers.menu_selection_options as menu_options
import Handlers.import_modules as func
import Handlers.import_dictionaries as dicts


global_menu = menu_options.GLBL_USER_CHOICE


class Menu:

    def __init__(self):
        self.global_menu = global_menu

    def build_it_all(self, global_menu):
        """
        This function is a type of a master function that runs all necessary
        functions to build populate spreadsheets, merge them into one workbook,
        and then upload them with a specified naming convention to a Google Team
        Drive
         """
        user_input = input(menu_options.BUILD_REG_DATA)
        while user_input != 'q':
            if user_input == 'y':
                print('\nCreating data now...')
                time.sleep(0.5)
                func.create_new_Student_Data()
                time.sleep(1.5)
                func.new_match_SEVISID(dicts.campusID_SEVISID)
                func.new_match_major_data(dicts.SEVISID_major)
                func.new_match_advisor(dicts.advisor_major_ug,
                                       dicts.advisor_major_gr)
                func.add_advisor_notes(dicts.SEVISID_checked_in,
                                       dicts.SEVISID_cr_hours)
                time.sleep(0.3)
                func.add_registration_column()
                time.sleep(0.3)
                func.sort_new_data()
                print('\n*** Ran all functions for building NEW student registration notes: ***')
                time.sleep(1)
                print("Added student's advisor" + '\nAdded campusIDs' + '\nAdded student majors' \
                + '\nAdded SV & unit registration notes')
                time.sleep(1)

                print('\nBeginning data aggregation for ACTIVE Status students...')
                func.create_active_Student_Data()
                time.sleep(1.3)
                func.active_match_SEVISID(dicts.active_campusID_SEVISID)
                time.sleep(0.3)
                func.match_units(dicts.active_SEVISID_units)
                time.sleep(0.3)
                func.match_major_data(dicts.active_SEVISID_major)
                time.sleep(0.3)
                func.match_advisor(dicts.advisor_major_ug,
                                   dicts.advisor_major_gr)
                time.sleep(0.3)
                func.add_notes_column()
                time.sleep(0.3)
                func.add_graduated_student_emails(dicts.sevisID_emails)
                time.sleep(0.5)
                func.add_registration_status_column()
                time.sleep(0.3)
                func.add_graduation_status_column()
                time.sleep(0.3)
                func.sort_active_data()
                print('\n*** Ran all functions for building notes for SEVIS Active students: ***')
                time.sleep(0.5)
                print("Added student's advisor" + '\nAdded campusIDs' + "\nAdded student's majors" \
                    + '\nAdded Unit registration notes')

                time.sleep(1)
                print('\nBeginning data aggregation for Cancellation Lists...')
                time.sleep(0.5)
                print('Merging UG and GR No Show reports...')
                func.create_new_Cancel_Data()
                time.sleep(0.5)
                func.create_NoShow_Student_Data()
                time.sleep(0.5)
                print('\nUG and GR No Show reports merged successfully!')
                time.sleep(0.5)
                func.build_apdc_notes(dicts.Cancel_APDC)
                time.sleep(1.5)
                func.build_level_data(dicts.Cancel_Level)
                time.sleep(1)
                func.build_cancel_campusID(dicts.Cancel_SEVISID_CampusID)
                time.sleep(0.2)
                func.build_cancel_notes(dicts.Cancel_SEVISID_banner,
                                        dicts.Cancel_SEVISID_credits,
                                        dicts.Cancel_SEVISID_SV)
                print('\n*** Ran all functions for building Cancel List notes: ***')
                time.sleep(1)
                print('Added Campus IDs, APDC Codes, Level of Education, and student notes:' + \
                      '\nBanner Status' + '\nCredits' + '\nCheck-in Status')

                time.sleep(1)
                print('\nMerging all SEVIS Registration Workbooks...')
                func.merge_all_workbooks()
                print('\n*** Final Workbook created titled: SEVIS Registration ***')
                time.sleep(0.5)
                print('\nPreparing upload...')

                time.sleep(1.5)
                print('\nSyncing file with Google_Drive')
                func.drive_sheet_upload()
                time.sleep(1.0)
                print(f'\n** {func.uploaded_file_name} MASTER file imported into ISSS Team Drives folder **')
                time.sleep(1)
                print('\n*** DATA BUILDING AND PROCESSING COMPLETE ***')
                time.sleep(1)

            return global_menu


    def final_build_it(self, global_menu):

        """
        This function merges several sheets from the current workflow in the
        Google TeamDrive with a final active student data build, merges them into
        one workbook, and then upload them with a specified naming convention
        to the current ISSS TeamDrive.
         """
        user_input = input(menu_options.BUILD_REG_DATA)
        while user_input != 'q':
            if user_input == 'y':
                print('\nCreating data now...')
                time.sleep(0.5)
                print(
                    '\nBeginning data aggregation for ACTIVE Status students...')
                func.create_active_Student_Data()
                time.sleep(1.3)
                func.active_match_SEVISID(dicts.active_campusID_SEVISID)
                time.sleep(0.3)
                func.match_units(dicts.active_SEVISID_units)
                time.sleep(0.3)
                func.match_major_data(dicts.active_SEVISID_major)
                time.sleep(0.3)
                func.match_advisor(dicts.advisor_major_ug,
                                   dicts.advisor_major_gr)
                time.sleep(0.3)
                func.add_notes_column()
                time.sleep(0.3)
                func.add_graduated_student_emails(dicts.sevisID_emails)
                time.sleep(0.5)
                func.add_registration_status_column()
                time.sleep(0.3)
                func.add_graduation_status_column()
                time.sleep(0.3)
                func.sort_active_data()
                print(
                    '\n*** Ran all functions for building notes for SEVIS Active students: ***')
                time.sleep(0.5)
                print(
                    "Added student's advisor" + '\nAdded campusIDs' + "\nAdded student's majors" \
                    + '\nAdded Unit registration notes')
                time.sleep(1)
                print('\nMerging all SEVIS Registration Workbooks...')
                func.final_merge_all_workbooks()
                print(
                    '\n*** Final Workbook created titled: SEVIS Registration ***')
                time.sleep(0.5)
                print('\nPreparing upload...')

                time.sleep(1.5)
                print('\nSyncing file with Google_Drive')
                func.drive_sheet_upload()
                time.sleep(1.0)
                print(
                    f'\n** {func.uploaded_file_name} MASTER file imported into ISSS Team Drives folder **')
                time.sleep(1)
                print('\n*** DATA BUILDING AND PROCESSING COMPLETE ***')
                time.sleep(1)

            return global_menu


    def transfer_menu(self, global_menu):
        """
        Menu to access and modify transfer student data

        """
        user_input = input(menu_options.MANAGE_TRANSFER_DATA)
        while user_input != 'q':
            if user_input == 'n':
                func.create_workbook()
            elif user_input == 'a':
                func.create_new_Data()
                time.sleep(3)
                func.transfer_match_major_data(dicts.SEVISID_major)
                print("\nAdded Student's Major")
                time.sleep(0.5)
                func.sort_data()
                time.sleep(2)
                func.check_in_fsa()
                time.sleep(2)
                func.paste_to_final()
                time.sleep(2)
            elif user_input == 's':
                func.sort_data()
            elif user_input == 'p':
                func.check_in_fsa()
            elif user_input == 'f':
                func.paste_to_final()
            elif user_input == 'u':
                func.find_in_fsa()
            elif user_input == 'c':
                func.grab_final_data()

            return global_menu


    def sync_googlesheets(self, global_menu):
        """
        menu where users can select a spreadsheet to sync with Google_Drive
        """
        user_input = input(menu_options.SYNC_GOOGLESHEETS)
        while user_input != 'q':
            if user_input == 'a':
                func.drive_sheet_upload()
                print('Syncing with Google_Drive')
                time.sleep(1)
                print(f'** {func.Registration_file} file imported in Team Drives folder **')
            elif user_input == 'd':
                func.download_file()
            elif user_input == 'r':
                func.drive_doc_upload()
                print('Syncing with Google_Drive')
                time.sleep(1)
                print(f'** {func.REGISTRATION_TIMELINE} file imported in Team Drives folder **')

            return global_menu


    def sms(self, global_menu):
        """
        Menu where users can select to send a text to a student or email blast
        multiple students
        """
        user_input = input(menu_options.SMS_MESSAGE)
        while user_input != 'q':
            if user_input == 's':
                func.send_sms(func.client,
                              func.get_message_content(func.content_list))
            elif user_input == 'b':
                func.send_blast_sms(func.client,
                                    func.get_blast_list(func.group_list),
                                    func.get_message_content(func.content_list))

            return global_menu


    def emails(self, global_menu):
        """Menu where users can elect to send emails to students"""
        user_input = input(menu_options.EMAIL_TO_STUDENT_template)
        while user_input != 'q':
            if user_input == 'e':
                func.singular_email(
                func.get_emessage_content(func.e_content_list))
                time.sleep(0.5)
            elif user_input == 'm':
                func.multiple_emails(
                func.get_eblast_list(func.e_group_list),
                func.get_emessage_content(func.e_content_list))
                time.sleep(0.5)


            return global_menu


    def new_menu(self, global_menu):
        """
        menu where users can select a section of the
        spreadsheet to populate about new students requiring registration
         """
        user_input = input(menu_options.NEWs_USER_CHOICE)
        while user_input != 'q':
            if user_input == 'a':
                func.create_new_Student_Data()
                time.sleep(2)
                func.new_match_SEVISID(dicts.campusID_SEVISID)
                func.new_match_major_data(dicts.SEVISID_major)
                func.new_match_advisor(dicts.advisor_major_ug,
                                       dicts.advisor_major_gr)
                func.add_advisor_notes(dicts.SEVISID_checked_in,
                                       dicts.SEVISID_cr_hours)
                print('Ran all functions for building new student registration notes:' + "\nAdded student's advisor" + \
                      '\nAdded campusIDs' + '\nAdded student majors' + '\nAdded SV & unit registration notes')
            elif user_input == 'ad':
                func.new_match_advisor(dicts.advisor_major_ug,
                                       dicts.advisor_major_gr)
                print("Added student's advisor")
            elif user_input == 'm':
                func.new_match_SEVISID(dicts.campusID_SEVISID)
                print('Added campusIDs')
            elif user_input == 'w':
                func.new_match_major_data(dicts.SEVISID_major)
                print('Added student majors')
            elif user_input == 'c':
                func.add_advisor_notes(dicts.SEVISID_checked_in,
                                       dicts.SEVISID_cr_hours)
                print('Added SV & unit registration notes')

            return global_menu


    def active_menu(self, global_menu):
        """
        menu where users can select a section of the
        spreadsheet to populate about new students requiring registration
        """
        user_input = input(menu_options.ACTIVEs_USER_CHOICE)
        while user_input != 'q':
            if user_input == 'a':
                func.create_active_Student_Data()
                time.sleep(1)
                func.active_match_SEVISID(dicts.active_campusID_SEVISID)
                time.sleep(0.5)
                func.match_units(dicts.active_SEVISID_units)
                time.sleep(0.5)
                func.match_major_data(dicts.active_SEVISID_major)
                time.sleep(0.5)
                func.match_advisor(dicts.advisor_major_ug,
                                   dicts.advisor_major_gr)
                time.sleep(0.5)
                func.sort_active_data()
                print(
                    '\n*** Ran all functions for building notes for SEVIS Active students: ***')
                time.sleep(0.5)
                print(
                    "Added student's advisor" +'\nAdded campusIDs' +
                    "\nAdded student's majors" + '\nAdded Unit registration notes')
                print('Ran all functions for building notes for SEVIS Active students:')
            elif user_input == 'm':
                func.active_match_SEVISID(dicts.active_campusID_SEVISID)
                print('Added campusIDs')
            elif user_input == 'w':
                func.match_major_data(dicts.active_SEVISID_major)
                print('Added student majors')
            elif user_input == 'e':
                func.match_advisor(dicts.advisor_major_ug,
                                   dicts.advisor_major_gr)
                print("Added student's advisor")

            return global_menu


    def cancellation_menu(self, global_menu):
        """
        menu where users can merge UG and GR cancellation lists from ISSM and then
        poplate data relevant to students that haven't checked in or are not registered
        """
        user_input = input(menu_options.BUILD_CANCEL_CHOICE)
        while user_input != 'q':
            if user_input == 'a':
                func.create_new_Cancel_Data()
                print('Processing data...')
                time.sleep(1)
                func.create_NoShow_Student_Data()
                print(f'Data copied: current range = '
                      f'{func.NOSHOW_students_sheet.max_row}')
                print('Range copied and pasted')
                time.sleep(1.5)
                print(f'New Row Range = '
                      f'{func.NOSHOW_students_sheet.max_row}')
                time.sleep(0.5)
                func.build_apdc_notes(dicts.Cancel_APDC)
                time.sleep(0.5)
                func.build_level_data(dicts.Cancel_Level)
                time.sleep(0.5)
                func.build_cancel_campusID(dicts.Cancel_SEVISID_CampusID)
                time.sleep(0.2)
                func.build_cancel_notes(dicts.Cancel_SEVISID_banner,
                                        dicts.Cancel_SEVISID_credits,
                                        dicts.Cancel_SEVISID_SV)
                print('Added Campus IDs, APDC Code, and student notes')
            elif user_input == 'm':
                func.create_new_Cancel_Data()
                print('Processing data...')
                time.sleep(1)
                print(f'Data copied: current range = {func.ug_row_max}')
                print('Graduate Cancel range copied and pasted')
                time.sleep(0.5)
                print(f'New Row Range = {func.ug_row_max}')

            return global_menu


    def completed_menu(self, global_menu):
        """
        menu where users can elect to match SEVIS COMPLETED students with their ISSM
        Profile Status
        """
        user_input = input(menu_options.COMPLETED_STUDENTS)
        while user_input != 'n':
            if user_input == 'y':
                func.match_SEVISID_completed(func.SEVISID_completed)
                print('Matching SEVIS IDs and building notes for discrepancies')

            return global_menu


    def grad_menu(self, global_menu):
        """
        menu where users can select a section of the
        spreadsheet to populate about graduated students
        """
        user_input = input(menu_options.GRADUATEs_USER_CHOICE)
        while user_input != 'q':
            if user_input == 'a':
                func.add_advisor(dicts.master_deg_adv, dicts.bachelor_deg_adv)
                func.match_SEVISID(dicts.campusID_SEVISID)
                func.add_work_type(dicts.campusID_work_auth)
                func.add_work_enddate(dicts.campusID_workend)
                func.add_profile_enddate(dicts.campusID_end_date)
                func.add_emails(dicts.campusID_emails)
                print('Ran all functions')
            elif user_input == 'ad':
                func.add_advisor(dicts.master_deg_adv, dicts.bachelor_deg_adv)
                print("Added student's advisor")
            elif user_input == 'm':
                func.match_SEVISID(dicts.campusID_SEVISID)
                print('Added campusIDs')
            elif user_input == 'w':
                func.add_work_type(dicts.campusID_work_auth)
                print('Added work authorization types')
            elif user_input == 'e':
                func.add_work_enddate(dicts.campusID_workend)
                print('Added work end dates')
            elif user_input == 'p':
                func.add_profile_enddate(dicts.campusID_end_date)
                print('Added profile end dates')
            elif user_input == 's':
                func.add_emails(dicts.campusID_emails)
                print('Added student emails')

            return global_menu
