#!/usr/bin/python3
"""square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square - Square class inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ - initialises the attributes of the Square class
        Args:
            size (int): The width and height of the square
            x (int): the x cordinate of Square instance
            y (int): the y cordinate of Square instance
            id (int): default None, automatically generated else asigned id
        """
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        """ returns the string representation of the class square"""
        return "[{}] (<id>) <{}>/<{}> - <{}>".format(self.__class__.__name__,
                                                     self.x, self.y, self.width)
