#!/usr/bin/python3
"""
student class
Arthor: Adigwe Dennis
"""


class Student:
    """
    Defines class Student
    Args:
        first_name (str): first_name of the student
        last_name (str): last name of student
        age (int): age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj = vars(self).copy()
        if type(attrs) is list:
            filtered_obj = {}
            for attr in attrs:
                if type(attr) is not str:
                    return obj
                if attr in obj:
                    filtered_obj[attr] = obj[attr]
            return filtered_obj
        return obj
