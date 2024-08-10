def remove_char_at(str, n):
  """
  Creates a copy of the string, removing the character at the given index.

  Args:
      str (str): The original string.
      n (int): The index of the character to remove (0-based indexing).

  Returns:
      str: A new string with the character at index n removed.
  """
  new_string = ""
  for i in range(len(str)):
    if i != n:  # Skip the character at index n
      new_string += str[i]
  return new_string

# This line is not executed when the module is imported
if __name__ == "__main__":
  print("Say something! (won't be executed when imported)")