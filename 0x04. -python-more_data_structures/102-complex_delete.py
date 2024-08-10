#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """
    Deletes all keys with a specific value from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to modify.
        value: The value to search for and delete associated keys.

    Returns:
        dict: The modified dictionary (unchanged if no keys have the value).
    """

    # Create a copy of the dictionary to avoid modifying the original
    new_dict = a_dictionary.copy()

    # Iterate through keys in a copy to safely delete
    for key in list(new_dict.keys()):
        if new_dict[key] == value:
            del new_dict[key]

    return new_dict