def magic_calculation(a, b, c):
  """
  Performs a magic calculation based on the given arguments.

  Args:
      a (int): First argument.
      b (int): Second argument.
      c (int): Third argument.

  Returns:
      int: The result of the calculation.
  """
  if a < b:
    return c
  elif c > b:
    return a + b
  else:
    return a * b - c

# This line is not executed when the module is imported
if __name__ == "__main__":
  print("Say something! (won't be executed when imported)")