import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("arg", nargs='*')
args = parser.parse_args()
if len(args.arg) != 0:
    print('\n'.join(args.arg))
else:
    print('no args')