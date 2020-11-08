import sys
import argparse
parser = argparse.ArgumentParser('Версия 1.0')

parser.add_argument('-f','--file', type=str, nargs='+')
parser.add_argument('-n', '--name', help='необходимо ввести имя файла для поиска')
parser.add_argument('-n', '--name', help='необходимо ввести имя файла для поиска')

argv = parser.parse_args()

for find_file in argv.file:
    in_file=open(find_file)
    print(in_file.read())
