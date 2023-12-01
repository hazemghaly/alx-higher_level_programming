#!/bin/bash
#body display
curl -s -o /dev/null -r 0-200 -w "%{http_code}\n" $1 
