#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

from calc_ui import *

logging.basicConfig(level=logging.DEBUG,
                format = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt = '%a, %d %b %Y %H:%M:%S')

class Calculater(QWidget, Ui_Calculater):
    def __init__(self):
        super(Calculater, self).__init__()
        self.setupUi(self)

    def on_click(self):

        source = self.sender()
        logging.debug(source.text())

        #全部输入清零
        if source.text() == 'Clear All':
            self.display.setText('0')

        #删除最近输入的一个操作数
        elif source.text() == 'Clear':
            if self.resultflag != 1:
                clrreg = re.compile(r'[0-9.]+$')
                substr = clrreg.sub('', self.display.text())
                if substr == '':
                    substr = '0'
                self.display.setText(substr)

        #退格键功能
        elif source.text() == 'Backspace':
            if self.resultflag != 1:
                if len(self.display.text()) <= 1:
                    newtext = '0'
                else:
                    newtext = self.display.text()[0 : (len(self.display.text()) - 1)]
                self.display.setText(newtext)

        #计算输入的算术表达式并将结果显示
        elif source.text() == '=':
            if self.resultflag != 1:
                try:
                    disstr = self.display.text()[:]
                    #考虑表达式不完整的情况处理：尾部为运算符*/则补1
                    if disstr[len(disstr) - 1 : ] in '*/':
                        calstr = disstr + '1'
                    #尾部为运算符+-或小数点则补0
                    elif disstr[len(disstr) - 1 : ] in '+-.':
                        calstr = disstr + '0'
                    else:
                        calstr = disstr[:]
                    result = str(eval(calstr))
                #考虑除0异常处理
                except (ZeroDivisionError, Exception) as errinfo:
                    result = 'Error: '+ str(errinfo)
                    self.errflag = 1
                self.display.setText(result)
                self.resultflag = 1

        #输入数字或小数点：将算术表达式输入同步显示出来
        else:
            # self.numhandle()
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = Calculater()
    windows.show()
    sys.exit(app.exec_())
