#!/usr/bin/python3


def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format() if the value is an integer type.

    Args:
        value: The value to be checked and printed.

    Returns:
        bool: True if the value is an integer and printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        return False