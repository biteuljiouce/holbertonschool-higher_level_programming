#!/usr/bin/python3

"""Module contains function to modify string."""


def text_indentation(text):
    """
        Add 2 new lines after some special char.

        Arg :
            text : string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    special_chars = ('.', '?', ':')
    for c in text:
        if c == ' ' and remove_space:
            pass
        else:
            print(c, end="")
        if c in special_chars:
            print("\n\n", end="")
            remove_space = True
        else:
            remove_space = False
