#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    numArgs = len(argv)
    if numArgs == 1:
        print("0 arguments.")
    elif numArgs == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(numArgs - 1))
    for i in range(1, numArgs):
        print("{}: {}".format(i, argv[i]))
