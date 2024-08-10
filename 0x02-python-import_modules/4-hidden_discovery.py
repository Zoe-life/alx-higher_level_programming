#!/usr/bin/python3
"""
This program discovers and prints public names from hidden_4.pyc.
"""

import dis
import hidden_4  # Import the compiled module

# Extract bytecode from the compiled module
bytecode = hidden_4.__code__.co_code

# Define an empty list to store public names
public_names = []

# Iterate through bytecode instructions
for op in dis.Instruction(bytecode, 0).get_instructions():
    # Check for LOAD_NAME instruction
    if op.opcode == dis.opmap['LOAD_NAME']:
        # Extract the name
        name = op.argval

        # Check if the name starts with __ (dunder)
        if not name.startswith('__'):
            # Add the public name to the list
            public_names.append(name)

# Sort the list alphabetically (optional for the prompt)
public_names.sort()

# Print each public name on a separate line
for name in public_names:
    print(name)