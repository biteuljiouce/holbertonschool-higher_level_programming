#!/usr/bin/python3
# 2-matrix_divided.py
"""
    This module deals with matrix calculation.
"""

def matrix_divided(matrix, div):
    """
    Use a matrix of float or integer.
    Divide each term of the matrix by the given int or float.
    """
    # Cannot divide by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Check if each row has same size
    for line in matrix:
        if len(line) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    # Check if all value are int or float
    # if ok, calculate result
    res_matrix = []
    res_line = []
    for line in matrix:
        for val in line:
            if not isinstance(val, int) and not isinstance(val, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                res_line.append(round(val / div, 2))
        else:
            res_matrix.append(res_line)
    return res_matrix
