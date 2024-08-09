#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
        my_list (list, optional): The list to print elements from. Defaults to [].
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        int: The actual number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()  # Print a newline after all elements
    return count