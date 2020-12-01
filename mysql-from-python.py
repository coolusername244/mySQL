import os
import pymysql

if os.path.exists("env.py"):
    import env

username = os.environ.get("usernme")
password = os.environ.get("password")

connection = pymysql.connect(
    host="localhost", user=username, password=password, db="Chinook"
)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()