#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first number.
        b (int, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The sum of a and b, cast to an integer if necessary.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)