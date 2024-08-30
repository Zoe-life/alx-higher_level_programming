#!/bin/bash
# Get response body for successful (200) GET requests
response=$(curl -sL "$1"); [[ "${response: -3}" == 200 ]] && echo "${response:0:-3}"
