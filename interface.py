import ui_interface
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtMultimedia import QMediaContent
from movie_cutter import MovieCutterAPI


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
        self.button_convert.clicked.connect(self.convert)
        self.input_file_name = None

    def openFile(self):
        self.input_file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", QDir.homePath())
        if self.input_file_name != '':
            print(self.input_file_name)
            self.video_player_original.openFile(self.input_file_name)

    def convert(self):
        if (self.input_file_name is None):
            self.showErrorMessage("Не указан исходный файл")
        else:
            movie_cutter = MovieCutterAPI(source_file=self.input_file_name,
                                          min_silence_len=self.input_min_length.value(),
                                          silence_thresh=self.input_thresh.value())
            movie_cutter.cut()
            output_file_name = movie_cutter.save_clip()
            print(output_file_name)
            self.video_player_result.openFile(output_file_name)

    def showErrorMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибкв")
        msg.setInformativeText(message)
        msg.setWindowTitle("Ошибка")
        msg.show()
        msg.exec()
