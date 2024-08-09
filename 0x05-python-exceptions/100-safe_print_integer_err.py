#!/usr/bin/python3


import sys


def safe_print_integer_err(value):
    """
    Prints an integer and handles errors by writing to standard error.

    Args:
        value: The value to be checked and printed.

    Returns:
        bool: True if the value is an integer and printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        print("Exception: ", file=sys.stderr)
        print("Invalid integer value", file=sys.stderr)
        return False