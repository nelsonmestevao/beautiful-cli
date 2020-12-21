"""example program

Usage: example.py [--count=N] <path> FILE...

Arguments:
  FILE     input file
  PATH     out directory

Options:
  -h --help         Show this screen.
  -v, --version     Show version.
  --count=N         Number of operations [default: 10].
"""
from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version = "example 1.0")

    for file in args['FILE']:
        print(file)
