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
        if list_dictionaries is None or not list_dictionaries:
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

    @classmethod
    def load_from_file(cls):
        """
        load_from_file - that returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                dictionaries = Base.from_json_string(f.read())
            return [cls.create(**dictionary) for dictionary in dictionaries]
        except IOError:
            return []

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - returns the list of the JSON string
                           representation json_string
        Args:
            json_string: is a string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create - eturns an instance with all attributes already set
        Args:
            dictionary (dict): double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(15, 4)
            else:
                new_instance = cls(15)
            new_instance.update(**dictionary)
            return new_instance
