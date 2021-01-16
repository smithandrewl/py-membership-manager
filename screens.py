
from db import *


class ScreenManager:
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


class MembersScreen:
    def init(self, screen_manager):
        self.screen_manager = screen_manager

    def display_menu(self):
        print(
            "\n".join(
                [
                    "Members screen!",
                    " Please enter a number:",
                    " 1. List all members",
                    " 2. Add a member",
                    " 3. Delete a member",
                    " 4. Return to the main menu"
                ]
            )
        )

    def run(self):
        while(True):
            self.display_menu()

            choice = input()

            if choice == "4":
                self.screen_manager.change_screen(MainScreen())
            else:
                print("Option not implemented yet")
class MainScreen:
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
                print("You selected 'Classes'")
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
