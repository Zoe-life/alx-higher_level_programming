def append_after(filename="", search_string="", new_string=""):
  """Inserts a line of text after each line containing a search string in a file.

  Args:
      filename (str): The name of the file to modify. Defaults to "".
      search_string (str): The string to search for in the file. Defaults to "".
      new_string (str): The line of text to insert after the search string. Defaults to "".
  """
  # Open the file in read mode
  with open(filename, 'r') as f:
    # Read the entire file content
    content = f.read()

  # Split the content into lines
  lines = content.splitlines()

  # Modified content to store the updated lines
  modified_lines = []
  for line in lines:
    # Check if the current line contains the search string
    if search_string in line:
      # Append the original line and the new string
      modified_lines.append(line)
      modified_lines.append(new_string)
    else:
      # Append the original line if no match
      modified_lines.append(line)

  # Join the modified lines with newlines
  joined_content = '\n'.join(modified_lines)

  # Open the file again in write mode
  with open(filename, 'w') as f:
    # Write the updated content to the file
    f.write(joined_content)