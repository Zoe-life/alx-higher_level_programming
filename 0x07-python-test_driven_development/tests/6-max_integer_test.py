#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer  # Import the function to test

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Test case for an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test case for a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test case for a list with multiple elements."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_elements(self):
        """Test case for a list with negative elements."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_elements(self):
        """Test case for a list with mixed elements (positive, negative, zero)."""
        self.assertEqual(max_integer([0, 5, -2]), 5)

if __name__ == "__main__":
    unittest.main()