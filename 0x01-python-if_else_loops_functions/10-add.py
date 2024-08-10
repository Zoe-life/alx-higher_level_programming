def add(a, b):
    """
    Adds two integers and returns the sum.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    
    # Simulate addition using bitwise operations
    while b != 0:
        carry = a & b  # Get the carry bit (overflow from addition)
        a = a ^ b     # Perform XOR to get the sum without carry
        b = carry << 1 # Shift the carry to the left for the next iteration
    return a  # Final sum is in a

# This line is not executed when the module is imported
if __name__ == "__main__":
    print("Say something! (won't be executed when imported)")