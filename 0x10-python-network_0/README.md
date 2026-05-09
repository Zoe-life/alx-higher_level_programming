# Python Network 0

## Overview

Networking exercises that introduce HTTP concepts, cURL-based request scripting, request inspection, and a small Python algorithm task.

## Learning Objectives

- Send HTTP requests with `curl`.
- Inspect response headers, bodies, and status codes.
- Submit data with request parameters and JSON payloads.
- Mix shell-based networking tasks with a standalone Python problem.

## Key Deliverables

- `0-body_size.sh`
- `1-body.sh`
- `100-status_code.sh`
- `101-post_json.sh`
- `102-catch_me.sh`
- `2-delete.sh`
- `3-methods.sh`
- `4-header.sh`
- `5-post_params.sh`
- `6-peak.py`
- `6-peak.txt`

## Requirements

- bash
- curl
- Python 3 for the peak-finding exercise

## Usage

Run shell scripts with `bash <filename>.sh`. Use `python3 6-peak.py` to exercise the included Python function if needed.

## Detailed File Guide

- `0-body_size.sh` — Sends GET request and prints response body size only.
- `1-body.sh` — Fetches and prints body for successful (`200`) responses.
- `2-delete.sh` — Sends DELETE request to target URL.
- `3-methods.sh` — Displays allowed HTTP methods from server headers.
- `4-header.sh` — Sends GET request with custom `X-School-User-Id` header.
- `5-post_params.sh` — Sends POST request with specific form parameters.
- `6-peak.py` — Finds a peak integer in an unsorted list.
- `6-peak.txt` — Complexity explanation for peak-finding algorithm.
- `100-status_code.sh` — Sends request and prints returned HTTP status code.
- `101-post_json.sh` — Sends JSON file content as POST body.
- `102-catch_me.sh` — Crafts request that triggers expected hidden server response.
