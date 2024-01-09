#!/usr/bin/python3
"""converts from json"""
import json


def from_json_string(my_str):
    """from_json_string - converts from json to strings"""
    return json.loads(my_str)
