#!/usr/bin/python3
"""function returns true if same class"""


def is_same_class(obj, a_class):
    """it returns true is it is same class else false"""
    if type(obj) is a_class:
        return True
    else:
        return False
