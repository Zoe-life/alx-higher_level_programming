#!/bin/bash
# This script sends a request to a URL and checks for a specific message in the response using curl.

url="http://0.0.0.0:5000/catch_me"

# Send request and capture response body
body=$(curl -s "$url")

# Check if response body contains the target message
if grep -q "You got me!" <<< "$body"; then
  exit 0  # Exit with success code (0) if message is found
fi

exit 1  # Exit with failure code (1) if message is not found