#!/bin/bash
#body display
curl -s -r 0-200 -w "%{http_code}\n" $1 
