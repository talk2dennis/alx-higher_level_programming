#!/urs/bin/python3
"""open file module"""


def read_file(filename=""):
    """read_file - a function that reads from a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
