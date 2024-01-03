#!/usr/bin/python3
"""
text_indentation - Splits a text into sentences using the delimiters '.', '?', and ':'.
"""


def text_indentation(text):
    """
    text_indentation - Splits a text into sentences using the delimiters '.', '?', and ':'.

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
        new_text = (delim + "\n\n").join([word.strip(" ") for word in new_text.split(delim)])
    print(new_text)
