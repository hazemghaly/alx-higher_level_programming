#!/bin/bash
#body display
curl -s -w "%{http_code}\n" $1
