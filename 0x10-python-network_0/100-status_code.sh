#!/bin/bash
# Script that sends a req to the URL passed as an argument, and only the status code of the response will be displayed
curl -so /dev/null -w "%{http_code}" "$1"
