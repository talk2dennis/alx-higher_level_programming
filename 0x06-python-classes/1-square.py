#!/usr/bin/python3
"""
Defines a class Square

"""


class Square:
    """ Square is a class with private instance atrinbue of size"""

    def __init__(self, size):
        """
        creates a new instance of a Square
        Args:
            size: size of the square
        """

        self.__size = size
