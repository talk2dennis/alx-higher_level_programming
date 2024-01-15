#!/usr/bin/python3
"""creates unittest for rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os



class TestRectangle(unittest.TestCase):
    """ Difines test casses for Rectangle Class"""
    b1 = Base()
    b2 = Base(None)
    b3 = Base(10)
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    s1 = Square(10, 7, 2, 8)
    s2 = Square(10, 5, 3, 6)

    @classmethod
    def tearDown(self):
        """ deletes all the created files for the test cases"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_is_base(self):
        self.assertIsInstance(self.b1, Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()
    def test_arg1(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_arg2(self):
        self.assertEqual(self.r1.id, 5)

    def test_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(self.__width))

    def test_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(self.__height))

    def test_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(self.__x))

    def test_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(self.__y))

    def test_width_getter(self):
        self.assertEqual(10, self.r1.width)

    def test_width_setter(self):
        self.r1.width = 12
        self.assertEqual(12, self.r1.width)

    def test_height_getter(self):
        self.assertEqual(7, self.r1.height)

    def test_height_setter(self):
        self.r1.height = 12
        self.assertEqual(12, self.r1.height)

    def test_x_getter(self):
        self.assertEqual(2, self.r1.x)

    def test_x_setter(self):
        self.r1.x = 5
        self.assertEqual(5, self.r1.x)

    def test_y_getter(self):
        self.assertEqual(8, self.r1.y)

    def test_y_setter(self):
        self.r1.y = 5
        self.assertEqual(5, self.r1.y)

    def test_no_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)

    def test_no_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 10)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "10")

    def test_0_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10)

    def test_0_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(15, 0)




