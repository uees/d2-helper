import keyboard


def callback(e: keyboard.KeyboardEvent):
    print(e.name, e.scan_code)


keyboard.hook(callback)

keyboard.wait('esc')
