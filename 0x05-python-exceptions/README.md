# Python Exceptions

## Overview

Practice handling runtime errors gracefully through exception-aware utilities, custom failure behavior, and defensive programming patterns.

## Learning Objectives

- Catch and handle exceptions without crashing programs unnecessarily.
- Separate normal execution flow from error-handling logic.
- Raise exceptions intentionally when invalid states occur.
- Write safer utility functions that validate input and output.

## Key Deliverables

- `0-safe_print_list.py`
- `1-safe_print_integer.py`
- `100-safe_print_integer_err.py`
- `101-safe_function.py`
- `102-magic_calculation.py`
- `103-python.c`
- `103-tests.py`
- `2-safe_print_list_integers.py`
- `3-safe_print_division.py`
- `4-list_division.py`
- `5-raise_exception.py`
- `6-raise_exception_msg.py`

## Requirements

- Python 3
- pycodestyle
- gcc for the CPython helper source if needed

## Usage

Execute the scripts with `python3 <filename>.py`. The provided driver files demonstrate expected input and output scenarios.

## Detailed File Guide

- `0-safe_print_list.py` — Prints up to `x` list elements safely.
- `1-safe_print_integer.py` — Prints an integer if value is valid integer format.
- `2-safe_print_list_integers.py` — Prints first `x` integer-only elements from list.
- `3-safe_print_division.py` — Divides two numbers with guaranteed cleanup message.
- `4-list_division.py` — Divides paired list items with per-item exception handling.
- `5-raise_exception.py` — Intentionally raises a `TypeError`.
- `6-raise_exception_msg.py` — Raises a `NameError` with custom message.
- `100-safe_print_integer_err.py` — Prints integer or writes error to stderr.
- `101-safe_function.py` — Runs a function safely and returns `None` on exception.
- `102-magic_calculation.py` — Recreates provided bytecode exception logic.
- `103-python.c` — C helpers for inspecting Python objects.
- `103-tests.py` — Tests for C helper inspection functions.
