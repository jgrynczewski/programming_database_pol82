# exceptions handling
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'

CREATE_DATABASE_QUERY = """CREATE DATABASE IF NOT EXISTS shop;"""

try:
    with connect(user=USER, password=PASSWORD) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(CREATE_DATABASE_QUERY)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists.")
    elif err.errno == errorcode.ER_PARSE_ERROR:
        print("SQL syntax error\n", err)
    else:
        print("An error occured\n", err)
else:
    print("Done.")
