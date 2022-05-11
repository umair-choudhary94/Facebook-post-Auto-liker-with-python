from pynput.keyboard import Key,Controller
import time
import pyautogui
keyboard = Controller()

while True:
    keyboard.press('j')
    keyboard.release('j')
    keyboard.press('l')
    pyautogui.press('enter')
    
    # time.sleep(1)