#!/bin/bash
#status of code
curl -s -o /dev/null -w "%{http_code}" "$1"
