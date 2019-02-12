import os
os.getcwd()
import Handlers.menu_selection_options as menu_options
import Handlers.menus as menu

global_menu = menu_options.GLBL_USER_CHOICE


def main():
    """
    Master menu that allows user to select which spreadsheet they'd like to run
    """
    user_input = input(global_menu)
    while user_input != 'q':
        if user_input == 'b':
            menu.build_it_all(global_menu)
        if user_input == 'f':
            menu.final_build_it(global_menu)
        if user_input == 's':  # for google sheets
            menu.sync_googlesheets(global_menu)
        if user_input == 'm':
            menu.sms(global_menu)
        if user_input == 't':
            menu.transfer_menu(global_menu)
        if user_input == 'e':  # to send emails
            menu.emails(global_menu)
        if user_input == 'n':
            menu.new_menu(global_menu)
        if user_input == 'a':
            menu.active_menu(global_menu)
        if user_input == 'c':
            menu.cancellation_menu(global_menu)
        if user_input == 'd':
            menu.completed_menu(global_menu)
        if user_input == 'g':
            menu.grad_menu(global_menu)


        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input(global_menu)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(global_menu)


if __name__ == '__main__':
    main()