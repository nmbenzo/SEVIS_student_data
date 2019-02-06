import os
os.getcwd()

from Handlers.menus import *


def main():
    """
    Master menu that allows user to select which spreadsheet they'd like to run
    """
    user_input = input(GLBL_USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            build_it_all(GLBL_USER_CHOICE)
        if user_input == 'f':
            final_build_it(GLBL_USER_CHOICE)
        if user_input == 'n':
            new_menu(GLBL_USER_CHOICE)
        if user_input == 'a':
            active_menu(GLBL_USER_CHOICE)
        if user_input == 'c':
            cancellation_menu(GLBL_USER_CHOICE)
        if user_input == 'd':
            completed_menu(GLBL_USER_CHOICE)
        if user_input == 'g':
            grad_menu(GLBL_USER_CHOICE)
        if user_input == 's':  # for google sheets
            sync_googlesheets(GLBL_USER_CHOICE)
        if user_input == 't':
            transfer_menu(GLBL_USER_CHOICE)
        if user_input == 'e':  # to send emails
            emails(GLBL_USER_CHOICE)

        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input(GLBL_USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(GLBL_USER_CHOICE)


if __name__ == '__main__':
    main()