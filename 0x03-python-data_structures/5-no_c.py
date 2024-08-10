#!/usr/bin/python3


def no_c(my_string):
    """Removes all characters 'c' and 'C' (case-insensitive) from a string.

    Args:
        my_string (str): The string to modify.

    Returns:
        str: The new string without 'c' or 'C' characters.
    """

    new_string = ""
    for char in my_string:
        if char.lower() != "c":
            new_string += char

    return new_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))