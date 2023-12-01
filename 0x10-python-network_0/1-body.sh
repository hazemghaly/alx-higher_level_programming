#!/bin/bash
#body display
curl -Lsi -o /dev/null -w "%{url_effective}" "$1"
