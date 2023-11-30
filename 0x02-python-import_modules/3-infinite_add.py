#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_len = len(argv)
    total = 0
    if arg_len == 1:
        print("{}".format(total))
    else:
        for i in range(1, arg_len):
            total += int(argv[i])
        print("{}".format(total))
