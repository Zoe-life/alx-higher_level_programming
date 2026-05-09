# Python Inheritance

## Overview

Exercises covering inheritance, custom subclasses, type inspection, attribute extension, and geometry-based class hierarchies.

## Learning Objectives

- Create subclasses that reuse and extend parent behavior.
- Inspect class relationships using built-in type helpers.
- Define abstract-style base classes and derived implementations.
- Apply inheritance to geometric modeling exercises.

## Key Deliverables

- `0-lookup.py`
- `1-my_list.py`
- `10-square.py`
- `100-my_int.py`
- `101-add_attribute.py`
- `11-square.py`
- `2-is_same_class.py`
- `3-is_kind_of_class.py`
- `4-inherits_from.py`
- `5-base_geometry.py`
- `6-base_geometry.py`
- `7-base_geometry.py`
- `8-rectangle.py`
- `9-rectangle.py`
- `tests`

## Requirements

- Python 3
- pycodestyle

## Usage

Run scripts with `python3 <filename>.py`. The `tests` directory can be used as a reference for additional validation support in this project.

## Detailed File Guide

- `0-lookup.py` — Returns available attributes/methods of an object.
- `1-my_list.py` — Subclass of list with custom sorted-print behavior.
- `2-is_same_class.py` — Checks whether object is exactly a specified class.
- `3-is_kind_of_class.py` — Checks object instance against class or subclass.
- `4-inherits_from.py` — Checks whether object inherited from a class.
- `5-base_geometry.py` — Defines base geometry class shell.
- `6-base_geometry.py` — Adds area method that raises exception placeholder.
- `7-base_geometry.py` — Adds integer validator utility in base class.
- `8-rectangle.py` — Rectangle class inheriting from `BaseGeometry`.
- `9-rectangle.py` — Adds string representation to rectangle class.
- `10-square.py` — Square class built on rectangle inheritance chain.
- `11-square.py` — Adds string representation for square.
- `100-my_int.py` — Rebel integer class with inverted equality behavior.
- `101-add_attribute.py` — Dynamically adds attribute to object when allowed.
- `tests/` — Validation files and task-specific test resources.
