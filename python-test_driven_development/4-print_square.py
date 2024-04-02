#!/usr/bin/python3

"""Module contains function to draw a square."""

def print_square(size):
    """
        Draw a square with character #.

        Arg :
            size : integer
    """
    for i in range(size):
        for j in range(size):
            print("#", end="")
        else:
            print("\n", end="")
    if size == 0:
        print("\n", end="")
