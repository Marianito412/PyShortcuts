from pynput import keyboard
from Hotkeys import hot_keys

def listener(open_ui, ui):
    combinations = hot_keys

    pressed_keys = set()

    def get_vk(key):
        # gets virtual key allowing pressed keys to easily be compared
        return key.vk if hasattr(key, 'vk') else key.value.vk

    def is_combination_pressed(combination):
        return all([get_vk(key) in pressed_keys for key in combination])

    def on_press(key):
        try:
            print("Added key")
            pressed_keys.add(get_vk(key))
        except:
            None

        for combination in combinations:  # Loop though each combination
            if is_combination_pressed(combination["shortcut"]):
                print("Got combination")
                
                
                if combination["input_required"]:
                    ui.set_event(combination["event"])
                    open_ui()
                else:
                    combination["event"]()
                

    def on_release(key):
        try:
            pressed_keys.remove(get_vk(key))
            print("Removed")
        except:
            pressed_keys.clear()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listen:
        listen.join()