#!/usr/bin/python3


def read_file(filename=""):
  """Reads a text file (UTF-8) and prints its content to stdout.

  Args:
    filename (str, optional): The name of the file to read. Defaults to "".
  """
  # Open the file in read mode with UTF-8 encoding using the with statement
  with open(filename, 'r', encoding="utf-8") as file:
    # Read the entire content of the file
    content = file.read()
    # Print the content to stdout
    print(content)

#Example usage (uncomment for testing)
# read_file("my_file_0.txt")