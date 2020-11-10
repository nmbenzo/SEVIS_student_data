import Handlers.menu_selection_options as menu_options
import Handlers.import_dictionaries as dict
import Handlers.import_modules as func
from SEVIS_Transfers.populate_transfer_data import *
from Student_Cancellations.populate_cancel_list import *


global_menu = menu_options.GLBL_USER_CHOICE
global_main_menu = menu_options.GLBL_MAIN_USER_CHOICE
global_query_menu = menu_options.QUERY_OUTPUT


class Menu:
    """
    This class organizes the various menu options into methods and where the
    global_menu option is returned as an class attribute in each method
    """
    try:
        def __init__(self, global_menu):
            """Initializes the global_menu parameter"""
            self.global_menu = global_menu

        def run_queries(self):
            """run_queries allows the user to select select how they want
            they query to be retured """
            try:
                user_input = input(menu_options.QUERY_OUTPUT)
                if user_input == 'P'.lower():
                    func.print_query_results()
                elif user_input == 'D'.lower():
                    func.read_query_to_df()
                elif user_input == 'R'.lower():
                    func.query_results_xlsx(sheet_name=input("Please input a workbook name: "))
            except Exception as e:
                print('The following error occurred: ' + str(e))
            return global_query_menu

        def build_it_all(self):
            """
            This method is a type of a master function that runs all necessary
            functions to build populate spreadsheets, merge them into one workbook,
            and then upload them with a specified naming convention to a Google Team
            Drive
             """
            import Handlers.import_modules as func

            user_input = input(menu_options.BUILD_REG_DATA).lower()
            while user_input != 'q':
                if user_input == 'y':
                    start_time = time.time()
                    print('\nCreating data now...')
                    time.sleep(0.5)
                    print('\nBeginning data aggregation for ACTIVE Status '
                          'students...')
                    func.match_active_advisor(func.merge_active_data(),
                                              dict.ug_final_df, dict.gr_final_df)
                    func.sort_active_data()
                    func.sort_active_data()
                    print('\n*** Ran all functions for building ACTIVE student '
                          'registration notes: ***')
                    func.print_active_work_done()
                    time.sleep(1)

                    print('\nBeginning data aggregation for INITIAL Status '
                          'students...')
                    func.dataframe_difference(which=None)
                    func.match_new_advisor(func.merge_new_data(),
                        dict.ug_final_df, dict.gr_final_df)
                    func.add_advisor_notes()
                    func.sort_new_data()
                    time.sleep(0.3)

                    print('\n*** Ran all functions for building NEW student '
                    'registration notes: ***')
                    time.sleep(1)
                    func.print_new_work_done()
                    time.sleep(1)

                    time.sleep(0.6)
                    print('\nBeginning data aggregation for Cancellation Lists...')
                    time.sleep(0.5)
                    print('\nMerging UG and GR No Show reports...')
                    rename_worksheets()
                    merge_no_show_data()
                    time.sleep(0.5)
                    print('\nUG and GR No Show reports merged successfully!')
                    sort_no_show_data()
                    time.sleep(1)
                    print('Processing notes for Admissions...')
                    build_cancel_notes(dict.Cancel_SEVISID_banner,
                                            dict.Cancel_SEVISID_credits,
                                            dict.Cancel_SEVISID_SV)
                    print('\n*** Ran all functions for building Cancel List '
                    'notes: ***')
                    print_no_show_work_done()
                    time.sleep(1)

                    time.sleep(1)
                    print('\nMerging all SEVIS Registration Workbooks...')
                    func.merge_all_workbooks()
                    print('\n*** Final Workbook created titled: '
                    'SEVIS Registration ***')
                    time.sleep(0.5)
                    print('\nPreparing upload...')
                    time.sleep(1.5)
                    print('\n\nSyncing file with Google_Drive')
                    try:
                        func.drive_sheet_upload()
                        time.sleep(1.0)
                        print(f'\n** {func.uploaded_file_name} MASTER file imported '
                        f'into ISSS Team Drives folder **')
                        time.sleep(1)
                        print('\n*** DATA BUILDING AND PROCESSING COMPLETE ***')
                        print("Total Data Processing time: " + "--- %s seconds ---"
                              % (time.time() - start_time))
                    except:
                        print('An Error Occurred during the Google Drive Sync '
                              'function')

                return global_main_menu

        def sync_google_drive(self):
            """
            Menu where users can select a spreadsheet to sync with Google_Drive
            """
            user_input = input(menu_options.SYNC_GOOGLESHEETS)
            while user_input != 'q':
                if user_input == 'a':
                    func.drive_sheet_upload()
                    print('Syncing with Google_Drive')
                    time.sleep(1)
                    print(f'** {func.Registration_file} file imported in Team '
                          f'Drives folder **')
                elif user_input == 'd':
                    func.download_file()
                elif user_input == 'r':
                    func.drive_doc_upload()
                    print('Syncing with Google_Drive')
                    time.sleep(1)
                    print(f'** {func.REGISTRATION_TIMELINE} file imported in Team'
                          f' Drives folder **')

                return global_main_menu

        def sms(self):
            """
            Menu where users can select to send a text to a student or sms blast
            multiple students with custom text or pre-selected templates
            """
            user_input = input(menu_options.SMS_MESSAGE).lower()
            while user_input != 'q':
                if user_input == 's':
                    func.send_singular_sms(func.client,
                    func.get_message_content(func.content_list))
                elif user_input == 'b':
                    func.banner_query_sms_blast(func.client,
                    (func.banner_ODSP_tele(func.banner_ods_handler(),
                                           func.choose_query())),
                    func.get_message_content(func.content_list))
                elif user_input == 'cb':
                    func.send_blast_sms(func.client,
                    func.get_blast_list(func.group_list),
                    func.get_message_content(func.content_list))
                elif user_input == 'ts':
                    func.banner_query_sms_single(func.client,
                    func.get_message_content(func.content_list))
                elif user_input == 'tb':
                    func.banner_query_sms_blast(func.client,
                    (func.banner_ODSP_tele(func.banner_ods_handler(),
                                           func.choose_query())), func.get_message_content(func.content_list))
                elif user_input == 'bl':
                    func.banner_query_sms_blast(func.client,
                    (func.banner_ODSP_tele(func.banner_ods_handler(),
                                           func.choose_query())), func.get_message_content(func.content_list))

                return global_main_menu

        def emails(self):
            """
            Menu where users can elect to send emails to students
            """
            user_input = input(menu_options.EMAIL_TO_STUDENT_template).lower()
            while user_input != 'q':
                if user_input == 'e':
                    func.singular_email(
                    func.get_email_message_content(func.e_content_list))
                    time.sleep(0.5)
                elif user_input == 'm':
                    func.multiple_emails(
                    func.get_email_blast_list(func.e_group_list),
                    func.get_email_message_content(func.e_content_list))
                    time.sleep(0.5)
                elif user_input == 'es':
                    func.banner_query_singular_email(
                    func.get_email_message_content(func.e_content_list))
                elif user_input == 'eb':
                    func.banner_query_blast_email(
                    func.get_email_message_content(func.e_content_list))
                    time.sleep(0.5)
                elif user_input == 'lt':
                    func.banner_query_blast_email(
                    func.get_email_message_content(func.e_content_list))
                    time.sleep(0.5)

                return global_main_menu

        def new_menu(self):
            """
            menu where users can select a section of the
            spreadsheet to populate about new students requiring registration
             """
            user_input = input(menu_options.NEWs_USER_CHOICE)
            while user_input != 'q':
                if user_input == 'a':
                    func.match_new_advisor(merge_trans_data(),
                                           dict.gr_major_advisor_df,
                                           dict.ug_major_advisor_df)
                    func.sort_new_data()
                    time.sleep(0.3)
                    print('\n*** Ran all functions for building NEW student '
                          'registration notes: ***')
                    func.print_new_work_done()
                elif user_input == 'ad':
                    func.match_new_advisor(dict.advisor_major_ug,
                                           dict.advisor_major_gr)
                    print("Added student's advisor")

                return global_main_menu

        def active_menu(self):
            """
            menu where users can select a section of the
            spreadsheet to populate about new students requiring registration
            """
            user_input = input(menu_options.ACTIVEs_USER_CHOICE)
            while user_input != 'q':
                if user_input == 'a':
                    func.match_active_advisor(func.merge_active_data(),
                                              dict.ug_final_df,
                                              dict.gr_final_df)
                    func.sort_active_data()
                    print('\n*** Ran all functions for building ACTIVE student '
                          'registration notes: ***')
                    func.print_active_work_done()
                elif user_input == 'e':
                    func.match_active_advisor(func.merge_active_data(),
                                              dict.ug_final_df,
                                              dict.gr_final_df)

                return global_main_menu

        def cancellation_menu(self):
            """
            menu where users can merge UG and GR cancellation lists from ISSM and then
            poplate data relevant to students that haven't checked in or are not registered
            """
            user_input = input(menu_options.BUILD_CANCEL_CHOICE)
            while user_input != 'q':
                if user_input == 'a':

                    print('\nBeginning data aggregation for Cancellation Lists...')
                    time.sleep(0.5)
                    print('\nMerging UG and GR No Show reports...')
                    rename_worksheets()
                    merge_no_show_data()
                    time.sleep(0.5)
                    print('\nUG and GR No Show reports merged successfully!')
                    sort_no_show_data()
                    time.sleep(1)
                    print('Processing notes for Admissions...')
                    build_cancel_notes(dict.Cancel_SEVISID_banner,
                                            dict.Cancel_SEVISID_credits,
                                            dict.Cancel_SEVISID_SV)
                    print('\n*** Ran all functions for building Cancel List '
                          'notes: ***')
                    print_no_show_work_done()

                return global_main_menu

        def grad_menu(self):
            """
            menu where users can select a section of the
            spreadsheet to populate about graduated students
            """
            user_input = input(menu_options.GRADUATEs_USER_CHOICE)
            while user_input != 'q':
                if user_input == 'b':
                    func.build_grad_opt_status()

                return global_main_menu
    except:
        pass
