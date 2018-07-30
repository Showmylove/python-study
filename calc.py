#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

from calc_ui import *

class Calculater(QWidget, Ui_Calc):
    def __init__(self):
        super(Calculater, self).__init__()
        self.setupUi(self)

    def on_click(self):
        print('click')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = Calculater()
    windows.show()
    sys.exit(app.exec_())
