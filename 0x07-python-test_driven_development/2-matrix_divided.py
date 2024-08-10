#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats representing the matrix.
        div (int or float): The number by which to divide all elements.

    Raises:
        TypeError:
            - If `matrix` is not a list of lists of integers or floats.
            - If each row of the `matrix` does not have the same size.
            - If `div` is not a number (integer or float).
        ZeroDivisionError: If `div` is equal to zero.

    Returns:
        list: A new matrix containing the divided elements, rounded to 2 decimal places.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) and all(isinstance(item, (int, float)) for item in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(len(row) == cols for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]