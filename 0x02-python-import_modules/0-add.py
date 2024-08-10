#!/usr/bin/python3
"""
This program imports the add function from add_0.py and prints the sum of 1 and 2.
"""

# Import the add function from add_0.py
from add_0 import add

# Assign values to variables
a = 1
b = 2

# Calculate the sum using the add function
sum = add(a, b)

# Print the formatted output
print("{} + {} = {}".format(a, b, sum))