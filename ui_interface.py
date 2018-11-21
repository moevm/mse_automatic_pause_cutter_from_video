from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_select_input = QtWidgets.QPushButton(self.centralwidget)
        self.button_select_input.setGeometry(QtCore.QRect(10, 10, 181, 32))
        self.button_select_input.setObjectName("button_select_input")
        self.line_v = QtWidgets.QFrame(self.centralwidget)
        self.line_v.setGeometry(QtCore.QRect(190, -10, 31, 801))
        self.line_v.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_v.setObjectName("line_v")
        self.line_h = QtWidgets.QFrame(self.centralwidget)
        self.line_h.setGeometry(QtCore.QRect(210, 370, 601, 20))
        self.line_h.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h.setObjectName("line_h")
        self.video_player_original = VideoPlayer(self.centralwidget)
        self.video_player_original.setEnabled(True)
        self.video_player_original.setGeometry(QtCore.QRect(220, 10, 591, 361))
        self.video_player_original.setObjectName("video_player_original")
        self.video_player_result = VideoPlayer(self.centralwidget)
        self.video_player_result.setGeometry(QtCore.QRect(220, 390, 591, 361))
        self.video_player_result.setObjectName("video_player_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 22))
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
        self.button_select_input.setText(_translate("MainWindow", "Select input file"))

from video_player import VideoPlayer
