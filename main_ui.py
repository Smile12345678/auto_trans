# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.zhBtn = QtWidgets.QPushButton(self.centralwidget)
        self.zhBtn.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.zhBtn.setObjectName("zhBtn")
        self.enBtn = QtWidgets.QPushButton(self.centralwidget)
        self.enBtn.setGeometry(QtCore.QRect(200, 110, 75, 23))
        self.enBtn.setObjectName("enBtn")
        self.jpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.jpBtn.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.jpBtn.setObjectName("jpBtn")
        self.xmlBtn = QtWidgets.QPushButton(self.centralwidget)
        self.xmlBtn.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.xmlBtn.setObjectName("xmlBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "donate"))
        self.zhBtn.setText(_translate("MainWindow", "中文xls"))
        self.enBtn.setText(_translate("MainWindow", "英文xls"))
        self.jpBtn.setText(_translate("MainWindow", "日文xls"))
        self.xmlBtn.setText(_translate("MainWindow", "回刷xml"))

