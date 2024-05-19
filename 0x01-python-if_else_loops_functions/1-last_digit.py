#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    """ Handling negatives """
    if number >= 0:
        return number % 10
    else:
        return -(number % -10)


last = last_digit(number)
number_str = str(last)
if number_str > '5':
    print(f"Last digit of {number} is {number_str}\
            and is greater than 5")
elif number_str == '0':
    print(f"Last digit of {number} is {number_str}\
            and is 0")
elif number:
    print(f"Last digit of {number} is {number_str}\
            and is less than 6 and not 0")
