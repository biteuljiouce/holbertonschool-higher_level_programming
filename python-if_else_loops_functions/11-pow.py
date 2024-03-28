#!/usr/bin/python3
def pow(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("args must be integer")
    return a ** b
