#!/usr/bin/python3

"""Define a class Square."""


class Square:

    """Represents a square (geometrical object)."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (
            len(position) != 2
            or not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """Draw the square with character #."""
        if self.__size == 0:
            print("\n", end="")
            return
        for i in range(self.__position[1]):
            print("\n", end="")
        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                char = "#"
                if j < self.__position[0]:
                    char = " "
                print("{}".format(char), end="")
            else:
                print("\n", end="")

    def area(self):
        """Returns current square area."""
        return self.__size ** 2
