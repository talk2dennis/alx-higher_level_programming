#!/usr/bin/python3
"""
text_indentation - Splits a text into sentences using '.', '?', and ':'.
"""


def text_indentation(text):
    """
    text_indentation - Splits a text into sentences using '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimeters = ".?:"
    new_text = text
    for delim in delimeters:
        new_text = (delim + "\n\n").join([word.strip(" ") for word
                                          in new_text.split(delim)])
    # new_text = new_text[1:(len(new_text) - 2)]
    print(new_text, end='')
