from pynput import keyboard, mouse
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

# Initialize controllers
keyboard_controller = KeyboardController()
mouse_controller = MouseController()

# Function to execute the macro
def execute_macro():
    try:
        # Press and release '3'
        keyboard_controller.press('3')
        time.sleep(0.01)  # 10 ms
        keyboard_controller.release('3')
        time.sleep(0.5)  # 500 ms

        # Press and release 'space'
        keyboard_controller.press(Key.space)
        time.sleep(0.01)  # 10 ms
        keyboard_controller.release(Key.space)
        time.sleep(0.01)  # 10 ms

        # Left click
        mouse_controller.press(Button.left)
        time.sleep(0.01)  # 10 ms
        mouse_controller.release(Button.left)
        time.sleep(0.025)  # 25 ms

        # Press and release 'space'
        keyboard_controller.press(Key.space)
        time.sleep(0.025)  # 25 ms
        keyboard_controller.release(Key.space)
        time.sleep(0.025)  # 25 ms

        # Press and release 'F'
        keyboard_controller.press('f')
        time.sleep(0.025)  # 25 ms
        keyboard_controller.release('f')
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to listen for the 'Page Down' key press
def on_press(key):
    try:
        if key == Key.page_down:
            execute_macro()
    except AttributeError:
        pass

# Main function to set up the listener
def main():
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
