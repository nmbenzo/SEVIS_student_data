import os
os.getcwd()

from menus import *


"""
---Notes---
An app that allows the user to choose which spreadsheet they
want to update and what on that spreadsheet they'd like to update.
The app should have a menu asks the user what they'd like to do:
***See All Spreadsheets
***Choose a Spreadsheet
***What would you like to do with this spreadsheet
***Update A,B,C, or All
***See Menu Again
***Upload to GS
***Quit

---Future Development---
***Add logging 
***Add threading and async to improve performance

"""



def global_choose_menu():
    """
    Master menu that allows user to select which spreadsheet they'd like to run
    """
    user_input = input(GLBL_USER_CHOICE)
    while user_input != 'q':
        if user_input == 'n':
            new_menu()
        if user_input == 'a':
            active_menu()
        if user_input == 'g':
            grad_menu()
        if user_input == 'gs':  # for google sheets
            pass
        else:
            print('Unknown command.')


        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input(GLBL_USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(GLBL_USER_CHOICE)


global_choose_menu()