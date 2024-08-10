#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest integer in a list, handling empty lists.

    Args:
        my_list (list, optional): The list of integers to check. Defaults to [].

    Returns:
        int: The biggest integer in the list, or None if the list is empty.
    """

    if not my_list:
        return None

    # Initialize variable to store the first element as a starting point
    largest = my_list[0]

    # Iterate through the list starting from the second element
    for num in my_list[1:]:
        if num > largest:
            largest = num

    return largest


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))