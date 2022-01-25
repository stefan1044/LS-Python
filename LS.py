from os import*
import argparse


def LS(arguments):
    directoryList=[]
    arguments.add_argument("directory", type=str, nargs='?', default='.')
    arguments.add_argument("--all", "-a", action="store_true",
                           help="do not ignore entries starting with .")
    args = arguments.parse_args()
    all = True if args.all else False
    for iterator in scandir(args.directory):
        if all:
            directoryList.append(iterator.name)
        elif str(iterator).startswith('.') == False:
            directoryList.append(iterator.name)
    for iterator in directoryList:
        print(type(iterator))
        print(iterator)
            


if __name__ == "__main__":
    try:
        inputString = argparse.ArgumentParser()
        LS(inputString)
    except OSError as error:
        print(error)
