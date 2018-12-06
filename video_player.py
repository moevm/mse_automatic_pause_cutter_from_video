from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPalette, QColor
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
        self.time_slider.setSliderPosition(self.mediaPlayer.get_position() * 100)
        if not self.mediaPlayer.is_playing():
            self.timer.stop()
            if not self.isPaused: self.stop()
