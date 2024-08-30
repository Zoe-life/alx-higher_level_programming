#!/bin/bash
# This script sends a POST request with form data and displays the response body using curl.
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1" && (echo "POST params:"; echo "    email: test@gmail.com"; echo "    subject: I will always be here for PLD"; echo ""; echo "$body")
