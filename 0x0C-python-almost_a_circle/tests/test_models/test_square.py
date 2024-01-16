#!/usr/bin/python3
"""creates unittest for rectangle class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        # Initialize a Square instance with default values for testing
        self.square = Square(size=5, x=2, y=3, id=1)

    def test_size_property(self):
        self.assertEqual(self.square.size, 5)

    def test_update_method_with_args(self):
        self.square.update(2, 7, 4, 6)
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 6)
        self.assertEqual(self.square.id, 2)

    def test_update_method_with_kwargs(self):
        self.square.update(id=3, size=8, x=1, y=9)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 9)
        self.assertEqual(self.square.id, 3)

    def test_to_dictionary_method(self):
        square_dict = self.square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

    def test_str_method(self):
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(self.square), expected_str)

if __name__ == '__main__':
    unittest.main()
