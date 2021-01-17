
from db import *


class ScreenManager:
    """
    This class manages the screens that can be accessed and displays
    the current screen.
    """
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def start(self):
        self.initial_state.init(self)
        self.initial_state.run()

    def change_screen(self, new_screen):
        self.initial_state = new_screen
        self.initial_state.init(self)
        self.initial_state.run()


class AdminScreen:
    """
    Implements the Admin menu screen.
    """
    def init(self, screen_manager):
        self.screen_manager = screen_manager

    def display_menu(self):
        print(
            "\n".join([
                "Admin screen!",
                "Please enter a number:",
                "1. Change the club name",
                "2. Return to the main menu"
            ])
        )

    def run(self):
        while(True):
            self.display_menu()
            choice = input()
            if choice == "1":
                new_name = input("Please enter the new name:")

                ClubDAO.change_club_name(new_name)
            elif choice == "2":
                self.screen_manager.change_screen(MainScreen())
            else:
                print('Error: Please enter a valid option!')


class ClassesScreen:
    """
    Implements the Classes menu screen.
    """
    def init(self, screen_manager):
        self.screen_manager = screen_manager

    def display_menu(self):
        print(
            "\n".join(
                [
                    "Classes screen!",
                    "Please enter a number:",
                    "1. List classes",
                    "2. Add a class",
                    "3. Return to the main menu",
                ]
            )
        )

    def run(self):
        while(True):
            self.display_menu()

            choice = input()

            if choice == "1":
                classes = ClassesDAO.get_classes()

                if classes.count() == 0:
                    print("There are no classes")
                else:
                    print()
                    print("Classes:")
                    for a_class in classes:
                        print("\t{0} ({1})".format(a_class.name, a_class.description))

                    print("\n")
            elif choice == "2":
                print("Please enter the class name")
                name = input()
                print("Please enter a class description")
                description = input()
                ClassesDAO.add(name, description, ClubDAO.get_club().club_id)
            elif choice == "3":
                self.screen_manager.change_screen(MainScreen())
            else:
                print("Option not implemented yet")


class MembersScreen:
    """
    Provides the functionality of the Member screen.
    """
    def init(self, screen_manager):
        self.screen_manager = screen_manager

    def display_menu(self):
        print(
            "\n".join(
                [
                    "Please enter a number:",
                    "1. List all members",
                    "2. Add a member",
                    "3. Delete a member",
                    "4. Return to the main menu"
                ]
            )
        )

    def run(self):
        print("Members screen!")
        while(True):
            self.display_menu()

            choice = input()
            if choice == "1":
                members = MembersDAO.get_all()

                print("\n")

                if members.count() == 0:
                    print("There are currently no members!")
                else:
                    print("Members:")
                    for member in members:
                        print("\t#{0} {1}, {2}".format(member.member_id, member.firstname, member.lastname))
                print("")
            elif choice == "2":

                print("Adding a new member:")
                print("Please enter a first name")

                first_name = input()
                print("Please enter a last name")
                last_name = input()

                MembersDAO.add_member(firstname=first_name, lastname=last_name)
            elif choice == "3":
                print("Delete a member")
                print("Please enter the id of the member to delete")

                number = input()

                if not number.isnumeric():
                    print("Please enter a valid number!")
                else:
                    if MembersDAO.exists(number):
                        MembersDAO.delete(number)
                    else:
                        print("There is no user with an id of {0}".format(number))

            elif choice == "4":
                self.screen_manager.change_screen(MainScreen())
            else:
                print("Error: Please enter a valid option!")


class MainScreen:
    """
    The main menu screen.

    The main menu screen displays a menu. Each selection from the main menu
    hands control to a different screen.  Selecting 1. for Admin, would
    hand control to the AdminScreen class.
    """
    def init(self, screen_manager):
        self.screen_manager = screen_manager

    def run(self):
        self.display_banner()

        while(True):
            self.display_menu_prompt()
            choice = input()

            if choice == "1":
                print("You selected option 1")
                self.screen_manager.change_screen(AdminScreen())
            elif choice == "2":
                self.screen_manager.change_screen(MembersScreen())
            elif choice == "3":
                self.screen_manager.change_screen(ClassesScreen())
            elif choice == "4":
                import sys
                sys.exit()
            else:
                print("Error: Please enter a valid option!")

    def display_banner(self):
        print(
            "\n".join(
                [
                    "                       _                   _     _              ",
                    "  /\\/\\   ___ _ __ ___ | |__   ___ _ __ ___| |__ (_)_ __       ",
                    " /    \\ / _ \\ '_ ` _ \\| '_ \\ / _ \\ '__/ __| '_ \\| | '_ \\ ",
                    "/ /\\/\\ \\  __/ | | | | | |_) |  __/ |  \\__ \\ | | | | |_) |  ",
                    "\\/    \\/\\___|_| |_| |_|_.__/ \\___|_|  |___/_| |_|_| .__/    ",
                    "                                                  |_|           ",
                    "                                                                ",
                    "       /\\/\\   __ _ _ __   __ _  __ _  ___ _ __                ",
                    "      /    \\ / _` | '_ \\ / _` |/ _` |/ _ \\ '__|              ",
                    "     / /\\/\\ \\ (_| | | | | (_| | (_| |  __/ |                 ",
                    "     \\/    \\/\\__,_|_| |_|\\__,_|\\__, |\\___|_|              ",
                    "                           |___/ "
                ]
            )
        )

    def display_menu_prompt(self):
        club_name = ClubDAO.get_club_name()

        print(
            "\n".join(
                [
                    "Welcome to club '" + club_name + "' Please enter a number:",
                    "1. Administration",
                    "2. Members",
                    "3. Classes",
                    "4. Exit"
                ]
            )
        )
