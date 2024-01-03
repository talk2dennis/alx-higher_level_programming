#!/usr/bin/python3
"""
say_my_name - A function that takes your first and last name
Args: takes first and last name
Return: your full name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: A function that prints your full name
    Args:
        first_name: a string
        last_name: a string
    Return: returns the full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
