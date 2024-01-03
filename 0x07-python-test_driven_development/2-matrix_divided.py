#!/usr/bin/python3
"""
matrix_divided - a function that divides list of lists of integers or floats.
Args: matrix of lists
Return: list of lists
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - A function that returns the result\
            of dividing list of lists.
    Args:
        matrix: lisit of lists
        div: int
    Raise:
        TypeError: exception with message
        ZeroDivisionError: exception with message
    Return: the result list of lists rounded to 2 decimal places
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = 0
    for lists in matrix:
        if not isinstance(lists, list) or \
                not all(isinstance(item, (int, float)) for item in lists):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    return [[round(element / div, 2) for element in lists] for lists in matrix]
