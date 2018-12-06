from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 367)
        self.button_play = QtWidgets.QPushButton(Form)
        self.button_play.setGeometry(QtCore.QRect(0, 330, 71, 32))
        self.button_play.setObjectName("button_play")
        self.video = None
        if sys.platform == "darwin": # for MacOS
            from PyQt5.QtWidgets import QMacCocoaViewContainer
            self.video = QMacCocoaViewContainer(0,parent=Form)
        else:
            self.video = QtWidgets.QFrame(parent=Form)
        self.video.setGeometry(QtCore.QRect(9, 0, 576, 324))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy)
        self.video.setObjectName("video")
        self.button_pause = QtWidgets.QPushButton(Form)
        self.button_pause.setGeometry(QtCore.QRect(60, 330, 71, 32))
        self.button_pause.setObjectName("button_pause")
        self.time_slider = QtWidgets.QSlider(Form)
        self.time_slider.setGeometry(QtCore.QRect(130, 330, 451, 22))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_play.setText(_translate("Form", "Play"))
        self.button_pause.setText(_translate("Form", "Pause"))

