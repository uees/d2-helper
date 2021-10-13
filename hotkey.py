import time
import keyboard
import mouse

from state import state
from settings import SKILLS
from logger import logger


class SkillsHotkey:
    """
    快捷施法的实现
    """

    def register_hotkeys(self):
        for skill in SKILLS:
            keyboard.add_hotkey(skill['key_code'], self.handle, args=(skill, ))
            logger.info(f"Hotkey `{skill['key_code']}` was successfully registered.")

    @staticmethod
    def handle(skill: dict):
        """
        实现按键之后的功能
        :return:
        """
        if state.binding_right != skill['key_code'] and state.binding_left != skill['key_code']:
            time.sleep(.01)

        # 绑定左右键技能信息
        if skill["bind"] == mouse.LEFT:
            state.binding_left = skill['key_code']
        else:
            state.binding_right = skill['key_code']

        # 释放技能
        mouse.click(skill["bind"])

        logger.info(f"释放了技能: {skill['name']}")


class MoveHotkey:
    """
    按 x 强制移动的实现
    """

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
