def magic_calculation(a, b):
    """
    Performs a "magic" calculation based on the provided operands.

    Args:
        a (int): The first operand.
        b (int): The second operand.

    Returns:
        int: The result of the calculation.

    Raises:
        Exception: If a is less than or equal to b.
    """
    result = 0
    for i in range(1, 3):
        try:
            if a <= b:
                raise Exception("Too far")
            result += a ** b // i
        except Exception as e:
            print(e)
            result = b + a
            break

    return result