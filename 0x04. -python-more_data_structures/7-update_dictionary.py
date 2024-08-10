#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Updates or adds a key-value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to modify.
        key (str): The key to update or add.
        value (any): The value to associate with the key.

    Returns:
        dict: The modified dictionary.
    """

    # Update or add the key-value pair
    a_dictionary[key] = value
    return a_dictionary