#!/bin/bash
# This script retrieves the body size of a URL in bytes using curl.

size=$(curl -s "$1" -o /dev/null --write-out "%{size_download}")
echo "$size"