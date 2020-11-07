import sys
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-n', '--names', default='name111')

argv = parser.parse_args()

print("Привет, {}!".format (argv.names))
