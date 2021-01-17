
import db

from screens import ScreenManager, MainScreen

if __name__ == '__main__':
    db.create_db()
    screen_manager = ScreenManager(MainScreen())
    screen_manager.start()
