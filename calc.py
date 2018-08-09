#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import logging

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

from calc_ui import *

logging.basicConfig(level=logging.DEBUG,
                format = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt = '%a, %d %b %Y %H:%M:%S')

class Calculater(QWidget, Ui_Calculater):

    calcinput = ''
    displaybuffer = ''
    charbuffer = ''
    calcflag = False
    symbolflag = False

    def __init__(self):
        super(Calculater, self).__init__()
        self.setupUi(self)
        self.display('0')

    def on_click(self):

        source = self.sender()
        # logging.debug(source.text())

        #全部输入清零
        if source.text() == 'Clear All':
            self.calcflag = False
            self.symbolflag = False
            self.charbuffer = ''
            self.displaybuffer = ''
            self.calcinput = ''
            self.display('0')
        #删除最近输入的一个操作数
        elif source.text() == 'Clear':
            self.calcflag = False
            self.symbolflag = False
            self.charbuffer = ''
            self.displaybuffer = ''
            self.calcinput = ''
            self.display('0')
        #退格键功能
        elif source.text() == 'Backspace':
                self.displaybuffer = self.displaybuffer[:len(self.displaybuffer) - 1]
                self.display(self.displaybuffer)
                logging.debug(self.displaybuffer + ' ' + str(len(self.displaybuffer)))
                self.calcinput = self.calcinput[:len(self.calcinput) - 1]
        #计算输入的算术表达式并将结果显示
        elif source.text() == '=':
            self.display(self.calc(self.calcinput))
        #输入数字或小数点：将算术表达式输入同步显示出来
        else:
            self.display(self.str_handle(source.text()))
            self.calc_pre_handle(source.text())

    def str_handle(self, s):
        if s in '+-*/':
            self.symbolflag = True
            ret = self.displaybuffer
        else:
            if s in '.' and (0 == len(self.displaybuffer) or '00' == self.displaybuffer):
                self.displaybuffer = '0' + s
            else:
                if self.symbolflag == True:
                    self.symbolflag = False
                    self.displaybuffer = s
                else:
                    self.symbolflag = False
                    self.displaybuffer = self.displaybuffer + s
            ret = self.displaybuffer
        logging.debug('-->' + ret)
        return ret

    def calc_pre_handle(self, s):
        if s in '0123456789.':
            self.calcflag = True
            self.calcinput = self.calcinput + s
        elif s in '+-*/' and self.calcflag == True:
            if self.charbuffer in '+-*/':
                self.calcinput = self.calcinput[:-1] + s
            else:
                self.calcinput = self.calcinput + s
        else:
            pass
        self.charbuffer = s
        logging.debug('==>' + self.calcinput)

    def calc(self, str):
        return eval(str)

    def display(self, str):
        self.lcdNumber.display(str)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = Calculater()
    windows.show()
    sys.exit(app.exec_())
