#!/bin/bash
#body display
curl -Ls -o /dev/null -w "%{url_effective}" "$1"
