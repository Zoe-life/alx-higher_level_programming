#!/usr/bin/python3


def lookup(obj):
    """
    This function returns a list of attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings containing the names of all attributes and methods of the object.
    """

    return dir(obj)