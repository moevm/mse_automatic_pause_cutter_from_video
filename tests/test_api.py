import pytest
from ..movie_cutter import MovieCutterAPI
from .common import *
import moviepy.editor as mp
import os


class TestApi:
    def setup(self):
        self.cutter = MovieCutterAPI(source_file=SOURCE_FILE, min_silence_len=MIN_SILIENCE_LEN,
                                     silence_thresh=SILIENCE_THRESH, output_file=OUTPUT_FILE)
        self.result_clip = mp.VideoFileClip(RESULT_FILE)

    def test_if_convert_required_ts(self):
        self.cutter.format = "ts"
        assert self.cutter.convert_required() == True

    def test_if_convert_required_mkv(self):
        self.cutter.format = "mkv"
        assert self.cutter.convert_required() == True

    def test_if_convert_not_required_mkv(self):
        self.cutter.format = "mp4"
        assert self.cutter.convert_required() == False

    def test_convert(self):
        self.cutter = MovieCutterAPI(source_file=SOURCE_FILE_MKV, min_silence_len=MIN_SILIENCE_LEN,
                                     silence_thresh=SILIENCE_THRESH, output_file=OUTPUT_FILE)
        self.cutter.convert()
        assert self.cutter.is_converted == True, "Файл не сконвертирован"

    def test_cut(self):
        self.cutter.cut()
        assert round(self.cutter.clip_cut.duration, 1) == round(self.result_clip.duration,
                                                                1), "Длительность полученного видео не совпадает с ожидаемой"

    def test_save_clip(self):
        self.cutter.cut()
        self.cutter.save_clip()
        assert os.path.exists(RESULT_FILE) == True, "Файл не сохранён"

    def test_if_saved_file_correct(self):
        self.cutter.cut()
        self.cutter.save_clip()
        cut_file = mp.VideoFileClip(OUTPUT_FILE)
        assert round(cut_file.duration, 1) == round(self.result_clip.duration,
                                                    1), "Длительность полученного видео не совпадает с ожидаемой"

    def teardown(self):
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
        if os.path.exists(RESULT_FILE_CONVERTED):
            os.remove(RESULT_FILE_CONVERTED)
