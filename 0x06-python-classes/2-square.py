#!/usr/bin/python3
"""
Defines a class Square

"""


class Square:
    """ Square is a class with private instance atrinbue of size"""

    def __init__(self, size = 0):
        """
        creates a new instance of a Square
        Args:
            size: size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
