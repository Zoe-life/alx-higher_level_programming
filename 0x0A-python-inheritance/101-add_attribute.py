#!/usr/usr/bin/python3


def add_attribute(obj, attr, value):
    """
    Attempts to add a new attribute to an object.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute to add.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object's type doesn't allow adding new attributes.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)