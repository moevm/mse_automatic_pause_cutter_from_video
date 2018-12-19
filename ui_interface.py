# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/leonidkutsenok/Documents/Projects/mse_automatic_pause_cutter_from_video/ui/interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_select_input = QtWidgets.QPushButton(self.centralwidget)
        self.button_select_input.setGeometry(QtCore.QRect(10, 390, 181, 32))
        self.button_select_input.setObjectName("button_select_input")
        self.video_player_original = VideoPlayer(self.centralwidget)
        self.video_player_original.setEnabled(True)
        self.video_player_original.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.video_player_original.setObjectName("video_player_original")
        self.video_player_result = VideoPlayer(self.centralwidget)
        self.video_player_result.setGeometry(QtCore.QRect(510, 10, 481, 281))
        self.video_player_result.setObjectName("video_player_result")
        self.input_min_length = QtWidgets.QSpinBox(self.centralwidget)
        self.input_min_length.setGeometry(QtCore.QRect(370, 390, 171, 24))
        self.input_min_length.setMaximum(10000)
        self.input_min_length.setProperty("value", 100)
        self.input_min_length.setObjectName("input_min_length")
        self.input_thresh = QtWidgets.QSpinBox(self.centralwidget)
        self.input_thresh.setGeometry(QtCore.QRect(190, 390, 171, 24))
        self.input_thresh.setMinimum(-99)
        self.input_thresh.setProperty("value", -40)
        self.input_thresh.setObjectName("input_thresh")
        self.button_convert = QtWidgets.QPushButton(self.centralwidget)
        self.button_convert.setGeometry(QtCore.QRect(810, 390, 181, 32))
        self.button_convert.setObjectName("button_convert")
        self.graphicsView = Timeline(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 300, 971, 81))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MSE Automatic Pause Cutter"))
        self.button_select_input.setText(_translate("MainWindow", "Выбор исходного файла"))
        self.input_min_length.setSuffix(_translate("MainWindow", " мс"))
        self.input_thresh.setSuffix(_translate("MainWindow", " Дб"))
        self.button_convert.setText(_translate("MainWindow", "Преобразовать"))

from timeline import Timeline
from video_player import VideoPlayer
