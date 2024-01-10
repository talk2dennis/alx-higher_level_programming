#!/usr/bin/python3
"""class_to_json"""


def class_to_json(obj):
    """check if obj has attr dict"""
    if hasattr(obj, "__dict__"):
        return vars(obj).copy()
    return {}
