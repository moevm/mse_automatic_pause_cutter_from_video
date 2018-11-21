from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtMultimedia import QMediaPlayer
import ui_video_player


class VideoPlayer(QtWidgets.QWidget, ui_video_player.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.button_play.clicked.connect(self.play)
        self.button_pause.clicked.connect(self.pause)
        self.time_slider.sliderMoved.connect(self.setPosition)

        self.mediaPlayer.setVideoOutput(self.video)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

    def play(self):
        if (self.mediaPlayer.state() == QMediaPlayer.PlayingState):
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            self.button_pause.setEnabled(True)
            self.button_play.setEnabled(False)
            self.video.resize(self.video.width(), self.video.height() + 1)
            self.video.resize(self.video.width(), self.video.height() - 1)

    def pause(self):
        self.mediaPlayer.pause()
        self.button_pause.setEnabled(False)
        self.button_play.setEnabled(True)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def positionChanged(self, position):
        self.time_slider.setValue(position)

    def durationChanged(self, duration):
        self.time_slider.setRange(0, duration)