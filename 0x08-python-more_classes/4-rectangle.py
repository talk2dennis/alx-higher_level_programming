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
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ getter for field width """
        return self.__width

    @property
    def height(self):
        """
        A method to get the height attribute
        Return: the height
        """
        return self.__height

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
        self.__width = value

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        string = ""
        if self.__height == 0 or self.width == 0:
            return string
        for i in range(self.__height):
            string += "#" * self.__width
            if i < ((self.__height) - 1):
                string += '\n'
        return string

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", "\
                + str(self.__height) + ")"
