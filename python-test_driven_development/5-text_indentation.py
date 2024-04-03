#!/usr/bin/python3

"""Module contains function to modify string."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    new_line = True
    for c in text:
        if c in special_chars:
            print(c, end='')
            print("\n")
            new_line = True
        else:
            if c.strip():
                print(c, end='')
                new_line = False
            elif not new_line:
                print(c, end='')
