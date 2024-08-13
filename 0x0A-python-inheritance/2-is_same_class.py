#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    This function checks if an object is an exact instance of a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an exact instance of the class, False otherwise.
    """

    return type(obj) == a_class