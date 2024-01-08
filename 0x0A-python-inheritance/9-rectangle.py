#!/usr/bin/python3
"""class Rectangle inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class is a sub class of BaseGeometry class"""
    def __init__(self, width, height):
        """int method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """overidding the parent method"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of Rectangle class"""
        return "[{}] {}/{}".format(str(self.__class__.__name__),
                                   str(self.__width), str(self.__height))
