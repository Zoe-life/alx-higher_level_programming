def print_last_digit(number):
    """
    Prints the last digit of a number.

    Args:
        number (int): The number to get the last digit from.

    Returns:
        int: The last digit of the number.
    """
    print(abs(number) % 10)  # Get absolute value and modulo by 10

# This line is not executed when the module is imported
if __name__ == "__main__":
    print("Say something! (won't be executed when imported)")