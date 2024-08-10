#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Prints all integers in a list in reverse order, one per line.

    Args:
        my_list (list, optional): The list of integers to print. Defaults to [].
    """

    for num in reversed(my_list):
        print("{:d}".format(num))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)