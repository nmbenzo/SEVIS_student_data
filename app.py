import os
os.getcwd()

from menus import *


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


def global_choose_menu():
    """
    Master menu that allows user to select which spreadsheet they'd like to run
    """
    user_input = input('Please choose a menu: ')
    while user_input != 'q':
        if user_input == 'a':
            active_menu()
        elif user_input == '':
            new_menu()
        elif user_input == '':
            grad_menu()
        else:
            print('Unknown command.')

        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input('Please choose a menu: ')
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input('Please choose a menu: ')


global_choose_menu()