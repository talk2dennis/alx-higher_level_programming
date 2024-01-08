#!/usr/bin/python3
"""print_sorted"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """print_sorted - returns the the list obj in the sorted order"""
        my_list = sorted(self)
        print(my_list)
