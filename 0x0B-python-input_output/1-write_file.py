#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """a function that writes to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
