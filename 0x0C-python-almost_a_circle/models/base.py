#!/usr/bin/python3
"""base module"""


class Base:
    """ base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialising the class"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
