import os

SOURCE_FILE = os.path.dirname(__file__) + "/sources/test.mp4"
SOURCE_FILE_MKV = os.path.dirname(__file__) + "/sources/test.mkv"
RESULT_FILE = os.path.dirname(__file__) + "/sources/result.mp4"
OUTPUT_FILE = os.path.dirname(__file__) + "/sources/output.mp4"
RESULT_FILE_CONVERTED = os.path.dirname(__file__) + "/sources/_tmp.mp4"
MIN_SILIENCE_LEN = 100
SILIENCE_THRESH = -40