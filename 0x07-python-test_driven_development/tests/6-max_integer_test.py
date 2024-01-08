#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class testMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])"""

    def test_max(self):
        """text case for max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_float(self):
        """test case for max float"""
        self.assertEqual(max_integer([1, 4.6, 3.5, 4.0]), 4.6)

    def test_max_empty(self):
        """test case for empty value"""
        self.assertEqual(max_integer(empty), None)

    def test_max_empty(self):
        """test case for empty string"""
        self.assertEqual(max_integer(""), None)

    def test_max_neg(self):
        """test for one negative number"""
        self.assertEqual(max_integer([20, -10, 3, 4.0]), 20)

    def test_max_negs(self):
        """test with more negative numbers"""
        self.assertEqual(max_integer([-20, -10, -3, -4.0]), -3)

    def test_max_one(self):
        """test with one element"""
        self.assertEqual(max_integer([20]), 20)

if __name__ == '__main__':
    unittest.main()
