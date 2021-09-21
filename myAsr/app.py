from PyQt5 import QtWidgets, QtGui, QtCore, uic
import re
from asrInterface import Ui_MainWindow
import sys,threading
import time
import speech_recognition as sr
import os,win32api
import pyaudio
from listenAndExecuteThread import LAEThread
orders=['open notepad','play mysic']


class myWindow(QtWidgets.QMainWindow):
    _signal=QtCore.pyqtSignal(str)         #1.定义信号,定义参数为str类型
    _signal_to_close_gif=QtCore.pyqtSignal()
    _signal_to_close_textEdit=QtCore.pyqtSignal()
    def __init__(self):
        super(myWindow, self).__init__()
        self._signal.connect(self.print)
        self._signal_to_close_gif.connect(self.close_gif)
        self._signal_to_close_textEdit.connect(self.close_text)
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._signal.emit("Hi! How can I help?")

        self._signal.emit("You can say:")
        self._signal.emit("1. Enjoy music by saying \"Play music\"")
        self._signal.emit("2. Take some notes by saying \"Open Notepad\"")


    def print(self,string):
        self.ui.textEdit.append("<font color=\"#F8F8FF\">"+string+"</font> ")

    def close_gif(self):
        self.ui.label.setVisible(False)
        self.ui.label_2.setVisible(False)
        self.ui.label_3.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.textEdit.setVisible(True)

    def close_text(self):
        self.ui.label.setVisible(True)
        self.ui.label_2.setVisible(True)
        self.ui.label_3.setVisible(True)
        self.ui.label_4.setVisible(True)
        self.ui.textEdit.setVisible(False)


#命令关键词
orderlist=['网易云',"记事本"]

#程序地址
exelist=['Y:\Z\CloudMusic\cloudmusic.exe','E:\\song.txt']


if __name__=='__main__':
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
   #
    application._signal_to_close_gif.emit()
    #application._signal_to_close_textEdit.emit()
    listenAndHandler=LAEThread()
    listenAndHandler.bind_window(application)
    listenAndHandler.bind_orderlist(orderlist)
    listenAndHandler.bind_orderaddlist(exelist)
    listenAndHandler.start()
    sys.exit(app.exec())

