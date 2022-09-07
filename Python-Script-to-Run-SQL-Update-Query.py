import psycopg2
import sys

firstarg=sys.argv[1]

print("Running Query ID:")

conn = psycopg2.connect(
    host="database_hostname",
    database="database",
    user="user",
    password="password:q",
    port=5432)

conn.autocommit = True
cur = conn.cursor()

sql = "{}".format(firstarg)

print(sql)

cur.execute(sql)

updated_rows = cur.rowcount
print("UPDATE {}".format(updated_rows))

conn.commit()
conn.close()
