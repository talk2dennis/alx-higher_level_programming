#!/usr/bin/python3:
"""
Defines a class Square

"""


class Square:
    """ Square is a class with private instance atrinbue of size"""

    def __init__(self, size=0, position=(0, 0)):
        """
        creates a new instance of a Square
        Args:
            size: size of the square
            position: tuple
        Raises:
            TypeError: if int was not provided
            ValueError: if value is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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
        Raises:
            TypeError: if int was not provided
            ValueError: if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        defines a property method that returns the position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        defines a setter for ppsition
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not value[0] >= 0 or not value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        defines a public method my_print
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
