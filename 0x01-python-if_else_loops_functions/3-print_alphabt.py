#!/usr/bin/python3

for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in 'qe':  # Check if character is not 'q' or 'e'
        print(chr(char), end='')