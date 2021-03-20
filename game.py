import pyautogui
import time
import numpy
from PIL import ImageGrab
import keyboard
import cv2
from PyQt5 import QtCore
import datetime

size_screen = pyautogui.size()
if size_screen == (1600, 900):
    x0, y0 = (700, 450), (900, 470)
    abs_i = 150

elif size_screen == (1920, 1080):
    x0, y0 = (840, 539), (1080, 569)
    x_bait = (1600,555)
    y_bait = (1660,555)
    abs_i = 180
elif size_screen == (1366, 768):
    x0, y0 = (575, 380), (790, 407)
    abs_i = 160
elif size_screen == (1280, 720):
    x0, y0 = (540, 360), (740, 380)
    abs_i = 150
else:
    x0, y0 = (840, 539), (1080, 569)
    x_bait = (1600, 555)
    y_bait = (1660, 555)
    abs_i = 180


class Game(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.stop = True
        self.count_eat = 0
        self.count_bait = 0
        self.hook_rad = 13
        self.time_eat = 30
        self.time_bait = 10
        self.eat, self.bait, self.isgetBait, self.isgetEat = False, False, False, False
        self.wait_eat, self.wait_bait = 0, 0
        self.stop_wait_eat, self.stop_wait_bait = True, True
        self.key_eating, self.key_bait = 'f2', 'f1'
        self.i_click = 5
        self.hook = cv2.cvtColor(cv2.imread('hook.png', 0), cv2.COLOR_BAYER_BG2GRAY)
        self.percent_find = 0.7
        self.zonex = abs_i
        self.bot_exit = False
        self.time_bot_exit = self.cur_min()

    def bot_exiting(self):
        if self.bot_exit and self.cur_min() >= self.time_bot_exit:
            self.stop = True
            return True
        else:
            return False

    def catch(self):
        time.sleep(0.1)
        count_fail = 0

        for i in range(1000):
            if self.stop:
                return

            ImageGrab.grab(bbox=(*x0, *y0)).save('hook_screen.png')
            hook_sg = cv2.cvtColor(cv2.imread('hook_screen.png', 0), cv2.COLOR_BAYER_BG2GRAY)

            res = cv2.matchTemplate(hook_sg, self.hook, cv2.TM_CCOEFF_NORMED)
            loc = numpy.where(res >= self.percent_find)

            try:
                a = int(numpy.max(loc[-1]))

                if a < self.zonex:

                    pyautogui.mouseDown(button='left')

                else:
                    pyautogui.mouseUp(button='left')

                count_fail = 0
            except:
                #print('Не вижу крючка')
                pyautogui.mouseUp(button='left')

                count_fail += 1
                if count_fail >= 7:
                    return

    def cur_min(self):
        x = datetime.datetime.now()

        return int(x.hour * 60 + x.minute + x.year * 365 * 24 + x.day * 24 * 60 + x.month * 30 * 24 * 60)

    def getBait(self):
        if self.isgetBait:
            pyautogui.press('i')
            time.sleep(0.5)
            pyautogui.moveTo(*y_bait)
            pyautogui.rightClick()
            time.sleep(0.5)
            pyautogui.press('i')

    def getEat(self):
        if self.isgetEat:
            pyautogui.press('i')
            time.sleep(0.5)
            pyautogui.moveTo(*x_bait)
            pyautogui.rightClick()
            time.sleep(0.5)
            pyautogui.press('i')

    def eating(self, first_time):
        if self.stop_wait_eat:
            if self.eat and self.cur_min() - first_time >= self.wait_eat:
                pyautogui.press(self.key_eating)
                self.wait_eat = 0
                self.stop_wait_eat = False
                self.count_eat+=1
                time.sleep(2)
                return True
            else:
                return False
        else:

            if self.eat and self.cur_min() - first_time >= self.time_eat:
                pyautogui.press(self.key_eating)
                self.wait_eat = 0
                time.sleep(2)
                self.count_eat += 1
                if self.count_eat >=5:
                    self.getEat()
                    self.count_eat = 0
                return True
            else:
                return False

    def baiting(self, first_time):
        if self.stop_wait_bait:
            if self.bait and self.cur_min() - first_time >= self.wait_bait:
                pyautogui.press(self.key_bait)
                self.wait_bait = 0
                self.stop_wait_bait = False
                time.sleep(1)
                self.count_bait+=1
                return True
            else:
                return False
        else:

            if self.bait and self.cur_min() - first_time >= self.time_bait:
                pyautogui.press(self.key_bait)
                self.wait_bait = 0
                time.sleep(1)
                self.count_bait += 1
                if self.count_bait >= 5:
                    self.getBait()
                    self.count_bait = 0
                return True
            else:
                return False

    def throw_a_hook(self, x, y):
        pyautogui.moveTo(x, y, 0.5)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.mouseUp(button='left')

    def wait(self):
        keyboard.wait('l')
        return pyautogui.position()

    def click_on_hook(self, x, y):
        zero_count = 0
        array = [numpy.mean(
            ImageGrab.grab(bbox=(x - self.hook_rad, y - self.hook_rad, x + self.hook_rad, y + self.hook_rad)))]

        for i in range(1000):
            if self.stop:
                return

            clean_screen = ImageGrab.grab(
                bbox=(x - self.hook_rad, y - self.hook_rad, x + self.hook_rad, y + self.hook_rad))

            mean = numpy.mean(clean_screen)
            diff = abs(array[-1] - mean)
            #print(round(diff, 3))
            array.append(mean)

            if diff >= self.i_click:

                pyautogui.click()
                return False

            if diff < 0.1:
                zero_count += 1
            else:
                zero_count = 0
            if zero_count >= 10:
                return True

    def run(self):
        while True:
            if self.bot_exiting():
                pyautogui.hotkey('alt', 'f4')
                break

            first_time_eat = self.cur_min()
            first_time_bait = self.cur_min()

            while self.stop:
                if self.bot_exiting():
                    break
                time.sleep(1)

            while 1:
                if self.bot_exiting():
                    break
                if self.stop:
                    break
                bool_repeat = False
                coord0 = self.wait()
                coord1 = self.wait()
                self.wait()
                time.sleep(0.1)
                if bool_repeat:
                    bool_repeat = False

                while True:
                    if self.bot_exiting():
                        break

                    if self.eating(first_time_eat):
                        first_time_eat = self.cur_min()
                    if self.baiting(first_time_bait):
                        first_time_bait = self.cur_min()

                    if self.stop:
                        break

                    bool_repeat = False

                    self.throw_a_hook(*coord0)
                    if self.stop:
                        break
                    time.sleep(1.5)

                    bool_repeat = self.click_on_hook(*coord1)
                    if self.stop:
                        break
                    if bool_repeat:
                        continue

                    time.sleep(0.1)
                    self.catch()
                    if self.stop:
                        break
                    time.sleep(2)
