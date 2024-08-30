#!/bin/bash
# This script sends a request to a URL and checks for a specific message in the response using curl.
url="http://0.0.0.0:5000/catch_me"; [[ $(curl -s "$url") =~ "You got me!" ]] && exit 0 || exit 1
