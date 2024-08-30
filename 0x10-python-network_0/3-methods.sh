#!/bin/bash
# This script retrieves allowed HTTP methods for a URL using curl.
[[ $(curl -s "http://0.0.0.0:5000/catch_me") =~ "You got me!" ]] && exit 0 || exit 1
