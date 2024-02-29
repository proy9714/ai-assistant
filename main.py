from dotenv import load_dotenv
from clipboard import get_selection, get_line_selection, replace_selection, get_all_selection
from pynput import keyboard
from llm import get_corrected_text

# Loading env variables
load_dotenv()

# Hotkey functions
def handle_selection(get_text_fn):
    text = get_text_fn()
    print("Received selection...")
    corrected_text = get_corrected_text(text)
    print("Corrected text...")
    replace_selection(corrected_text)
    print("Replaced selection!")

# Main loop
def main():
    with keyboard.GlobalHotKeys({
            # f2
            '<113>': lambda: handle_selection(get_selection),
            # f4
            '<115>': lambda: handle_selection(get_line_selection),
            # f6
            '<117>': lambda: handle_selection(get_all_selection)
    }) as h:
        h.join()

if __name__ == "__main__":
    main()
