#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Creates a list of booleans indicating whether elements in a list are divisible by 2.

    Args:
        my_list (list, optional): The list of integers to check. Defaults to [].

    Returns:
        list: A new list of booleans (True for even, False for odd) with the same length as the original list.
    """

    result = []
    for num in my_list:
        # Use the remainder operator (%) to check divisibility
        result.append(num % 2 == 0)

    return result


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1