def magic_calculation(a, b):
  """
  Performs a magic calculation based on a and b.

  Args:
      a: The first number.
      b: The second number.

  Returns:
      The result of the magic calculation.
  """

  if a < b:
    c = add(a, b)
    for i in range(4, 6):
      c = add(c, i)
    return c
  else:
    return sub(a, b)

# Simulate importing add and sub from another module
add = lambda x, y: x + y  # Add function
sub = lambda x, y: x - y  # Subtract function