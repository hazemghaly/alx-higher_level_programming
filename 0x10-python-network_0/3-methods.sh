#!/bin/bash
#show all options
curl -Li -X "OPTIONS" -s "$1" | grep "Allow:" | cut -f2- -d" "
