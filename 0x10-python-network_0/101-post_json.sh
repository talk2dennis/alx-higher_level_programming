#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sH "Content-Type: application/json" -d cat $2 POST $1
