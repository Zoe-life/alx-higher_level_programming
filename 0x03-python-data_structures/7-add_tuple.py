#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds elements of two tuples, handling cases of different lengths.

    Args:
        tuple_a (tuple, optional): The first tuple. Defaults to an empty tuple.
        tuple_b (tuple, optional): The second tuple. Defaults to an empty tuple.

    Returns:
        tuple: A new tuple containing the sum of corresponding elements.
    """

    # Extract elements with a maximum of 2 elements
    a_elements = tuple_a[:2] + (0, ) * (2 - len(tuple_a))  # Pad with 0s if needed
    b_elements = tuple_b[:2] + (0, ) * (2 - len(tuple_b))

    # Add corresponding elements
    sum_elements = tuple(a + b for a, b in zip(a_elements, b_elements))

    return sum_elements


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))