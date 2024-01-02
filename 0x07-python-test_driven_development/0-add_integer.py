#!/usr/bin/python3
"""
A python function to return the addition of two integers
"""


def add_integer(a, b=98):
    """
    add_integer - a function that adds qnd return the sum of the result.
    Args:
        a: int
        b: int with default 98
    Return:
        sum of the two numbers
    Raises:
        typeError
    """

    if isinstance(a, float):
        a = int(a)
    if b is not None and isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if b is not None and not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
