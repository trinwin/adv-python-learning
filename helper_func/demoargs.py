# ----------------------------------------------------------------------
# Name:        demoargs
# Purpose:     demonstrate the use of the argparse module
#
# Author:      Rula Khayrallah
#
# ----------------------------------------------------------------------
"""
Demonstrate the use of the argparse module.

usage: demoargs.py [-h] [-v] {blue,yellow,green} [name] [size] [score]
positional arguments:
  {blue,yellow,green}  What background color would you like?
  players              How many players?
  scale                What scale to use?
  scorefile            File to be used to save the score

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Print details?
"""
import argparse
import sys


def scale_type(entered_scale):
    """
    Validate the user entered scale and return the highest multiple
    of 10 that is less or equal to the entered scale
    :param entered_scale: (string)
    :return: integer
    """
    try:
        scale = float(entered_scale)
    except ValueError:
        raise argparse.ArgumentTypeError(f'invalid number')
    else:
        if scale < 10:
            raise argparse.ArgumentTypeError('must be >= 10')
    return int(scale) // 10 * 10


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the number of players (int),
        the scale(int), the color (string), scorefile (file object) and
        the verbose option (boolean).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='What background color would you like?',
                        choices=['blue', 'yellow', 'green'])

    parser.add_argument('players',
                        help='How many players?',
                        type=int,
                        nargs='?',
                        default=2)

    parser.add_argument('scale',
                        help='What scale to use?',
                        type=scale_type,
                        nargs='?',
                        default=10)

    parser.add_argument('scorefile',
                        help='File to be used to save the score',
                        type=argparse.FileType('x', encoding='UTF-8'),
                        nargs='?',
                        default=sys.stdout)

    parser.add_argument('-v', '--verbose',
                        help='Print details?',
                        action='store_true')

    arguments = parser.parse_args()
    players = arguments.players
    scale = arguments.scale
    color = arguments.color
    scorefile = arguments.scorefile
    verbose = arguments.verbose
    return players, scale, color, scorefile, verbose


def main():
    players, scale, color, scorefile, verbose = get_arguments()
    if verbose:
        print(f'Starting a {color} game with {players} players')
        print(f'at a scale of {scale}.')
    scorefile.write('Hello\n')


if __name__ == '__main__':
    main()
