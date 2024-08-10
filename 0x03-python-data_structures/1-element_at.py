#!/usr/bin/python3


def element_at(my_list, idx):
    """Retrieves an element from a list based on its index, similar to C.

    Args:
        my_list (list): The list to access.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index or None if the index is invalid.
    """

    list_length = len(my_list)

    if idx < 0 or idx >= list_length:
        return None
    else:
        return my_list[idx]


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    element = element_at(my_list, idx)
    print(f"Element at index {idx} is {element}")