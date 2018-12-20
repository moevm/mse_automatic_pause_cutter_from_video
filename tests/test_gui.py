import pytest
from .common import *
from ..interface import *


class TestGui:
    def setup(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = GUI_Window()
        self.window.input_min_length.setProperty("value", MIN_SILIENCE_LEN)
        self.window.input_thresh.setProperty("value", SILIENCE_THRESH)

    def test_window_is_shown(self):
        assert self.window.height() > 0 and self.window.width() > 0

    def test_video_is_open(self):
        self.window.input_file_name = SOURCE_FILE_MP4
        self.window.openFile(True)
        assert self.window.video_player_original.mediaPlayer.get_media() is not None

    def test_result_video_is_shown(self):
        self.window.input_file_name = SOURCE_FILE_MP4
        self.window.openFile(True)
        self.window.button_convert.click()
        assert self.window.message is None and self.window.video_player_result.mediaPlayer.get_media() is not None

    def test_input_value_changes(self):
        self.window.input_min_length.setProperty("value", MIN_SILIENCE_LEN)
        self.window.input_thresh.setProperty("value", SILIENCE_THRESH)
        assert self.window.input_thresh.value() == SILIENCE_THRESH and self.window.input_min_length.value() == MIN_SILIENCE_LEN

    def test_original_video_is_playing(self):
        self.window.input_file_name = SOURCE_FILE_MP4
        self.window.openFile(True)
        self.window.video_player_original.button_play.click()
        assert self.window.video_player_original.isPaused == False

    def test_original_video_is_paused(self):
        self.window.input_file_name = SOURCE_FILE_MP4
        self.window.openFile(True)
        self.window.video_player_original.button_play.click()
        self.window.video_player_original.button_pause.click()
        assert self.window.video_player_original.isPaused == True

    def test_result_video_is_playing(self):
        self.window.video_player_result.openFile(RESULT_FILE_MP4)
        self.window.video_player_result.button_play.click()
        assert self.window.video_player_result.isPaused == False

    def test_result_video_is_paused(self):
        self.window.video_player_result.openFile(RESULT_FILE_MP4)
        self.window.video_player_result.button_play.click()
        self.window.video_player_result.button_pause.click()
        assert self.window.video_player_result.isPaused == True

    def teardown(self):
        if os.path.exists(OUTPUT_FILE_MP4):
            os.remove(OUTPUT_FILE_MP4)
