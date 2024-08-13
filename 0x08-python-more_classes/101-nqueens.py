#!/usr/bin/python3

import sys


def is_safe(row, col, board):
    """
    Checks if placing a queen at (row, col) is safe based on existing queens.

    Args:
        row: The row index.
        col: The column index.
        board: A list representing the chessboard (0 for empty, 1 for queen).

    Returns:
        True if the position is safe, False otherwise.
    """
    # Check columns on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):
    """
    Solves the N-Queens problem using backtracking.

    Args:
        board: A list representing the chessboard (0 for empty, 1 for queen).
        col: The current column index.

    Returns:
        True if a solution is found, False otherwise.
    """
    if col >= len(board):
        return True  # All queens placed

    for i in range(len(board)):
        if is_safe(i, col, board):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack if placement doesn't lead to a solution

    return False


def print_solution(board):
    """
    Prints a chessboard representation of the solution.
    """
    for row in board:
        for col in row:
            if col == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def main():
    """
    Main function that validates input and calls the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    board = [[0] * n for _ in range(n)]  # Initialize empty board

    if solve_n_queens(board, 0):
        print_solution(board)
    else:
        print("Solution does not exist")


if __name__ == "__main__":
    main()