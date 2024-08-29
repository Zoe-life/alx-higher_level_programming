#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """Squares all integers in a matrix using map."""
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
