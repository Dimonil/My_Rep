import pyautogui
import time
x_bait = (1600,555)

def getBait():
    pyautogui.press('i')
    pyautogui.moveTo(*x_bait, 1)
    pyautogui.rightClick()
    pyautogui.press('i')

time.sleep(3)
getBait()