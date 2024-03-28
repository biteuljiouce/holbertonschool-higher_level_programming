#!/usr/bin/python3
def uppercase(input):
    if not type(input) is str:
        raise TypeError("arg must be a string")
    for c in input:
        code = ord(c)
        newChar = c
        if code >= 97 and code <= 122:
            newChar = chr(code-32)
        print("{}".format(newChar), end="")
    else:
        print("\n", end="")
