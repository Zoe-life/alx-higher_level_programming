#!/bin/bash
# This script sends a POST request with JSON data from a file and displays the response body using curl.

url="$1"
json_file="$2"

# Check if both arguments are provided
if [[ -z "$url" || -z "$json_file" ]]; then
  echo "Error: Please provide both URL and JSON file name."
  exit 1
fi

# Check if JSON file exists
if [[ ! -f "$json_file" ]]; then
  echo "Error: JSON file '$json_file' does not exist."
  exit 1
fi

# Read JSON data from the file
json_data=$(cat "$json_file")

# Validate JSON syntax (optional)
if [[ ! $(jq -e '. >/dev/null' <<< "$json_data") ]]; then
  echo "Not a valid JSON"
  exit 1
fi

# Send POST request with JSON data
body=$(curl -s -X POST -H "Content-Type: application/json" -d "$json_data" "$url")
echo "$body"