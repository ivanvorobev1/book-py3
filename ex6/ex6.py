import sys
import argparse
parser = argparse.ArgumentParser('Версия 1.0')

parser.add_argument('-а', '--find', help='Короче тут типа поиск файлов в каталоге')
parser.add_argument('-n', '--name', default='name111', help='необходимо ввести имя файла для поиска')

argv = parser.parse_args()

print("Привет, {}!".format (argv.name))
