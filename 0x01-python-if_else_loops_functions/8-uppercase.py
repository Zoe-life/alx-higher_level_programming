def uppercase(string):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        string (str): The string to be converted to uppercase.
    """
    for char in string:
        new_char = chr(ord(char) - 32 if ord('a') <= ord(char) <= ord('z') else ord(char))  # Convert lowercase to uppercase
        print(new_char, end='')
    print('')  # Print newline outside the loop

# This line is not executed when the module is imported
if __name__ == "__main__":
    print("Say something! (won't be executed when imported)")