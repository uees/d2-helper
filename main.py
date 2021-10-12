import keyboard

from state import state
from hotkey import MoveHotkey, SkillsHotkey
from logger import logger
from settings import HOT_KEY


class Bot(object):

    def __init__(self):
        self.mk = MoveHotkey()
        self.sk = SkillsHotkey()

    def start(self):
        keyboard.add_hotkey(HOT_KEY, self.handle, args=(self.mk, self.sk))

    def restart(self):
        keyboard.unhook_all()
        self.start()

    def run(self):
        self.start()
        keyboard.wait()

    def handle(self, mk: MoveHotkey, sk: SkillsHotkey):
        if not state.is_running:
            mk.register_hotkeys()
            sk.register_hotkeys()
        else:
            self.restart()

        state.toggle()
        logger.info(f"脚本启用状态：{state.is_running}")


if __name__ == "__main__":
    Bot().run()
