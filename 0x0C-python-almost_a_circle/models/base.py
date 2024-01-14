#!/usr/bin/python3
"""base module"""
import json

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

    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string
        Args:
            list_dictionaries (list): List of dictionaries
        Returns:
            str: JSON-formatted string.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - that writes the JSON string representation
                        of list_objs to a file
        Args:
            list_objs (list): is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                lts = [word.to_dictionary() for word in list_objs]
                f.write(Base.to_json_string(lts))
