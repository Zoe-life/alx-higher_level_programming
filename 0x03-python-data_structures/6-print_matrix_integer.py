#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers, each integer on a separate line.

    Args:
        matrix (list, optional): The matrix of integers to print. Defaults to [].
    """

    for row in matrix:
        # Print elements of a row, separated by spaces
        print(*row, sep=" ")
        # Add a newline after each row (except the last one)
        if row != matrix[-1]:
            print()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()