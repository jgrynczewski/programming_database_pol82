# DQL - JOIN
# 9. Wyświetl klientów razem z produkatmi które kupili.

import datetime
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'shop'

stmt = """
SELECT c.first_name, c.last_name, p.name, od.quantity FROM order_detail as od JOIN 
client as c ON od.client_id=c.id JOIN
product as p ON od.product_id=p.id
;"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(stmt)

            for row in cursor:
                print(row)


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
