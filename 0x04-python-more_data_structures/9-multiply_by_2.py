#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Creates a new dictionary with values multiplied by 2.

    Args:
        a_dictionary (dict): The original dictionary.

    Returns:
        dict: A new dictionary with values doubled.
    """

    new_dict = {}
    for key, value in a_dictionary.items():
        # Create new key-value pair with doubled value
        new_dict[key] = value * 2
    return new_dict
