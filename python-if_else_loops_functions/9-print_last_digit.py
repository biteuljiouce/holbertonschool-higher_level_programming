#!/usr/bin/python3
def print_last_digit(input):
    if not type(input) is int:
        raise TypeError("arg must be a integer")
    inputAsStr = str(input)
    lastChar = inputAsStr[len(inputAsStr)-1]
    print("{}".format(lastChar),end="")
