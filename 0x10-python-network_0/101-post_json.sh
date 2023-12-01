#!/bin/bash
#json
curl -i -s "$1" -X POST -H "Content-Type: application/json" -o "$2" -H "Accept: application/json"
