import psycopg2
import sys

# firstarg lets you pass your sql query wrapped in double quotes so it works like this
# python3 ./python-script-to-run-sql-update-query.py "update users set id = 123 where id = 120;" 
# the script then connects to your DB and executes the query on the remote host

firstarg=sys.argv[1]

# In the conn spaces fill out your database connection parameters
conn = psycopg2.connect(
    host="database_hostname",
    database="database",
    user="user",
    password="password",
    port=5432)

# put the print statement of your database where X is name of your DB
print("Running Query on {}:".format(database))

conn.autocommit = True
cur = conn.cursor()

sql = "{}".format(firstarg)

print(sql)

cur.execute(sql)

# below prints the row count of the amount of rows that were updated, inserted, or deleted in the database
updated_rows = cur.rowcount
if firstarg[0:6].lower() == "update":
	print("UPDATE {}".format(updated_rows))
elif firstarg[0:6] == "insert":
	print("INSERT {}".format(updated_rows))
elif firstarg[0:6] == "delete":
    print("DELETE {}".format(updated_rows))

# connection then gets closed by the database
conn.commit()
conn.close()
