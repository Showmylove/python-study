#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

from calc_ui import *

class MainWindow(QWidget, Ui_Calc):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def click_one(self):
        # QtWidgets.QMessageBox.information(self.pushButton,"标题","这是第一个PyQt5 GUI程序")
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())