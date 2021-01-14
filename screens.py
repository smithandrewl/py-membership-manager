class ScreenManager:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def start(self):
        self.initial_state.init(self)
        self.initial_state.run()


class MainScreen:
    def init(self, screen_manager):
        self.screen_manager = screen_manager

    def run(self):
        print("Main Screen")
