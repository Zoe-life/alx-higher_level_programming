def pow(a, b):
    """
    Calculates a raised to the power of b (a ^ b).

    Args:
        a (int): The base number.
        b (int): The exponent.

    Returns:
        int: The result of a raised to the power of b.
    """
    
    result = 1
    if b == 0:  # Handle zero exponent case
        return 1
    if b < 0:  # Handle negative exponent (a^-b = 1/a^b)
        a = 1 / a
        b = abs(b)  # Convert exponent to positive
    for _ in range(b):
        result *= a
    return result

# This line is not executed when the module is imported
if __name__ == "__main__":
    print("Say something! (won't be executed when imported)")