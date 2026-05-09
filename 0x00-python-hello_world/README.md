# Python Hello World

## Overview

Introductory Python exercises covering execution, output, string manipulation, and a small C utility for linked list cycle detection.

## Learning Objectives

- Set up and run Python scripts from the command line.
- Work with standard output, strings, and formatted text.
- Understand basic Python file execution and compilation flow.
- Bridge simple Python tasks with a supporting C exercise.

## Key Deliverables

- `0-run`
- `1-run_inline`
- `10-check_cycle.c`
- `100-write.py`
- `101-compile`
- `102-magic_calculation.py`
- `2-print.py`
- `3-print_number.py`
- `4-print_float.py`
- `5-print_string.py`
- `6-concat.py`
- `7-edges.py`
- `8-concat_edges.py`
- `9-easter_egg.py`
- `lists.h`

## Requirements

- Python 3
- gcc for the C source files
- pycodestyle for style checking when required by the coursework

## Usage

Run individual Python scripts with `python3 <filename>.py`. Compile C files such as `10-check_cycle.c` together with the provided header when testing the linked list utility.

## Detailed File Guide

- `0-run` — Shell script that runs a Python script file.
- `1-run_inline` — Shell script that executes inline Python code with `-c`.
- `2-print.py` — Prints the exact string "Programming is like building a multilingual puzzle".
- `3-print_number.py` — Stores an integer and prints it inside a sentence.
- `4-print_float.py` — Prints a float with 2 decimal places using formatting.
- `5-print_string.py` — Prints a string three times and then its first 9 characters.
- `6-concat.py` — Concatenates first name and last name into a greeting.
- `7-edges.py` — Slices and prints first, middle, and last parts of a word.
- `8-concat_edges.py` — Builds and prints a sentence from selected string slices.
- `9-easter_egg.py` — Prints "The Zen of Python" with `import this`.
- `10-check_cycle.c` — C function that detects a cycle in a singly linked list.
- `100-write.py` — Prints text to stderr using low-level output style.
- `101-compile` — Shell script that compiles a Python file into bytecode (`.pyc`).
- `102-magic_calculation.py` — Reproduces given Python bytecode logic in source form.
- `lists.h` — Header with linked-list structure and function prototype for C task.
