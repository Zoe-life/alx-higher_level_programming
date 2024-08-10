#!/usr/bin/python3
"""
This program prints the number and list of arguments passed to it.
"""

import sys

# Get the number of arguments
num_args = len(sys.argv) - 1  # Subtract script name

# Print the main message
if num_args == 0:
    print("0 arguments.")
else:
    print("{} argument{}".format(num_args, "s" if num_args > 1 else ""))

# Print individual arguments (if any)
if num_args > 0:
    for i in range(1, num_args + 1):
        print("{:d}: {}".format(i, sys.argv[i]))