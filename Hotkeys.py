from prompt_toolkit import shortcuts
from pynput import keyboard
from notion import add_task

def test():
    print("event Completed bitches!!!!")

hot_keys = [
    {
        "shortcut": {keyboard.Key.ctrl_l, keyboard.Key.space},
        "event": add_task,
        "input_required": True
    },
    {
        "shortcut": {keyboard.Key.shift_l, keyboard.Key.tab},
        "event": test,
        "input_required": False
    }
]