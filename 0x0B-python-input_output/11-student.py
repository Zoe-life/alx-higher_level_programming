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
    # Same logic as in 10-student.py for attribute selection and serialization

  def reload_from_json(self, json):
    """Updates the Student instance attributes based on a dictionary.

    Args:
        json (dict): A dictionary representing the student's attributes.
    """
    # Update attributes based on the dictionary (json)
    for key, value in json.items():
      if hasattr(self, key):
        setattr(self, key, value)