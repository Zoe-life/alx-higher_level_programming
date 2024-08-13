#!/usr/bin/python3


def append_write(filename="", text=""):
  """Appends a string to the end of a text file (UTF-8) and returns the number of characters written.

  Args:
      filename (str, optional): The name of the file to append to. Defaults to "".
      text (str, optional): The string to append to the file. Defaults to "".

  Returns:
      int: The number of characters appended to the file.
  """
  # Open the file in append mode with UTF-8 encoding using the with statement
  with open(filename, 'a', encoding="utf-8") as file:
    # Write the text to the file
    characters_written = file.write(text)
    # Return the number of characters written
    return characters_written


# Example usage (uncomment for testing)
nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)