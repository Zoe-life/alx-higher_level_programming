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

  def to_json(self):
    """Returns a dictionary representation of the student instance.

    Returns:
        dict: A dictionary containing the student's attributes.
    """
    # Create an empty dictionary to store the attributes
    output_dict = {}
    # Add student attributes as key-value pairs
    output_dict["first_name"] = self.first_name
    output_dict["last_name"] = self.last_name
    output_dict["age"] = self.age
    # Return the dictionary
    return output_dict