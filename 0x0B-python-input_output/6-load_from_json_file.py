#!/usr/bin/python3
"""reads json obj from a file"""
import json


def load_from_json_file(filename):
    """load_from_json_file - loads from a json file and returns the string"""
    with open(filename, encoding="utf-8") as f:
        my_obj = f.read()
        return json.loads(my_obj)
