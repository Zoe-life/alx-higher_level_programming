#!/bin/bash
# This script sends a DELETE request to a URL and displays the response body using curl.
body=$(curl -s -X DELETE "$1"); echo "$body"
