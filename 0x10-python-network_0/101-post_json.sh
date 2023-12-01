#!/bin/bash
#json
curl -i -s "$1" -d "$2" -X POST -H "Content-Type: application/json" -H "Accept: application/json"
