#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices element-wise.

    Args:
        m_a (list): The first matrix (list of lists of numbers).
        m_b (list): The second matrix (list of lists of numbers).

    Returns:
        list: The resulting product matrix, or None if multiplication is not possible.

    Raises:
        TypeError:
            - If `m_a` or `m_b` is not a list.
            - If `m_a` or `m_b` is a list of lists but contains non-numeric elements.
            - If `m_a` or `m_b` is not a rectangle (rows have different sizes).
            - If `m_a` and `m_b` cannot be multiplied (different column count in A vs. row count in B).
        ValueError:
            - If `m_a` or `m_b` is empty.
    """

    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")

    if not all(all(isinstance(item, (int, float)) for item in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(item, (int, float)) for item in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    cols_a = len(m_a[0])  # Store number of columns in A

    if len(m_b) != cols_a:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]  # Initialize result matrix

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result