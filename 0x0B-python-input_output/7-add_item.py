#!/usr/bin/python3
import sys
from os import path

from . import save_to_json_file, load_from_json_file


def main():
  """Adds all command-line arguments to a list and saves them as JSON."""
  filename = "add_item.json"
  # Load existing items from the JSON file (or an empty list if it doesn't exist)
  item_list = load_from_json_file(filename) or []
  # Add all command-line arguments (excluding the script name) to the list
  item_list.extend(sys.argv[1:])
  # Save the updated list to the JSON file
  save_to_json_file(item_list, filename)


if __name__ == "__main__":
  main()