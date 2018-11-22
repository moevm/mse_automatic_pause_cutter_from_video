from movie_cutter import MovieCutterAPI
from interface import GUI
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automatically cuts silent periods from video file',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-g', '--gui', action='store_true',
                        help='run in GUI mode, if selected, all other flags will be ignored')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), help='path to input file')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='path where output file will be saved',
                        default='./cut.mp4')
    parser.add_argument('-m', '--min', type=int, help='minimal duration of silent part to be cut (in milliseconds)',
                        default=100)
    parser.add_argument('-t', '--thresh', type=float,
                        help='maximum threshold (in db) of "silence". Everything bellow this level will be considered as silence',
                        default=-16)

    args = parser.parse_args()
    if (args.gui):
        GUI()
    else:
        if (args.input is None):
            parser.error("the following arguments are required: -i/--input")
        else:
            cutter = MovieCutterAPI(source_file=args.input.name, output_file=args.output.name, min_silence_len=args.min,
                                    silence_thresh=args.thresh)
            cutter.cut()
            cutter.save_clip()
