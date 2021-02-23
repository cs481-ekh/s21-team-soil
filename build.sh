#!/bin/bash

echo "Installing Dependencies"
python -m pip install --upgrade pip || { echo "pip install failed"; exit 1; }
python -m pip install --upgrade pylint || { echo "Pylint install failed"; exit 1; }
if [ -f requirements.txt ]; then pip install -r requirements.txt || { echo "Virtual environment requirements install failed"; exit 1; } fi
python -m pip install --upgrade Django || { echo "Django install failed"; exit 1; }

# PyLint will automatically output an exit code to stderr, so sending exit codes here isn't necessary.
echo "Running PyLint"
pylint -d C src || { echo "pylint failed"; exit 1; }

echo "Running Django Migrations"
python src/manage.py migrate || { echo "migrate failed"; exit 1; }

echo "Build success. Run the command 'python src/manage.py runserver' to run the webserver locally in a browser."

exit 0