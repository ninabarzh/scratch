import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--startdir", help="directory to start from", default='.')
args = parser.parse_args()

if args.start:
    for (dirpath, dirnames, filenames) in os.walk(args.start):
        for f in filenames:
            print('File: ', os.path.join(dirpath, f))
        for d in dirnames:
            print('Directory: ', os.path.join(dirpath, d))

