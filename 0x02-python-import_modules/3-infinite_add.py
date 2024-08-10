#!/usr/bin/python3
"""
This program calculates the sum of all arguments passed to it.
"""

import sys

if __name__ == "__main__":
    # Convert arguments to integers and sum them
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)