#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for c in text:
        new_text += c
        if c in ".?:":
            new_text += "\n\n"
            # Remove leading spaces after newlines
            new_text = new_text.rstrip()

    print(new_text.strip())