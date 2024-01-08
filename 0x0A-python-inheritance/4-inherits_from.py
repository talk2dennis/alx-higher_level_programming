#!/usr/bin/python3
"""checks if a class is the direct parent of an obj"""


def inherits_from(obj, a_class):
    """inherits_from - checks if a class is the direct parent of an object"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
