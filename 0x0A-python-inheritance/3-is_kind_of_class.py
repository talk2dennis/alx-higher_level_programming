#!/usr/bin/python3
"""funtions return true if an obj is an instance"""


def is_kind_of_class(obj, a_class):
    """returns true if an obj is an instance of a class otherwise false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
