#!/bin/bash

echo "Installing Dependencies"
python -m pip install --upgrade pip
python -m pip install --upgrade pylint
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
python -m pip install --upgrade Django
python -m pip install --upgrade mysqlclient

# PyLint will automatically output an exit code to stderr, so sending exit codes here isn't necessary.
echo "Running PyLint"
pylint src

echo "Running Django Migrations"
python src/manage.py migrate || { echo "migrate failed"; exit 1; }

echo "Build success. Run the command 'python src/manage.py runserver localhost:8000' to run the webserver locally in a browser."

exit 0