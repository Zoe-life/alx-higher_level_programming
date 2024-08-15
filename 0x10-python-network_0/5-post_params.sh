#!/bin/bash
# This script sends a POST request with form data and displays the response body using curl.

email="test@gmail.com"
subject="I will always be here for PLD"

body=$(curl -s -X POST -d "email=$email&subject=$subject" "$1")
echo "POST params:"
echo "    email: $email"
echo "    subject: $subject"
echo ""
echo "$body"