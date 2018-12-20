from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPalette, QColor
import numpy as np
import ui_video_player
import vlc
import sys


class VideoPlayer(QtWidgets.QWidget, ui_video_player.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.instance = vlc.Instance()
        self.mediaPlayer = self.instance.media_player_new()

        self.button_play.clicked.connect(self.play)
        self.button_pause.clicked.connect(self.pause)
        self.time_slider.sliderMoved.connect(self.setPosition)

        self.palette = self.video.palette()
        self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.video.setPalette(self.palette)
        self.video.setAutoFillBackground(True)

        self.timer = QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.updateUI)
        self.isPaused = False

    def play(self):
        self.mediaPlayer.play()
        self.button_pause.setEnabled(True)
        self.button_play.setEnabled(False)
        self.isPaused = False
        self.timer.start()

    def pause(self):
        self.mediaPlayer.pause()
        self.button_pause.setEnabled(False)
        self.button_play.setEnabled(True)
        self.isPaused = True

    def stop(self):
        self.mediaPlayer.stop()
        self.button_pause.setEnabled(False)
        self.button_play.setEnabled(True)
        self.isPaused = True
        self.time_slider.setSliderPosition(0)

    def setPosition(self, position):
        self.mediaPlayer.set_position(position / 100.0)
        return

    def openFile(self, filename=None):
        if sys.version < '3':
            filename = unicode(filename)
        self.media = self.instance.media_new(filename)
        self.mediaPlayer.set_media(self.media)
        self.media.parse()
        if sys.platform.startswith('linux'):  # Linux (X Server)
            self.mediaPlayer.set_xwindow(self.video.winId())
        elif sys.platform == "win32":  # Windows
            self.mediaPlayer.set_hwnd(self.video.winId())
        elif sys.platform == "darwin":  # OS X
            self.mediaPlayer.set_nsobject(int(self.video.winId()))
        self.play()

    def updateUI(self):
        print(self.mediaPlayer.get_position())
        self.time_slider.setSliderPosition(self.mediaPlayer.get_position() * 100)
        seconds_elapsed = (int(np.floor(self.mediaPlayer.get_position() * self.mediaPlayer.get_length() / 1000)))
        num_minutes_passed = int(seconds_elapsed / 60)
        num_seconds_passed = int(seconds_elapsed % 60)
        seconds_left = int(self.mediaPlayer.get_length() / 1000) - seconds_elapsed
        num_minutes_left = int(seconds_left/ 60)
        num_seconds_left = int(seconds_left % 60)

        num_minutes_passed_string = str(num_minutes_passed) if num_minutes_passed >= 10 else '0' + str(num_minutes_passed)
        num_seconds_passed_string = str(num_seconds_passed) if num_seconds_passed >= 10 else '0' + str(num_seconds_passed)
        num_seconds_left_string = str(num_seconds_left) if num_seconds_left >= 10 else '0' + str(num_seconds_left)
        num_minutes_left_string = str(num_minutes_left) if num_minutes_left >= 10 else '0' + str(num_minutes_left)
        self.label_time_passed.setText(num_minutes_passed_string + ':' + num_seconds_passed_string)
        self.label_time_left.setText('-' + num_minutes_left_string + ':' + num_seconds_left_string)
        if not self.mediaPlayer.is_playing():
            self.timer.stop()
            if not self.isPaused: self.stop()
