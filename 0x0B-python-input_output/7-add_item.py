#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
from sys import argv


if __name__ == "__main__":
    save_filename = "add_item.json"
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        my_obj = load_from_json_file(save_filename)
    except FileNotFoundError:
        my_obj = []

    my_obj.extend(argv[1:])
    save_to_json_file(my_obj, save_filename)
