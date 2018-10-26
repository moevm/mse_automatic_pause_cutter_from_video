from pydub import AudioSegment
from pydub.silence import detect_silence
from moviepy.editor import VideoFileClip, concatenate_videoclips

class MovieCutterAPI:
    def __init__(self, source_file='test.mp4', output_file='test_cut.mp4', format='mp4', min_silence_len=100,
                 silence_thresh=-16):
        self.source_file = source_file
        self.output_file = output_file
        self.format = format
        self.min_silence_len = min_silence_len
        self.silence_thresh = silence_thresh

        self.clip = VideoFileClip(self.source_file)
        self.clip_cut = None

    def cut(self):
        # Выризаем аудио из видео для поиска "тихих" мест
        audio = AudioSegment.from_file(self.source_file, self.format)

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
        self.clip_cut.write_videofile(self.output_file)