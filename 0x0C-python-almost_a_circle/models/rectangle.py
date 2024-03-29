#!/usr/bin/python3
""" rectangle.py """
from models.base import Base


def check_int(name, value):
    """ check_int - validates integer value """
    if not isinstance(value, int):
        raise TypeError("{} must be an integer".format(name))
    if (name == "x" or name == "y") and value < 0:
        raise ValueError("{} must be >= 0".format(name))
    if (name == "width" or name == "height") and value <= 0:
        raise ValueError("{} must be > 0".format(name))


class Rectangle(Base):
    """
    Rectangle: rectangle class than inherits from Base class
    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): with a default
        y (int): with a default value
        id (int): id of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ intialising all the attributes of the rectangle """
        super().__init__(id)
        check_int("width", width)
        self.__width = width
        check_int("height", height)
        self.__height = height
        check_int("x", x)
        self.__x = x
        check_int("y", y)
        self.__y = y

    @property
    def width(self):
        """returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Defines private property of Rectangle class
        """
        check_int("width", value)
        self.__width = value

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defines the height of the Rectangle"""
        check_int("height", value)
        self.__height = value

    @property
    def x(self):
        """ getter for x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """defines the x value of Rectangle"""
        check_int("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter for y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y value"""
        check_int("y", value)
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """
        update - update rectangle with the variable args or kwargs supplied
        if args not supplied, kwargs will be used
        Args:
            *args (tuple): variable number of argument
            **kwargs (dict): key word argument
        """
        if not args:
            for k, v in kwargs.items():
                if k == "id":
                    super().__init__(v)
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
        for i in range(len(args)):
            if i == 0:
                super().__init__(args[i])
            if i == 1:
                self.width = args[i]
            if i == 2:
                self.height = args[i]
            if i == 3:
                self.x = args[i]
            if i == 4:
                self.y = args[i]

    def to_dictionary(self):
        """ converts the rectangle attributes to dict"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def display(self):
        """display - a public method that displays with # the rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for space in range(self.x):
                print(" ", end='')
            print("#" * self.width)

    def __str__(self):
        name = self.__class__.__name__
        no = str(self.id)
        x = str(self.x)
        y = str(self.y)
        height = str(self.height)
        width = str(self.width)
        return "[{}] ({}) {}/{} - {}/{}".format(name, no, x, y, width, height)
