#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_len = len(argv)
    if arg_len < 2:
        print("{} arguments.".format(len(argv) - 1))
    elif arg_len == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, arg_len):
            print("{}: {}".format(i, argv[i]))
