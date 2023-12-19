#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    stat = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        stat = False
    finally:
        return stat
