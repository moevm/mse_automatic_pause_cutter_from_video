# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/leonidkutsenok/Documents/Projects/mse_automatic_pause_cutter_from_video/ui_src/video_player.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyle
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 360)
        self.button_play = QtWidgets.QPushButton(Form)
        self.button_play.setGeometry(QtCore.QRect(2, 289, 50, 50))
        self.button_play.setText("")
        icon = QtGui.QIcon.fromTheme("SP_MediaPlay")
        self.button_play.setIcon(icon)
        self.button_play.setObjectName("button_play")
        self.button_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.video = None
        if sys.platform == "darwin": # for MacOS
            from PyQt5.QtWidgets import QMacCocoaViewContainer
            self.video = QMacCocoaViewContainer(0,parent=Form)
        else:
            self.video = QtWidgets.QFrame(parent=Form)
        self.video.setGeometry(QtCore.QRect(9, 0, 500, 280))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy)
        self.video.setObjectName("video")
        self.button_pause = QtWidgets.QPushButton(Form)
        self.button_pause.setGeometry(QtCore.QRect(42, 289, 50, 50))
        self.button_pause.setText("")
        self.button_pause.setObjectName("button_pause")
        self.button_pause.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.time_slider = QtWidgets.QSlider(Form)
        self.time_slider.setGeometry(QtCore.QRect(140, 300, 301, 22))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        self.label_time_passed = QtWidgets.QLabel(Form)
        self.label_time_passed.setGeometry(QtCore.QRect(100, 300, 61, 20))
        self.label_time_passed.setObjectName("label_time_passed")
        self.label_time_left = QtWidgets.QLabel(Form)
        self.label_time_left.setGeometry(QtCore.QRect(450, 300, 60, 16))
        self.label_time_left.setObjectName("label_time_left")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_time_passed.setText(_translate("Form", "00:00"))
        self.label_time_left.setText(_translate("Form", "-00:00"))

