#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class testMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])"""

    def test_max(self):
        """
        text case for max_integer
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_float(self):
        """test case for max float"""
        self.assertEqual(max_integer([1, 4.6, 3.5, 4.0]), 4.6)

    def test_max_empty(self):
        """test case for empty value"""
        self.assertEqual(max_integer(empty), None)

    def test_max_empty(self):
        """test case for empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
