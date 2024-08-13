#!/usr/bin/python3
import json


def load_from_json_file(filename):
  """Creates an object from a JSON file.

  Args:
      filename (str): The name of the JSON file to read.

  Returns:
      object: The Python data structure represented by the JSON file, 
              or None if the file doesn't exist or the JSON is invalid.
  """
  # Try to open the file in read mode with UTF-8 encoding using the with statement
  try:
    with open(filename, 'r', encoding="utf-8") as file:
      # Read the entire content
      content = file.read()
      # Try to deserialize the JSON content
      try:
        return json.loads(content)
      except (json.JSONDecodeError, TypeError) as e:
        return None
  # If the file doesn't exist, return None
  except FileNotFoundError:
    return None


# Example usage (uncomment for testing)
# filename = "my_list.json"
# my_list = load_from_json_file(filename)
# print(my_list)
# print(type(my_list))

# filename = "my_dict.json"
# my_dict = load_from_json_file(filename)
# print(my_dict)
# print(type(my_dict))

# try:
#     filename = "my_set_doesnt_exist.json"
#     my_set = load_from_json_file(filename)
#     print(my_set)
#     print(type(my_set))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     filename = "my_fake.json"
#     my_fake = load_from_json_file(filename)
#     print(my_fake)
#     print(type(my_fake))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))