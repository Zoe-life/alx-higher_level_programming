#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Squares the elements of a matrix.

    Args:
        matrix (list, optional): A 2D list representing the matrix.
            Defaults to [].

    Returns:
        list: A new matrix with the squared elements.
    """

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * element)
        new_matrix.append(new_row)
    return new_matrix