#!/bin/bash

echo "Installing Dependencies"
python -m pip install --upgrade pip
python -m pip install --upgrade pylint
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
python -m pip install --upgrade Django

echo "Running PyLint"
pylint src
if [[ $? -eq 1 ]]; then exit 1;

echo "Running Django Migrations"
python src/manage.py migrate || { echo "migrate failed"; exit 1; }

echo "Build success. Run the command 'python src/manage.py runserver' to run the webserver locally in a browser."

exit 0