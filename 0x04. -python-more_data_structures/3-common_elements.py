#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    Finds the set of common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing the common elements between the two sets.
    """

    # Use set intersection operation for efficient common element finding
    return set_1.intersection(set_2)