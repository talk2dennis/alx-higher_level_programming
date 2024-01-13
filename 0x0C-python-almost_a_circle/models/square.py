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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size attribute of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ returns the string representation of the class square"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                     self.id, self.x, self.y,
                                                     self.width)
