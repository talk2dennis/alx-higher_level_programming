#!/usr/bin/python3
"""creates unittest for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Difines unnitest test case for the base class"""
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

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1, 1)
        self.assertEqual(b2, 2)


if __name__ == "__main__":
    unittest.main()
