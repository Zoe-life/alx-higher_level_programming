#!/bin/bash
# This script sends a POST request with JSON data from a file and displays the response body using curl.
[[ -z "$1" || -z "$2" || ! -f "$2" ]] && echo "Error: Invalid arguments" && exit 1; json_data=$(cat "$2"); [[ ! $(jq -e '. >/dev/null' <<< "$json_data") ]] && echo "Not a valid JSON" && exit 1; echo $(curl -s -X POST -H "Content-Type: application/json" -d "$json_data" "$1")
