from ast import arg
import os
import argparse


def LS( arguments):
    all=False
    arguments.add_argument("-a", help="do not ignore entries starting with .")
    arguments.parse_args("all")
    args = arguments.parse_args()
    print(args.all)
    for iterator in os.listdir():
        if all:
            print (iterator)
        elif  iterator.startswith('.') == False:
            print (iterator)
    


if __name__ == "__main__":
    try:
        inputString = argparse.ArgumentParser()
        LS(inputString)
    except OSError as error:
        print(error)
