#!/usr/bin/python3
"""
This program performs basic arithmetic operations based on user input.
"""

import sys

from calculator_1 import add, sub, mul, div


def main():
    """Handles user input and performs calculations."""

    # Check if there are exactly 3 arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Check if the operator is valid
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the calculation based on the operator
    result = None
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)

    # Print the result
    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()