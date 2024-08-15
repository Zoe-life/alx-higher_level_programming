#!/bin/bash
# This script retrieves allowed HTTP methods for a URL using curl.

allowed_methods=$(curl -s -o /dev/null -i -X OPTIONS "$1" | grep -Eo 'Allow: (.*)')

if [[ ! -z "$allowed_methods" ]]; then
  echo "${allowed_methods:7}"  # Remove leading "Allow: "
fi