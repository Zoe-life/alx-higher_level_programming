#!/bin/bash
# Get URL body size (bytes) silently & echo
curl -s "$1" -o /dev/null --write-out "%{size_download}"
