from pydub import AudioSegment
from pydub.silence import detect_silence
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.config import change_settings
import subprocess
import os

change_settings({"FFMPEG_BINARY": "ffmpeg"})

file_codec = {
    "ts": "mpeg2video",
    "mkv": "libx264",
    "mp4": "libx264",
}


class MovieCutterAPI:
    def __init__(self, source_file='test.mp4', output_file=None, min_silence_len=100,
                 silence_thresh=-16):
        self.source_file = source_file
        self.format = self.source_file.split('.')[-1]
        if output_file:
            self.output_file = output_file
        else:
            self.output_file = ''.join(self.source_file.split('.')[:-1]) + '_cut.' + self.format
        self.codec = file_codec[self.format]
        self.min_silence_len = min_silence_len
        self.silence_thresh = silence_thresh

        self.clip = VideoFileClip(self.source_file)
        self.clip_cut = None

    def cut(self):
        if (self.format == "ts" or self.format == "mkv"):
            subprocess.run(['ffmpeg', '-i', self.source_file, "_tmp.mp4"])
            self.source_file = "_tmp.mp4"
        # Выризаем аудио из видео для поиска "тихих" мест
        audio = AudioSegment.from_file(self.source_file)

        # Получаем массив времен начала и конца "тихих" участков
        chunks = detect_silence(audio, min_silence_len=self.min_silence_len, silence_thresh=self.silence_thresh)

        clips = []
        last_start = 0
        # Выризаем каждый "тихий" участок
        # Для этого сохраняем промежуток от конца предыдущего тихого участка до начала следующего
        for i, chunk in enumerate(chunks):
            clips.append(self.clip.subclip(last_start, float(chunk[0] / 1000)))
            last_start = float(chunk[1] / 1000)

        self.clip_cut = concatenate_videoclips(clips)

    def save_clip(self):
        self.clip_cut.write_videofile(self.output_file, codec=self.codec, audio_codec="aac")
        os.remove('./_tmp.mp4')
        return self.output_file
