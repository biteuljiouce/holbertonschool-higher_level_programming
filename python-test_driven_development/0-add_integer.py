#!/usr/bin/python3
# 0-add_integer.py
'''
    This module ideals with interger calculation.
'''


def add_integer(a, b=98):
    '''
        This function add two given integers or floats.
    '''

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError('a must be an integer')

    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return a + b
