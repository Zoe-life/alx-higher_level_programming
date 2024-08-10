#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (np.ndarray): The first matrix (NumPy array).
        m_b (np.ndarray): The second matrix (NumPy array).

    Returns:
        np.ndarray: The resulting product matrix, or None if multiplication is not possible.

    Raises:
        TypeError:
            - If `m_a` or `m_b` is not a NumPy array.
            - If `m_a` and `m_b` cannot be multiplied due to incompatible shapes.
    """

    if not isinstance(m_a, np.ndarray) or not isinstance(m_b, np.ndarray):
        raise TypeError("m_a and m_b must be NumPy arrays")

    if not np.matmul.shape_check((m_a, m_b)):
        raise TypeError("m_a and m_b cannot be multiplied")

    return np.matmul(m_a, m_b)