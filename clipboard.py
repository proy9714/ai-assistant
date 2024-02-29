from pynput.keyboard import Key, Controller
import pyperclip
import time

controller = Controller()

def get_selection() -> str:
    # 1. Copy to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')
        
    # Give some time to copy to clipboard
    time.sleep(0.1)
        
    # 2. Get text from clipboard
    clipboard_text = pyperclip.paste()
    
    return clipboard_text

def get_line_selection() -> str:
    # Simulate pressing and holding the Home key
    with controller.pressed(Key.home):
        # Simulate pressing and releasing the Shift and End keys
        controller.press(Key.shift)
        controller.press(Key.end)
        controller.release(Key.shift)
        controller.release(Key.end)
                
    clipboard_text = get_selection()
    
    return clipboard_text

def get_all_selection() -> str:
    # Simulate pressing and holding the Home key
    with controller.pressed(Key.ctrl):
        controller.tap('a')
                
    clipboard_text = get_selection()
    
    return clipboard_text

def replace_selection(text: str):
    # 1. Set clipboard text
    pyperclip.copy(text)
    
    # 2. Paste
    with controller.pressed(Key.ctrl):
        controller.tap('v')
    