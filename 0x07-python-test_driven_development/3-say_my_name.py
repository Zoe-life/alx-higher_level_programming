#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """Prints a formatted string with the provided first and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If `first_name` is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    print(f"My name is {first_name} {' ' + last_name if last_name else ''}")