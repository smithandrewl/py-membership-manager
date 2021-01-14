import db


class ScreenManager:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def start(self):
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
        self.display_menu()

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
            elif choice == "2":
                print("You selected option 2")
            else:
                print("Invalid selection")

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


        club_name = db.ClubDAO.get_club_name()

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
