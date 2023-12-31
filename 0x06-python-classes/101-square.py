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

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
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

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
