class BotState(object):
    def __init__(self, name: str, is_running: bool):
        self.name = name
        self.is_running = is_running
        self.binding_left = None
        self.binding_right = None

    def __str__(self):
        return f"<BotState(name: {self.name}, is_running: {self.is_running}, binding_left: {self.binding_left}, binding_right:{self.binding_right})>"

    def toggle(self):
        self.is_running = not self.is_running


state = BotState("default", False)
