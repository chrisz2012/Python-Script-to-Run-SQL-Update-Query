# Python-Script-to-Run-SQL-Update-Query
If you have a single update query you can pass it into the script to run it on your environment

The script uses the psycopg2 library to connect to a Postgres Database.
The script also calls the system arguments with the sys module. 

The prerequisite for this script to work is to download and install the psycopg2 module with pip or install its binary installation.

https://pypi.org/project/psycopg2/

pip install psycopg2

The script functions as so. Set your variables:

conn = psycopg2.connect(
    host="database_hostname",
    database="database",
    user="user",
    password="password",
    port=5432)

Then you can pass the update queries into the script and it will run them on your environment saving you time running it from your local commandline.

Example:

python3 ./Python-Script-to-Run-SQL-Update-Query.py "update users set first_name = 'John' where id = 1249;"
UPDATE 1

