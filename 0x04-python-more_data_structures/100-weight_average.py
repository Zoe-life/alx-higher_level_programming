#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    Calculates the weighted average of integers in a tuple list.

    Args:
        my_list (list, optional): The list of tuples containing scores
        and weights. Defaults to [].

    Returns:
        float: The weighted average of the integers (0 if empty list).
    """

    # Initialize variables to handle empty list
    numerator = 0
    denominator = 0

    for score, weight in my_list:
        # Ensure both score and weight are integers
        if isinstance(score, int) and isinstance(weight, int):
            numerator += score * weight
            denominator += weight

    # Calculate and return weighted average (0 if denominator is 0)
    return numerator / denominator if denominator else 0
