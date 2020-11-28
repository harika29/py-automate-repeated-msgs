import pyautogui
import time

while True:
    time.sleep(3)
    # writes at the current mouse pointer position
    pyautogui.typewrite("Hey Buddy, Good Morning!!")
    pyautogui.press('enter')