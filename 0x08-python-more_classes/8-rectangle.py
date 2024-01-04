#!/usr/bin/python3
"""
a class that represents a retangle
"""


class Rectangle:
    """
    my retangle class
    Args:
        width (int): the height of our rectangle
        height (int): the height of our rectangle
        print_symbol (any): the symbol of our rectangle
        number_of_instances (int): increments at every instance creation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialising the Retangle class """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares two instances of rectangle class
        and returns the the bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """
        returns the string representation of the class
        """
        string = ""
        if self.__height == 0 or self.width == 0:
            return string
        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if i < ((self.__height) - 1):
                string += '\n'
        return string

    def __repr__(self):
        """
        returns the representation of the class
        """
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """
        trigers when the instance of the class is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
