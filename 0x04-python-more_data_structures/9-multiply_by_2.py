#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    tup = a_dictionary.items()
    return dict(map(lambda key_value: (key_value[0], key_value[1] * 2), tup))
