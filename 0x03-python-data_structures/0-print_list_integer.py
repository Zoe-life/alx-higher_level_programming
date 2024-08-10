#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """Prints all integers in a list on separate lines.

    Args:
        my_list (list, optional): The list of integers to print. Defaults to [].
    """
    for num in my_list:
        print("{:d}".format(num))


if __name__ == "__main__":
    print_list_integer([1, 2, 3, 4, 5])