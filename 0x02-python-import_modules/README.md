# Python Imports and Modules

## Overview

Project work centered on modular Python programs, command-line arguments, reusable imports, and simple package-style organization.

## Learning Objectives

- Import functions and variables from other modules.
- Use `sys.argv` for command-line processing.
- Organize Python code into reusable modules.
- Build small executable scripts that reuse existing logic.

## Key Deliverables

- `0-add.py`
- `1-calculation.py`
- `100-my_calculator.py`
- `101-easy_print.py`
- `102-magic_calculation.py`
- `103-fast_alphabet.py`
- `2-args.py`
- `3-infinite_add.py`
- `4-hidden_discovery.py`
- `5-variable_load.py`
- `add_0.py`
- `calculator_1.py`
- `variable_load_5.py`

## Requirements

- Python 3
- pycodestyle

## Usage

Run scripts with `python3 <filename>.py`. Some programs depend on sibling modules in this folder, so execute them from within the project directory.

## Detailed File Guide

- `add_0.py` — Module exposing `add(a, b)` utility.
- `0-add.py` — Imports `add` and prints result of `1 + 2`.
- `1-calculation.py` — Imports arithmetic functions and prints formatted operations.
- `calculator_1.py` — Module containing `add`, `sub`, `mul`, and `div`.
- `2-args.py` — Prints count and values of command-line arguments.
- `3-infinite_add.py` — Sums all numeric command-line arguments.
- `4-hidden_discovery.py` — Lists names defined in hidden module, excluding private ones.
- `5-variable_load.py` — Imports and prints value of variable `a`.
- `variable_load_5.py` — Module that defines `a = 98` for import task.
- `100-my_calculator.py` — CLI calculator using operators and imported functions.
- `101-easy_print.py` — Prints required string without using `print` directly.
- `102-magic_calculation.py` — Source rewrite of provided bytecode logic.
- `103-fast_alphabet.py` — Prints uppercase alphabet quickly via module constant.
