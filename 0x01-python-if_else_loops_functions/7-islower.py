def islower(c):
    """
    Checks if a character is lowercase.

    Args:
        c (str): The character to check.

    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')  # Check ASCII range for lowercase

# This line is not executed when the module is imported
if __name__ == "__main__":
    print("Say something! (won't be executed when imported)")