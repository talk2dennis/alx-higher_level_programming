#!/usr/bin/python3
"""
a class that represents a retangle
"""


class Rectangle:
    """
    my retangle class
    Args:
        width: a private attribute
    """
    def __init__(self, width=0, height=0):
        """ initialising the Retangle class """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for field width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        a setter method for width
        Args:
            value (int): value for width
        Raise:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        A method to get the height attribute
        Return: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A metthod that sets the height attribute
        Args:
            value (int): the new value for height
        Raise:
            TypeError: if value is not a number
            ValueError: if value is less than 0
        Return: nothing
        """
        if not isintance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
