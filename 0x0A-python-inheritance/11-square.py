#!/usr/bin/python3
"""Defines a Square class that inherits from a Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """string representation of Rectangle class"""
        return "[{}] {}/{}".format(str(self.__class__.__name__),
                                   str(self.__size), str(self.__size))
