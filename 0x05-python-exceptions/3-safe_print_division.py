#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The first integer.
        b (int): The second integer (divisor).

    Returns:
        float: The result of the division, or None if there's a ZeroDivisionError.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result