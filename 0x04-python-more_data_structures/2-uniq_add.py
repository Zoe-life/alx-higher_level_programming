#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Args:
        my_list (list, optional): The list containing integers. Defaults to [].

    Returns:
        int: The sum of unique integers in the list.
    """

    seen = set()
    total = 0
    for element in my_list:
        # Check if element is an integer and not already seen
        if isinstance(element, int) and element not in seen:
            seen.add(element)
            total += element
    return total
