#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        ans = fct(*args)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        ans = None
    finally:
        return ans
