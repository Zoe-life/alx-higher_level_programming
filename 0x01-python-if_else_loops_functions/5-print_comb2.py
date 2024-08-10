#!/usr/bin/python3

for i in range(100):
    print("{:02}, ".format(i), end='')  # Print first digit pair with comma, space
print(f"{i+1}")  # Print last number (i+1 for 0-based indexing) without comma