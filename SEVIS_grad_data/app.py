import os
os.getcwd()
import openpyxl
from SEVIS_grad_data.build_grad_data import ws, campusID_SEVISID, campusID_work_auth, campusID_end_date, campusID_workend, campusID_emails
from major_advisor_data import master_deg_adv, bachelor_deg_adv
from SEVIS_grad_data.build_graduated_student_data import add_advisor, match_SEVISID, add_work_type, add_emails, add_work_enddate, add_profile_enddate



"""
Build an app that allows the user to choose which spreadsheet they
want to update and what on that spreadsheet they'd like to update.

The app should have a menu asks the user what they'd like to do:

***See All Spreadsheets
***Choose a Spreadsheet
***What would you like to do with this spreadsheet
***Update A,B,C, or All
***See Menu Again
***Quit

"""

USER_CHOICE = """
Please select one of the following:
- 'a' - Run all functions
- 'ad' - Add Advisor
- 'm' - Match SEVISID with CampusID
- 'w' - Add Work Authorization Type
- 'e' - Add Work End Date
- 'p' - Add Profile End Date
- 's' - Update Cell Email
 
"""

def menu():
    """
    menu where the front-end user can select a section of the
    spreadsheet to populate
    """
    user_input = input(USER_CHOICE)
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
            user_input = input(USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(USER_CHOICE)


menu()