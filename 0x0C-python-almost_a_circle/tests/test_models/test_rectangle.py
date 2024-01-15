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
