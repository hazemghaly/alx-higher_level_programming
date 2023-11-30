#!/bin/bash
#script to get size
curl -sI $URL | grep -i Content-Length | cut -d " " -f 2
