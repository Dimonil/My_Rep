# This is a sample Python script.
import time
from PyQt5 import uic, QtWidgets
import sys
from PyQt5 import QtCore
import game
inc_array = ['\t', '\n', '\r', ' ', '!', '"', '#', '/', '\\']
key_array = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
             ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
             '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
             'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
             'browserback', 'browserfavorites', 'browserforward', 'browserhome',
             'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
             'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
             'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
             'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
             'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
             'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
             'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
             'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
             'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
             'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
             'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
             'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
             'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
             'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
             'command', 'option', 'optionleft', 'optionright']


Form, _ = uic.loadUiType('interface.ui')


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res

    return tmp


class Config():
    def __init__(self):
        self.key = ''
        self.button_eat = ''
        self.button_bait = ''
        self.size_hook = 13
        self.accuracy = 10
        self.wait_eat = 0
        self.wait_bait = 0
        self.timer_bait = 5
        self.percent = 0.7
        self.zone_hook = 180
        self.timer_bot = 0
        self.eat_bool = False
        self.bait_bool = False
        self.timer_bool = False
        self.geteat = False
        self.getbait = False

    def getConfig(self):
        f = open('config.txt', 'r')
        for i in f:

            if i.find('button_eat') != -1:
                self.button_eat = i[11::1].strip()
            if i.find('button_bait') != -1:
                self.button_bait = i[12::1].strip()
            if i.find('size_hook') != -1:
                self.size_hook = int(i[10::].strip())
            if i.find('accuracy') != -1:
                self.accuracy = float(i[9::].strip())
            if i.find('wait_eat') != -1:
                self.wait_eat = int(i[9::].strip())
            if i.find('wait_bait') != -1:
                self.wait_bait = int(i[10::].strip())
            if i.find('timer_bait') != -1:
                self.timer_bait = int(i[11::].strip())
            if i.find('percent') != -1:
                self.percent = float(i[8::].strip())
            if i.find('zone_hook') != -1:
                self.zone_hook = int(i[10::].strip())
            if i.find('timer_bot') != -1:
                self.timer_bot = int(i[10::].strip())

            if i.find('eat_bool') != -1:
                if i.find('True') != -1:
                    self.eat_bool = True
                else:
                    self.eat_bool = False

            if i.find('get_eat') != -1:
                if i.find('True') != -1:
                    self.geteat = True
                else:
                    self.geteat = False

            if i.find('get_bait') != -1:
                if i.find('True') != -1:
                    self.getbait = True
                else:
                    self.getbait = False

            if i.find('bait_bool') != -1:
                if i.find('True') != -1:
                    self.bait_bool = True
                else:
                    self.bait_bool = False

            if i.find('timer_bool') != -1:
                if i.find('True') != -1:
                    self.timer_bool = True
                else:
                    self.timer_bool = False



    def printConfig(self):
        print(self.key, self.button_eat, self.button_bait, self.size_hook, self.accuracy, self.wait_eat, self.wait_bait
              ,self.timer_bait, self.percent, self.zone_hook, self.timer_bot, self.eat_bool, self.bait_bool,
              self.timer_bool)


class Ui(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.thread = QtCore.QThread()
        self.game = game.Game()
        self.config = Config()
        self.setConfig()
        self.game.moveToThread(self.thread)
        self.thread.started.connect(self.game.run)
        self.thread.start()
        self.start.clicked.connect(self.StartPressed)
        self.stop.clicked.connect(self.StopPressed)
        self.settings.clicked.connect(self.ConfirmSettings)

    def setConfig(self):
        self.config.getConfig()
        self.spinBox.setValue(self.config.size_hook)
        self.key_bait.setPlainText(self.config.button_eat)
        self.key_eat.setPlainText(self.config.button_bait)
        self.SpinBox_hook.setValue(self.config.accuracy)
        self.wait_bait.setValue(self.config.wait_bait)
        self.wait_eat.setValue(self.config.wait_eat)
        self.spinBox_2.setValue(self.config.timer_bait)
        self.spinBox_3.setValue(self.config.zone_hook)
        self.SpinBox_percent_find.setValue(self.config.percent)
        self.timerWork.setValue(self.config.timer_bot)
        self.bait.setChecked(self.config.bait_bool)
        self.eat.setChecked(self.config.eat_bool)
        self.timer_activate.setChecked(self.config.timer_bool)
        self.geteat.setChecked(self.config.geteat)
        self.getbait.setChecked(self.config.getbait)


    def keyPressEvent(self, e):
        y = e.key()
        if y == QtCore.Qt.Key_Escape:
            self.close()

        if y < 2000:
            x = chr(y).lower()

            if x == 'z' or x == 'я':
                self.start.setEnabled(True)
                self.stop.setEnabled(False)
                self.game.stop = True

            if x == 'ч' or x == 'x':
                self.game.stop = False
                self.stop.setEnabled(True)
                self.start.setEnabled(False)

    def StartPressed(self):
        self.stop.setEnabled(True)
        self.start.setEnabled(False)
        self.game.stop = False

    def StopPressed(self):
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self.game.stop = True

    def ConfirmSettings(self):
        self.game.zonex = self.spinBox_3.value()
        self.game.hook_rad = self.spinBox.value()
        self.game.eat = self.eat.isChecked()
        self.game.bait = self.bait.isChecked()
        self.game.isgetBait = self.getbait.isChecked()
        self.game.isgetEat = self.geteat.isChecked()
        self.game.wait_eat = self.wait_eat.value()
        self.game.wait_bait = self.wait_bait.value()
        self.game.i_click = self.SpinBox_hook.value()
        self.game.time_bait = self.spinBox_2.value()
        self.game.percent_find = self.SpinBox_percent_find.value()

        if self.timer_activate.isChecked():
            self.game.time_bot_exit += self.timerWork.value()
            self.game.bot_exit = True

        self.lineEdit.setText('')
        if self.key_bait.toPlainText().lower() in key_array:
            self.game.key_bait = self.key_bait.toPlainText().lower()
        else:
            if self.key_bait.toPlainText().lower() != '':

                self.lineEdit.setText(f'{self.key_bait.toPlainText()} не может быть клавишей; {self.lineEdit.text()}')

        if self.key_eat.toPlainText().lower() in key_array:
            self.game.key_eating = self.key_eat.toPlainText().lower()
        else:
            if self.key_eat.toPlainText().lower():
                self.lineEdit.setText(f'{self.key_eat.toPlainText()} не может быть клавишей; {self.lineEdit.text()}')


def ma():
    app = QtWidgets.QApplication(sys.argv)
    z = Ui()
    z.show()
    sys.exit(app.exec_())





