#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Finds the set of elements present in only one set (not both).

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing elements present in only one set.
    """

    # Use set symmetric_difference for efficient finding
    return set_1.symmetric_difference(set_2)
