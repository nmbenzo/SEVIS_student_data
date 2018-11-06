from import_app_modules import *


def new_menu():
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
        elif user_input == 'ad':
            match_advisor(advisor_major_ug, advisor_major_gr)
        elif user_input == 'm':
            match_SEVISID(campusID_SEVISID)
        elif user_input == 'w':
            match_major_data(SEVISID_major)
        elif user_input == 'n':
            add_advisor_notes()
        else:
            print('Unknown command.')

        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input(NEWs_USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(NEWs_USER_CHOICE)



def active_menu():
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
        elif user_input == 'm':
            match_SEVISID(campusID_SEVISID)
        elif user_input == 'w':
            match_major_data(SEVISID_major)
        elif user_input == 'e':
            match_advisor(advisor_major_ug, advisor_major_gr)
        else:
            print('Unknown command.')

        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input(ACTIVEs_USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(ACTIVEs_USER_CHOICE)


def grad_menu():
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
        elif user_input == 'ad':
            add_advisor(master_deg_adv, bachelor_deg_adv)
        elif user_input == 'm':
            match_SEVISID(campusID_SEVISID)
        elif user_input == 'w':
            add_work_type(campusID_work_auth)
        elif user_input == 'e':
            add_work_enddate(campusID_workend)
        elif user_input == 'p':
            add_profile_enddate(campusID_end_date)
        elif user_input == 's':
            add_emails(campusID_emails)
        else:
            print('Unknown command. Please select a valid option')

        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input(GRADUATEs_USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(GRADUATEs_USER_CHOICE)

