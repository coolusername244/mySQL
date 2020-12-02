import os
import datetime
import pymysql

if os.path.exists("env.py"):
    import env

username = os.environ.get("usernme")
password = os.environ.get("password")

connection = pymysql.connect(
    host="localhost",
    user=username,
    password=password,
    db="Chinook"
)

try:
    with connection.cursor() as cursor:
        list_of_names = ["lee", "Maria", "Paris", "Blaine"]
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE Name in ({});".format(format_strings), list_of_names)
        connection.commit()

finally:
    connection.close()
