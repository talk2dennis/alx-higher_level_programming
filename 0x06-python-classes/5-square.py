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

    def my_print(self):
        """
        defines a public method my_print
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
