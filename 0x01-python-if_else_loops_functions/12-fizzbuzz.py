def fizzbuzz():
  """
  Prints the numbers from 1 to 100 with FizzBuzz logic.
  """
  for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:  # Check for FizzBuzz
        print("FizzBuzz", end=' ')
    elif num % 3 == 0:  # Check for Fizz
        print("Fizz", end=' ')
    elif num % 5 == 0:  # Check for Buzz
        print("Buzz", end=' ')
    else:
        print(num, end=' ')

# This line is not executed when the module is imported
if __name__ == "__main__":
  fizzbuzz()