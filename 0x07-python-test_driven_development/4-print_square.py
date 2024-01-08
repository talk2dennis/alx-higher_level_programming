#!/usr/bin/python3
"""
print_square
"""


def print_square(size):
    """
    print_square - A function that prints squares using #
    Args:
        size: is the size length of the square (int)
    raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: if size is float and less than 0
    Return: nothing
    """

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size, end="")
        print()
