# Zapis do csv (można też użyć biblioteki csv)

import datetime
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'shop'

stmt = """SELECT * FROM client;"""

with open('test.csv', 'w+') as file_:
    try:
        with connect(user=USER, password=PASSWORD, database=DB) as cnx:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute(stmt)

                for row in cursor:
                    file_.write(f"{row.get('id')},{row.get('first_name')},{row.get('last_name')},{row.get('email')}\n")

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
