# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/leonidkutsenok/Documents/Projects/mse_automatic_pause_cutter_from_video/ui_src/interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_select_input = QtWidgets.QPushButton(self.centralwidget)
        self.button_select_input.setGeometry(QtCore.QRect(760, 420, 181, 32))
        self.button_select_input.setObjectName("button_select_input")
        self.video_player_original = VideoPlayer(self.centralwidget)
        self.video_player_original.setEnabled(True)
        self.video_player_original.setGeometry(QtCore.QRect(10, 40, 500, 360))
        self.video_player_original.setObjectName("video_player_original")
        self.video_player_result = VideoPlayer(self.centralwidget)
        self.video_player_result.setGeometry(QtCore.QRect(520, 40, 500, 360))
        self.video_player_result.setObjectName("video_player_result")
        self.input_min_length = QtWidgets.QSpinBox(self.centralwidget)
        self.input_min_length.setGeometry(QtCore.QRect(200, 420, 171, 24))
        self.input_min_length.setMaximum(10000)
        self.input_min_length.setProperty("value", 100)
        self.input_min_length.setObjectName("input_min_length")
        self.input_thresh = QtWidgets.QSpinBox(self.centralwidget)
        self.input_thresh.setGeometry(QtCore.QRect(10, 420, 171, 24))
        self.input_thresh.setMinimum(-99)
        self.input_thresh.setProperty("value", -16)
        self.input_thresh.setObjectName("input_thresh")
        self.button_convert = QtWidgets.QPushButton(self.centralwidget)
        self.button_convert.setGeometry(QtCore.QRect(580, 420, 181, 32))
        self.button_convert.setObjectName("button_convert")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, -10, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
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
        self.label.setText(_translate("MainWindow", "Исходный файл"))
        self.label_2.setText(_translate("MainWindow", "Предпросмотр"))

from video_player import VideoPlayer
