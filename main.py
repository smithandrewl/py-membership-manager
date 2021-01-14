# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import db

# Press the green button in the gutter to run the script.
from screens import ScreenManager, MainScreen

if __name__ == '__main__':
    screen_manager = ScreenManager(MainScreen())
    screen_manager.start()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
