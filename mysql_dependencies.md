The following is needed for MySQL to work with Django.

# 1. Download MySQL and install MySQL if you do not already have it.
    - MySQL downloads can be found here(I went with the standard Windows install): https://dev.mysql.com/downloads/
    - Important: When you install MySQL note your port number. It will be 3306 by default. This is needed for a later step.

# 2. Download mysqlclient
    - mysqlclient requires a c++ compiler. If you're on Windows check you have Microsoft Visual C++ installed with the command 'gcc -v'
    - If you have a virtual python environment for this project activate it before you install
    pip install mysqlclient

# 3. Create a designated database and user for Django to use
    - Enter the MySQL command line client. Your command line prompt should appear as 'mysql>'
    - Run the following command to create a database for the project(include semicolon): CREATE DATABASE soil_dev;
    - You can check the database was created with the command: SHOW DATABASES;
    - Now create a designated user that Django will use when interacting with the MySQL server. 
Run the following two commands in order
    - CREATE USER 'django_priv'@'%' IDENTIFIED WITH mysql_native_password BY '2468';
    - GRANT ALL ON soil_dev.* TO 'django_priv'@'%';
    - FLUSH PRIVILEGES;

# Running the program
    - Run the following command to verify that ip and port show as 'localhost' and '3306, respectively. You may now exit the MySQL command line client.
    - SELECT SUBSTRING_INDEX(USER(), '@', -1) AS ip, @@port as port;
    - Build the project as you normally would then run: 'python soil/manage.py runserver localhost:8000'
    - You should see the default Django landing page upon success.

# Debugging
    - Contact Brandon Contreras at brandoncontreras@u.boisestate.edu or message me in Slack if you have any troubles getting MySQL to work with Django
