#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list, handling invalid indices.

    Args:
        my_list (list, optional): The list to modify. Defaults to [].
        idx (int, optional): The index of the item to delete. Defaults to 0.

    Returns:
        list: A new list with the item at the specified index removed, or the original list if the index is invalid.
    """

    list_length = len(my_list)

    if idx < 0 or idx >= list_length:
        return my_list.copy()  # Return a copy of the original list

    # Create a new list to avoid modifying the original
    new_list = []
    for i in range(list_length):
        # Skip the element at the specified index
        if i != idx:
            new_list.append(my_list[i])

    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)