#!/usr/bin/python3

a = 10
b = 89

# Swap the values of a and b without using a temporary variable
a, b = b, a  # Destructuring assignment

print("a={} - b={}".format(a, b))