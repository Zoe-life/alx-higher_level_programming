class Student:
  """A class representing a student."""

  def __init__(self, first_name, last_name, age):
    """Initializes a Student instance.

    Args:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def to_json(self, attrs=None):
    """Returns a dictionary representation of the student instance.

    Args:
        attrs (list, optional): A list of attribute names to include. Defaults to None.

    Returns:
        dict: A dictionary containing the student's attributes (or filtered attributes).
    """
    # Create an empty dictionary to store the attributes
    output_dict = {}
    # If attrs is None, include all attributes
    if attrs is None:
      attributes = dir(self)
      for attr in attributes:
        if not attr.startswith("__"):
          value = getattr(self, attr)
          if isinstance(value, (list, dict, str, int, bool)):
            output_dict[attr] = value
    # If attrs is a list, include only those attributes
    else:
      for attr in attrs:
        if hasattr(self, attr):
          value = getattr(self, attr)
          if isinstance(value, (list, dict, str, int, bool)):
            output_dict[attr] = value

    # Return the dictionary
    return output_dict