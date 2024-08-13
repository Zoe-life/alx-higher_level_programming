#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    This function checks if an object is an instance of a class that directly or indirectly inherited from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against (base class).

    Returns:
        True if the object's type is a subclass (direct or indirect) of the specified class, False otherwise.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class