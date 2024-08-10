#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific index without modifying the original list, similar to C.

    Args:
        my_list (list): The list to consider.
        idx (int): The index of the element to replace.
        element: The new element to insert.

    Returns:
        A copy of the modified list, or the original list if the index is invalid.
    """

    list_length = len(my_list)

    if idx < 0 or idx >= list_length:
        return my_list.copy()  # Return a copy of the original list
    else:
        # Create a copy of the list to avoid modifying the original
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)  # This will print the original list since it wasn't modified