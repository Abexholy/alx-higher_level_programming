#!/bin/bash
# Sends a GET request to the URL,then displays the body of the response
curl -s -H "X-School-User-Id: 98" -L "$1"
