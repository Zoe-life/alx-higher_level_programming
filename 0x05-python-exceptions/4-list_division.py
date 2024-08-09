#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists element-wise and creates a new list.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list (divisor list).
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list with the division results, or an empty list if errors occur.
    """
    new_list = []
    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                new_list.append(0)
            elif my_list_2[i] == 0:
                print("division by 0")
                new_list.append(0)
            else:
                new_list.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list