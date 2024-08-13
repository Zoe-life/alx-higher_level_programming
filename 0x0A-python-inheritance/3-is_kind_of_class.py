#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of a specific class or its subclasses.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the class or its subclasses, False otherwise.
    """

    return isinstance(obj, a_class)