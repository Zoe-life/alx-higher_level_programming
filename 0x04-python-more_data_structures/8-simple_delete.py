#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary (if it exists).

    Args:
        a_dictionary (dict): The dictionary to modify.
        key (str, optional): The key to delete. Defaults to "".

    Returns:
        dict: The modified dictionary (unchanged if key doesn't exist).
    """

    # Check if key exists in the dictionary using 'in' operator
    if key in a_dictionary:
        # Delete the key using del keyword
        del a_dictionary[key]
    return a_dictionary
