#!/bin/bash

# Remove python bytecode files and cache
if [ -d "soil/soil/__pycache__" ]; then rm -Rf soil/soil/__pycache__; fi
find . -name "*.pyc" -delete

exit 0
