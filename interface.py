import ui_interface
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaContent


class GUI():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = GUI_Window()
        self.window.show()
        self.app.exec_()


class GUI_Window(QtWidgets.QMainWindow, ui_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_select_input.clicked.connect(self.openFile)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Открыть файл", QDir.homePath())
        if fileName != '':
             self.video_player_original.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))