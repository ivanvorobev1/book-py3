import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-g', '--goodbye', action='store_const', const=True)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    print (namespace)

    print ("Привет, мир!")
    if namespace.goodbye:
        print ("Прощай, мир!")
