# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui',
# licensing of 'window.ui' applies.
#
# Created: Fri Dec 27 15:10:52 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(164, 127)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(120, 10, 25, 25))
        self.toolButton.setObjectName("toolButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 141, 41))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_current = QtWidgets.QLabel(self.widget)
        self.label_current.setObjectName("label_current")
        self.gridLayout.addWidget(self.label_current, 0, 0, 1, 1)
        self.label_current_info = QtWidgets.QLabel(self.widget)
        self.label_current_info.setObjectName("label_current_info")
        self.gridLayout.addWidget(self.label_current_info, 0, 1, 1, 1)
        self.label_total = QtWidgets.QLabel(self.widget)
        self.label_total.setObjectName("label_total")
        self.gridLayout.addWidget(self.label_total, 1, 0, 1, 1)
        self.label_total_info = QtWidgets.QLabel(self.widget)
        self.label_total_info.setObjectName("label_total_info")
        self.gridLayout.addWidget(self.label_total_info, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 164, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "START", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.label_current.setText(QtWidgets.QApplication.translate("MainWindow", "Сейчас", None, -1))
        self.label_current_info.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_total.setText(QtWidgets.QApplication.translate("MainWindow", "ИТОГО", None, -1))
        self.label_total_info.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))

