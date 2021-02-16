#!/bin/bash

#TODO: Run build/lint setup

echo "Installing Dependencies"
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
python -m pip install Django

echo "Running Django Migrations"
python soil/manage.py migrate

echo "Starting up the application"
python soil/manage.py runserver

exit 0