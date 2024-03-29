#!/usr/bin/python3

"""Define a class Square."""


class Square:

    """Represents a square (geometrical object)."""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Returns current square area."""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Draw the square with character #."""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            else:
                print("\n", end="")
        if self.__size == 0:
            print("\n", end="")
