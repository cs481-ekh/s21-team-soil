#!/bin/bash

# Remove python bytecode files and cache
if [ -d "src/soil/__pycache__" ]; then rm -Rf src/soil/__pycache__; fi
find . -name "*.pyc" -delete

exit 0
