#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.

    Args:
        a_dictionary (dict, optional): The dictionary containing
        scores. Defaults to None.

    Returns:
        str: The key with the highest score (None if no scores).
    """

    if not a_dictionary:
        return None  # Return None for empty dictionary

    # Initialize with first key and value
    best_key = list(a_dictionary.keys())[0]
    best_score = a_dictionary[best_key]

    for key, value in a_dictionary.items():
        # Compare current value with best score
        if value > best_score:
            best_key = key
            best_score = value
    return best_key
