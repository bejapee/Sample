#!/bin/bash

# This shell script is used to test the core.py program
# Note that for some reason, on MacOS flask inserts newline
# characters; so expects needs them too

output=$(curl http://localhost:5000/api/)
expects='{
  "Hello": "World!"
}'

if [[ $output == $expects ]];
then
    echo "True"
else
    echo "False"
fi
