#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    """ Handling negatives """
    last_digit_1 = number % 10 if number >= 0 else -(number % -10)
    return str(last_digit_1)


# Extract the sign from the original number
sign = "-" if number < 0 else ""  # Empty string for positive numbers


last_digit_str = last_digit(number)
number_str1 = str(number)
if number_str1 > '0' and last_digit_str > '5':
    print(f"Last digit of {number} is {sign}{last_digit_str}"
          " and is greater than 5")
elif number_str1 >= '0' and last_digit_str == '0':
    print(f"Last digit of {number} is {sign}{last_digit_str}"
          " and is 0")
else:
    print(f"Last digit of {number} is {sign}{last_digit_str}"
          " and is less than 6 and not 0")
