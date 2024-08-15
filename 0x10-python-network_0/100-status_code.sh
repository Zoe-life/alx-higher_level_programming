#!/bin/bash
# This script retrieves the status code of a URL request using curl.

status_code=$(curl -s -w "%{http_code}" "$1")

if [[ $status_code ]]; then
  echo "$status_code"
fi