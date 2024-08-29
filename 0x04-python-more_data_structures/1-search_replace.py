#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a list with another element.

    Args:
        my_list (list): The original list.
        search (any): The element to replace.
        replace (any): The element to replace with.

    Returns:
        list: A new list with all occurrences of 'search' replaced by
        'replace'.
    """

    new_list = []
    for element in my_list:
        # Check if element is not equal to the element to be replaced
        if element != search:
            new_list.append(element)
        else:
            # If element matches, append the replacement
            new_list.append(replace)
    return new_list
