#!/bin/bash
#post
curl -X -d '{"email":"test@gmail.com","subject":"I will always be here for PLD"}' POST -s "$1"
