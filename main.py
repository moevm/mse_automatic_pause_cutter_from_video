from movie_cutter import MovieCutterAPI
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automatically cuts silent periods from video file',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), help='path to input file', required=True)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='path where output file will be saved',
                        default='./cut.mp4')
    parser.add_argument('-m', '--min', type=int, help='minimal duration of silent part to be cut (in milliseconds)',
                        default=100)
    parser.add_argument('-t', '--thresh', type=float,
                        help='maximum threshold (in db) of "silence". Everything bellow this level will be considered as silence',
                        default=-16)

    args = parser.parse_args()

    cutter = MovieCutterAPI(source_file=args.input.name, output_file=args.output.name, min_silence_len=args.min,
                            silence_thresh=args.thresh)
    cutter.cut()
    cutter.save_clip()
