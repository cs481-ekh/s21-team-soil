#!/bin/bash

echo "Installing Dependencies"
python -m pip install --upgrade pip || { echo "pip install failed"; exit 1; }
python -m pip install --upgrade pylint || { echo "Pylint install failed"; exit 1; }
if [ -f requirements.txt ]; then pip install -r requirements.txt || { echo "Virtual environment requirements install failed"; exit 1; } fi
python -m pip install --upgrade Django || { echo "Django install failed"; exit 1; }
python -m pip install --upgrade mysqlclient || { echo "Mysql client install failed"; exit 1; }
python -m pip install --upgrade djangorestframework || { echo "REST framework install failed"; exit 1; }
python -m pip install --upgrade django-cors-headers || { echo "CORS app install failed"; exit 1; }
python -m pip install --upgrade rpy2 || { echo "RPY2 framework imstall failed"; exit 1; }

echo "Running PyLint"
pylint -d C0415 src || { echo "pylint failed"; exit 1; }

echo "Running Django Migrations"
python src/manage.py migrate || { echo "migrate failed"; exit 1; }

echo "Build success. Run the command 'python src/manage.py runserver localhost:8000' to run the webserver locally in a browser."

exit 0