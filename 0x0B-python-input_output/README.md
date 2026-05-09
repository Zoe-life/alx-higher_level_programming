# Python Input and Output

## Overview

A collection of exercises centered on file handling, serialization, deserialization, class-to-dictionary conversion, and generator-based processing.

## Learning Objectives

- Read and write text files safely.
- Serialize Python data structures to and from JSON.
- Convert objects into serializable representations.
- Use generators and file parsing for incremental processing.

## Key Deliverables

- `0-read_file.py`
- `1-write_file.py`
- `10-student.py`
- `100-append_after.py`
- `101-generator.py`
- `101-stats.py`
- `11-student.py`
- `2-append_write.py`
- `3-to_json_string.py`
- `4-from_json_string.py`
- `5-save_to_json_file.py`
- `6-load_from_json_file.py`
- `7-add_item.py`
- `8-class_to_json.py`
- `8-main_2.py`
- `8-my_class.py`
- `8-my_class_2.py`
- `9-student.py`

## Requirements

- Python 3
- pycodestyle

## Usage

Execute scripts with `python3 <filename>.py`. Some tasks produce or consume local files, so run them from within this project directory.

## Detailed File Guide

- `0-read_file.py` — Reads and prints full text file content.
- `1-write_file.py` — Writes text to file and returns chars written.
- `2-append_write.py` — Appends text to file and returns chars added.
- `3-to_json_string.py` — Converts Python object to JSON string.
- `4-from_json_string.py` — Converts JSON string back to Python object.
- `5-save_to_json_file.py` — Saves Python object to JSON file.
- `6-load_from_json_file.py` — Loads Python object from JSON file.
- `7-add_item.py` — CLI script that persists argument list to JSON file.
- `8-class_to_json.py` — Returns dictionary representation of object attributes.
- `8-my_class.py`, `8-my_class_2.py`, `8-main_2.py` — Sample support files for class-to-JSON task behavior checks.
- `9-student.py` — Student class serializable through dictionary conversion.
- `10-student.py` — Student serialization with optional filtered fields.
- `11-student.py` — Student class supporting reload from JSON-style dict.
- `100-append_after.py` — Inserts text after matching lines in a file.
- `101-generator.py` — Generator that yields parsed rows from a large file.
- `101-stats.py` — Streams stdin log lines and prints status/byte metrics.
