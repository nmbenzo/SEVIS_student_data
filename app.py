import os
os.getcwd()
import Handlers.menus as menu
from Handlers.menus import global_menu


def main():
    """
    Master menu that allows user to select which functions they'd like to run
    """
    menu_instance = menu.Menu(global_menu)
    user_input = input(global_menu)
    while user_input != 'q':
        if user_input == 'b':
            menu_instance.build_it_all()
        elif user_input == 'f':
            menu_instance.final_build_it()
        elif user_input == 's':
            menu_instance.sync_google_drive()
        elif user_input == 'm':
            menu_instance.sms()
        elif user_input == 't':
            menu_instance.transfer_menu()
        elif user_input == 'e':
            menu_instance.emails()
        elif user_input == 'n':
            menu_instance.new_menu()
        elif user_input == 'a':
            menu_instance.active_menu()
        elif user_input == 'c':
            menu_instance.cancellation_menu()
        elif user_input == 'd':
            menu_instance.completed_menu()
        elif user_input == 'g':
            menu_instance.grad_menu()


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