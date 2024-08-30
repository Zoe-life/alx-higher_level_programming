#!/bin/bash
# This script retrieves the status code of a URL request using curl.
response=$(curl -sI "$1"); echo "${response: -3}"
