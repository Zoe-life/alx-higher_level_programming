#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Args:
        my_list (list, optional): The list to print elements from. Defaults to [].
        x (int, optional): The number of elements to access. Defaults to 0.

    Returns:
        int: The actual number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break
    print()  # Print a newline after all elements
    return count