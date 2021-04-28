#!/bin/bash
#exec 3>&1 4>&2
#trap 'exec 2>&4 1>&3' 0 1 2 3
#exec 1>log.out 2>&1
# Everything below will go to the file 'log.out' if lines 2-4 are uncommented:
echo "Installing Dependencies"
python -m pip install --upgrade pip || { echo "pip install failed"; exit 1; }
python -m pip install --upgrade pylint || { echo "Pylint install failed"; exit 1; }
if [ -f requirements.txt ]; then pip install -r requirements.txt || { echo "Virtual environment requirements install failed"; exit 1; } fi
python -m pip install --upgrade Django || { echo "Django install failed"; exit 1; }
python -m pip install --upgrade mysqlclient || { echo "Mysql client install failed"; exit 1; }
python -m pip install --upgrade djangorestframework || { echo "REST framework install failed"; exit 1; }
python -m pip install --upgrade django-cors-headers || { echo "CORS app install failed"; exit 1; }
python -m pip install --upgrade rpy2 || { echo "RPY2 framework install failed"; exit 1; }
python -m pip install --upgrade numpy || { echo "numpy framework install failed"; exit 1; }
python -m pip install --upgrade reportlab || { echo "ReportLab install failed"; exit 1; }
python -m pip install --upgrade google-auth || { echo "Google Authentication install failed"; exit 1; }
python -m pip install --upgrade google-auth-oauthlib || { echo "Google Authentication OAuth Library install failed"; exit 1; }

echo "Running PyLint"
pylint -d R,C,wildcard-import,undefined-variable,W0105,W0703,E1101,E0401,unused-variable,unused-import,unused-import,unused-wildcard-import,unused-argument src || { echo "pylint failed"; exit 1; }

echo "Running Django Migrations"
python src/manage.py migrate || { echo "migrate failed"; exit 1; }

echo "Build success. Run the command 'python src/manage.py runserver localhost:8000' to run the webserver locally in a browser."

exit 0