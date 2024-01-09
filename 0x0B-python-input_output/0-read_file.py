#!/urs/bin/python3
"""open file module"""


def read_file(filename=""):
    """print_file - reads from a file using unicode format and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
