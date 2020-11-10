import os
os.getcwd()
from Handlers.menus import Menu, global_main_menu, global_menu


def main():
    """
    Master menu that allows user to select which functions they'd like to run
    """
    menu_instance = Menu(global_menu)
    user_input = input(global_menu).lower()
    if user_input == 'M'.lower():
        def main_menu():
            user_input = input(global_main_menu).lower()
            if user_input == 'b':
                menu_instance.build_it_all()
            elif user_input == 's':
                menu_instance.sync_google_drive()
            elif user_input == 'm':
                menu_instance.sms()
            elif user_input == 'e':
                menu_instance.emails()
            elif user_input == 'n':
                menu_instance.new_menu()
            elif user_input == 'a':
                menu_instance.active_menu()
            elif user_input == 'c':
                menu_instance.cancellation_menu()
            elif user_input == 'g':
                menu_instance.grad_menu()
            menu_again = input('\nWould you like to see the menu again? (y/n): ')
            if menu_again == 'y':
                main()
            elif menu_again == 'n':
                quit()
            else:
                print('Unknown command.')
                main()
        return main_menu()
    elif user_input == 'R'.lower():
        def query_menu():
            menu_instance.run_queries()
            menu_again = input('\nWould you like to see the menu again? (y/n): ')
            if menu_again == 'y':
                main()
            elif menu_again == 'n':
                quit()
            else:
                print('Unknown command.')
                main()
        return query_menu()
    else:
        print('Unknown command.')
        main()
    return global_menu

if __name__ == '__main__':
    main()