#!/bin/bash
# This script retrieves the body of a URL for a 200 status code GET request using curl.

status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [[ $status_code -eq 200 ]]; then
  body=$(curl -s "$1")
  echo "$body"
fi