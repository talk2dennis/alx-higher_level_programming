#!/usr/bin/python3
"""append to a file"""


def append_file(filename="", text=""):
    """a function that writes to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
