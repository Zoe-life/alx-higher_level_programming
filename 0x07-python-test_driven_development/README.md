# Python Test-Driven Development

## Overview

A test-driven project that combines documentation, input validation, matrix operations, formatted text output, and unit testing.

## Learning Objectives

- Write Python functions with explicit contracts and docstrings.
- Validate arguments before processing data.
- Use tests to confirm correctness and guard against regressions.
- Practice mathematical and formatting utilities using TDD principles.

## Key Deliverables

- `0-add_integer.py`
- `100-matrix_mul.py`
- `101-lazy_matrix_mul.py`
- `102-python.c`
- `2-matrix_divided.py`
- `3-say_my_name.py`
- `4-print_square.py`
- `5-text_indentation.py`
- `6-max_integer.py`
- `tests`

## Requirements

- Python 3
- pycodestyle
- unittest
- NumPy for the lazy matrix multiplication task if installed in the target environment

## Usage

Run the Python scripts with `python3 <filename>.py`. Execute the provided tests with `python3 -m unittest` from within the project directory when validating the unit test exercise.

## Detailed File Guide

- `0-add_integer.py` — Adds two integers/floats with strict validation.
- `2-matrix_divided.py` — Divides matrix values by a number with full checks.
- `3-say_my_name.py` — Prints "My name is" with validated first/last names.
- `4-print_square.py` — Prints a square of `#` of validated size.
- `5-text_indentation.py` — Formats text with line breaks after punctuation marks.
- `6-max_integer.py` — Returns max integer in a list.
- `100-matrix_mul.py` — Multiplies two matrices using pure Python rules.
- `101-lazy_matrix_mul.py` — Multiplies matrices using NumPy backend.
- `102-python.c` — C helper to print basic Python object info.
- `tests/` — Doctest and unit-test assets that validate expected behavior.
