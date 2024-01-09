#!/usr/bin/python3
"""writes json obj to a file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file- a function that saves object to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
