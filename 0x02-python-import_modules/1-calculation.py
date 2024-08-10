#!/usr/bin/python3
"""
This program imports functions from calculator_1.py and performs calculations on 10 and 5.
"""

# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Assign values to variables
a = 10
b = 5

# Perform calculations and print results (using only 4 print statements)
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))