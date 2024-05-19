#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    """ Handling negatives """
    return number % 10 if number >= 0 else - (number % -10)


last = last_digit(number)
number_str = str(last)
number_str1 = str(number)
if number_str1 > '0' and number_str > '5':
    print(f"""Last digit of {number} is {number_str} and is greater than 5""")
elif number_str1 >= '0' and number_str == '0':
    print(f"""Last digit of {number} is {number_str} and is 0""")
else:
    print(f"""Last digit of {number} is {number_str} and is less than 6 and not 0""")
