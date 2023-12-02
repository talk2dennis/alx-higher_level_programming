#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ""
    for c in my_string:
        if c != "c" and c != "C":
            my_new_string += c
    return my_new_string
