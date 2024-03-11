# DQL - operacje na danych oddelegowujemy do bazy

import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'shop'

stmt = """
SELECT ROUND(AVG(price), 2) as average_price FROM product;
"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(stmt)
            result = cursor.fetchone()

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
        print(result.get('average_price'))
