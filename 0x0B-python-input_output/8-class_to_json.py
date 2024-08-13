def class_to_json(obj):
  """Returns a dictionary representation of an object's attributes.

  Args:
      obj: An instance of a class.

  Returns:
      dict: A dictionary containing the serializable attributes of the object.
  """
  # Create an empty dictionary to store the object's attributes
  output_dict = {}
  # Get all public attributes of the object
  attributes = dir(obj)

  # Iterate through the attributes
  for attr in attributes:
    # Skip special methods (methods starting with double underscores)
    if not attr.startswith("__"):
      # Get the value of the attribute
      value = getattr(obj, attr)
      # Check if the value is a serializable data type
      if isinstance(value, (list, dict, str, int, bool)):
        # Add the attribute-value pair to the dictionary
        output_dict[attr] = value

  # Return the dictionary containing the serializable attributes
  return output_dict