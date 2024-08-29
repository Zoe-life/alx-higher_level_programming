#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with keys ordered alphabetically.

    Args:
        a_dictionary (dict): The dictionary to print with sorted keys.
    """

    # Sort keys and iterate in sorted order
    for key in sorted(a_dictionary.keys()):
        # Print key and value pair
        print("{}: {}".format(key, a_dictionary[key]))
