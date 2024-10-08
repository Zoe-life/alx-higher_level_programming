#!/usr/bin/python3
import json


def from_json_string(my_str):
  """Returns an object (Python data structure) represented by a JSON string.

  Args:
      my_str (str): The JSON string to deserialize.

  Returns:
      object: The Python data structure represented by the JSON string, 
              or None if the string is invalid.
  """
  # Try to deserialize the JSON string with json.loads
  try:
    return json.loads(my_str)
  # If there's a deserialization error, return None
  except (json.JSONDecodeError, TypeError) as e:
    return None


# Example usage (uncomment for testing)
# s_my_list = "[1, 2, 3]"
# my_list = from_json_string(s_my_list)
# print(my_list)
# print(type(my_list))

# s_my_dict = """
# {"is_active": true, "info": {"age": 36, "average": 3.14}, 
# "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
# """
# my_dict = from_json_string(s_my_dict)
# print(my_dict)
# print(type(my_dict))

# try:
#     s_my_dict = """
#     {"is_active": true, 12 }
#     """
#     my_dict = from_json_string(s_my_dict)
#     print(my_dict)
#     print(type(my_dict))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))