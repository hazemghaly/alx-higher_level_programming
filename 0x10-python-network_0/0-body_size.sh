#!/bin/bash
#script to get size
curl -Is $URL | grep -w Content-Length | awk '{print $2}'
