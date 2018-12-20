import ui_interface
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog
from movie_cutter import MovieCutterAPI
from message_box import MessageBox


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
        self.message = None
        self.movie_cutter = None

    def openFile(self):
        self.input_file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", QDir.homePath())
        if self.input_file_name != '':
            self.movie_cutter = MovieCutterAPI(source_file=self.input_file_name,
                                               min_silence_len=self.input_min_length.value(),
                                               silence_thresh=self.input_thresh.value())
            if(self.movie_cutter.convert_required()) :
                self.showMessage('info', 'Необходима конвертация исходного файла, это может занять несколько минут')
            self.movie_cutter.convert()
            self.video_player_original.openFile(self.input_file_name)

    def convert(self):
        if (self.input_file_name is None):
            self.showMessage("error", "Не указан исходный файл")
        else:
            self.movie_cutter.min_silence_len = self.input_min_length.value()
            self.movie_cutter.silence_thresh = self.input_thresh.value()
            try:
                self.movie_cutter.cut()
                output_file_name = self.movie_cutter.save_clip()
                self.video_player_result.openFile(output_file_name)
            except Exception as ex:
                self.self.showMessage("error", str(ex))

    def showMessage(self, type, message):
        if (self.message):
            self.message.hide()
        self.message = MessageBox(type, message)
        self.message.show()

    def hideMessage(self):
        if (self.message):
            self.message.hide()
            self.message = None
