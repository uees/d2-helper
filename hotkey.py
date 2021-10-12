import time
import keyboard
import mouse

from state import state
from settings import SKILLS
from logger import logger


class SkillsHotkey:
    def register_hotkeys(self):
        for index, skill in enumerate(SKILLS):
            keyboard.add_hotkey(str(index), self.handle, args=(skill, str(index)))
            logger.info(f"Hotkey `{index}` was successfully registered.")

    @staticmethod
    def handle(skill, index):
        """
        实现按键之后的功能
        :return:
        """
        if state.binding_right != index and state.binding_left != index:
            time.sleep(.01)

        if skill["bind"] == mouse.LEFT:
            state.binding_left = index
        else:
            state.binding_right = index

        mouse.click(skill["bind"])

        logger.info(f"释放了技能: {skill['name']}")
        logger.info(state)


class MoveHotkey:

    def register_hotkeys(self):
        keyboard.on_press_key('x', self.handle_press)
        keyboard.on_release_key('x', self.handle_release)
        logger.info("Hotkey `x` was successfully registered.")

    @staticmethod
    def handle_press(event: keyboard.KeyboardEvent):
        mouse.press(mouse.LEFT)

    @staticmethod
    def handle_release(event: keyboard.KeyboardEvent):
        mouse.release(mouse.LEFT)
