#!/usr/bin/python3
"""
Defines a class Square

"""


class Square:
    """ Square is a class with private instance atrinbue of size"""

    def __init__(self, size=0):
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

    def area(self):
        """
        defines a method that returns the area of a square
        Return: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        defines getter for size
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        defines setter for private instance of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """
        compares this instance of equal to other instance
        """
        return self.__size == other.__size

    def __lt__(self, other):
        """
        compares self, if less than the other
        """
        return self.__size < other.__size

    def __le__(self, other):
        """
        compares self, returns true if greater than others
        """
        return self.__size <= other.__size

    def __gt__(self, other):
        """
        compares self if greater than other
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """
        compares self if greater than or equal to other
        """
        return self.__size >= other.__size

    def __str__(self):
        """"
        defines string representation of the class square
        Return:
            returns the size of the square
        """
        return self.__size
