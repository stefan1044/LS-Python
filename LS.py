from os import*
import argparse


def LS(arguments):
    directoryList = []
    
    arguments.add_argument("directory", type=str, nargs='?', default='.')
    arguments.add_argument("-a", "--all", dest="all", action="store_true",
                           help="do not ignore entries starting with .")
    arguments.add_argument("-1", dest="one", action="store_true",
                           help="list one file per line.  Avoid '\n' with -q or -b")
    arguments.add_argument("-b", "--escape", dest="C", action="store_true",
                           help="list one file per line.  Avoid '\n' with -q or -b")
    
    
    args = arguments.parse_args()

    all = True if args.all else False
    endSeparator = '\n' if args.one else ' '
    cEscape = True if args.C else False
    
    for iterator in scandir(args.directory):
        if all:
            if ' ' in iterator.name:
                directoryList.append(iterator.name.replace(' ',"\ ")) if cEscape else directoryList.append("'"+iterator.name+"'")
            else: directoryList.append(iterator.name)
        elif str(iterator.name).startswith('.') is False:
            if ' ' in iterator.name:
                directoryList.append(iterator.name.replace(' ',"\ ")) if cEscape else directoryList.append("'"+iterator.name+"'")
            else: directoryList.append(iterator.name)
    for iterator in directoryList:
        print(iterator, end=endSeparator)


if __name__ == "__main__":
    try:
        inputString = argparse.ArgumentParser()
        LS(inputString)
    except OSError as error:
        print(error)
