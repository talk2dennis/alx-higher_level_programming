#!/usr/bin/python3
"""creates unittest for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestBase(unittest.TestCase):
    """ Difines unnitest test case for the base class"""
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

    def test_no_arg(self):
        self.assertEqual(self.b1.id, 1)

    def test_arg_none(self):
        self.assertEqual(self.b2.id, 2)

    def test_arg(self):
        self.assertEqual(self.b3.id, 10)

    def test_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_id_public(self):
        b = Base(10)
        b.id = 5
        self.assertEqual(b.id, 5)

    def test_id_str(self):
        self.assertEqual("id", Base("id").id)

    def test_id_lst(self):
        self.assertEqual("[id]", Base("[id]").id)

    def test_id_dict(self):
        self.assertEqual("{id: 10", Base("{id: 10").id)

    def test_id_range(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_to_json_string(self):
        self.assertEqual(str, type(Base.to_json_string([self.r1.to_dictionary()])))

    def test_to_json_string_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_save_to_file_rectangle1(self):
        Rectangle.save_to_file([self.r1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)
    
    def test_save_to_file_arg1(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_arg2(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])


    def test_save_to_file_rectangle2(self):
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_square1(self):
        Rectangle.save_to_file([self.s1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_filename(self):
        Base.save_to_file([self.s1])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
    
    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())


if __name__ == "__main__":
    unittest.main()
