#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
  """Writes an object to a text file using its JSON representation.

  Args:
      my_obj: The object to serialize and write to the file.
      filename (str): The name of the file to write to.
  """
  # Try to serialize the object with json.dumps
  try:
    json_string = json.dumps(my_obj)
  # If there's a serialization error, return without writing
  except (TypeError, OverflowError) as e:
    return

  # Open the file in write mode with UTF-8 encoding using the with statement
  with open(filename, 'w', encoding="utf-8") as file:
    # Write the JSON string to the file
    file.write(json_string)


# Example usage (uncomment for testing)
# filename = "my_list.json"
# my_list = [1, 2, 3]
# save_to_json_file(my_list, filename)

# filename = "my_dict.json"
# my_dict = {
#     "id": 12,
#     "name": "John",
#     "places": ["San Francisco", "Tokyo"],
#     "is_active": True,
#     "info": {
#         "age": 36,
#         "average": 3.14
#     }
# }
# save_to_json_file(my_dict, filename)

# try:
#     filename = "my_set.json"
#     my_set = {132, 3}
#     save_to_json_file(my_set, filename)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))