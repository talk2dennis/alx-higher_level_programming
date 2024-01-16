#!/usr/bin/python3
"""base module"""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save list of objects of rectangle or square to csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                next(f)
                list_objs = csv.DictReader(f, fieldnames=fieldnames)
                list_dict = [dict([k, int(v)] for k, v in lst_dict.items())
                             for lst_dict in list_objs]
                return [cls.create(**dictionary) for dictionary in list_dict]
        except IOError:
            return "[]"

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module
        Args:
            list_rectangles (list): list of rectangles
            list_squares (list): list of square instances
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#eaff7b")
        turt.pensize(2)
        turt.shape("turtle")

        turt.color("#000000")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for i in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#000000")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for i in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
