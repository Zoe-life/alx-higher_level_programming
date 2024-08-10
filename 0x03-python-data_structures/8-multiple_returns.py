#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns a tuple containing the length of a string and its first character.

    Args:
        sentence (str): The string to analyze.

    Returns:
        tuple: A tuple containing the length of the string and its first character (or None if empty).
    """

    if not sentence:  # Check for an empty string
        return (0, None)
    else:
        return (len(sentence), sentence[0])


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))