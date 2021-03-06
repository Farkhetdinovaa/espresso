# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_wdg = QtWidgets.QTableWidget(self.centralwidget)
        self.table_wdg.setGeometry(QtCore.QRect(10, 10, 710, 311))
        self.table_wdg.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эспрессо"))


class Espresso(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_wdg.setColumnCount(7)
        self.table_wdg.setRowCount(4)
        self.fill_table()

    def fill_table(self):
        con = sqlite3.connect("coffee (2).sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM sorts""").fetchall()
        for i, row in enumerate(result):
            self.table_wdg.setRowCount(
                self.table_wdg.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table_wdg.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        con.close()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Espresso()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
