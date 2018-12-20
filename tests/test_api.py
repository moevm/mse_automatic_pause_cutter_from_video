import pytest
from ..movie_cutter import MovieCutterAPI
from .common import *
import moviepy.editor as mp
import os


class TestApi:
    def setup(self):
        self.cutter_mp4 = MovieCutterAPI(source_file=SOURCE_FILE_MP4, min_silence_len=MIN_SILIENCE_LEN,
                                         silence_thresh=SILIENCE_THRESH, output_file=OUTPUT_FILE_MP4)
        self.cutter_mkv = MovieCutterAPI(source_file=SOURCE_FILE_MKV, min_silence_len=MIN_SILIENCE_LEN,
                                         silence_thresh=SILIENCE_THRESH, output_file=OUTPUT_FILE_MKV)
        self.cutter_ts = MovieCutterAPI(source_file=SOURCE_FILE_TS, min_silence_len=MIN_SILIENCE_LEN,
                                         silence_thresh=SILIENCE_THRESH, output_file=OUTPUT_FILE_TS)
        self.result_clip_mp4 = mp.VideoFileClip(RESULT_FILE_MP4)
        self.result_clip_mkv = mp.VideoFileClip(RESULT_FILE_MKV)
        self.result_clip_ts = mp.VideoFileClip(RESULT_FILE_TS)

    def test_if_convert_required_mp4(self):
        self.cutter_mp4.format = "mp4"
        assert self.cutter_mp4.convert_required() == False

    def test_if_convert_required_ts(self):
        self.cutter_mp4.format = "ts"
        assert self.cutter_mp4.convert_required() == True

    def test_if_convert_required_mkv(self):
        self.cutter_mp4.format = "mkv"
        assert self.cutter_mp4.convert_required() == True

    def test_convert_mp4(self):
        self.cutter_mp4.convert()
        assert self.cutter_mp4.is_converted == True, "Файл не сконвертирован"

    def test_cut_mp4(self):
        self.cutter_mp4.cut()
        assert round(self.cutter_mp4.clip_cut.duration, 1) == round(self.result_clip_mp4.duration,
                                                                    1), "Длительность полученного видео не совпадает с ожидаемой"
    def test_save_clip_mp4(self):
        self.cutter_mp4.cut()
        self.cutter_mp4.save_clip()
        assert os.path.exists(RESULT_FILE_MP4) == True, "Файл не сохранён"

    def test_if_saved_file_correct_mp4(self):
        self.cutter_mp4.cut()
        self.cutter_mp4.save_clip()
        cut_file = mp.VideoFileClip(OUTPUT_FILE_MP4)
        assert round(cut_file.duration, 1) == round(self.result_clip_mp4.duration,
                                                    1), "Длительность полученного видео не совпадает с ожидаемой"

    def test_convert_mkv(self):
        self.cutter_mkv.convert()
        assert self.cutter_mkv.is_converted == True, "Файл не сконвертирован"

    def test_cut_mkv(self):
        self.cutter_mkv.cut()
        assert round(self.cutter_mkv.clip_cut.duration, 1) == round(self.result_clip_mkv.duration,
                                                                    1), "Длительность полученного видео не совпадает с ожидаемой"
    def test_save_clip_mkv(self):
        self.cutter_mkv.cut()
        self.cutter_mkv.save_clip()
        assert os.path.exists(RESULT_FILE_MKV) == True, "Файл не сохранён"

    def test_if_saved_file_correct_mkv(self):
        self.cutter_mkv.cut()
        self.cutter_mkv.save_clip()
        cut_file = mp.VideoFileClip(OUTPUT_FILE_MKV)
        assert round(cut_file.duration, 1) == round(self.result_clip_mkv.duration,
                                                    1), "Длительность полученного видео не совпадает с ожидаемой"

    def test_convert_ts(self):
        self.cutter_ts.convert()
        assert self.cutter_ts.is_converted == True, "Файл не сконвертирован"

    def test_cut_ts(self):
        self.cutter_ts.cut()
        assert round(self.cutter_ts.clip_cut.duration, 1) == round(self.result_clip_ts.duration,
                                                                    1), "Длительность полученного видео не совпадает с ожидаемой"
    def test_save_clip_ts(self):
        self.cutter_ts.cut()
        self.cutter_ts.save_clip()
        assert os.path.exists(RESULT_FILE_TS) == True, "Файл не сохранён"

    def test_if_saved_file_correct_ts(self):
        self.cutter_ts.cut()
        self.cutter_ts.save_clip()
        cut_file = mp.VideoFileClip(OUTPUT_FILE_TS)
        assert round(cut_file.duration, 1) == round(self.result_clip_ts.duration,
                                                    1), "Длительность полученного видео не совпадает с ожидаемой"

    def teardown(self):
        if os.path.exists(OUTPUT_FILE_MP4):
            os.remove(OUTPUT_FILE_MP4)
        if os.path.exists(OUTPUT_FILE_MKV):
            os.remove(OUTPUT_FILE_MKV)
        if os.path.exists(OUTPUT_FILE_TS):
            os.remove(OUTPUT_FILE_TS)
        if os.path.exists(RESULT_FILE_CONVERTED):
            os.remove(RESULT_FILE_CONVERTED)
