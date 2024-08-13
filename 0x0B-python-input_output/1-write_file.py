#!/usr/bin/python3


def write_file(filename="", text=""):
  """Writes a string to a text file (UTF-8) and returns the number of characters written.

  Args:
      filename (str, optional): The name of the file to write to. Defaults to "".
      text (str, optional): The string to write to the file. Defaults to "".

  Returns:
      int: The number of characters written to the file.
  """
  # Open the file in write mode with UTF-8 encoding using the with statement
  with open(filename, 'w', encoding="utf-8") as file:
    # Write the text to the file
    characters_written = file.write(text)
    # Return the number of characters written
    return characters_written


# Example usage (uncomment for testing)
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)