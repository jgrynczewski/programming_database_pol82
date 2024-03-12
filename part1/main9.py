# metoda executemany
# 6. Dodaj kilka rekordów do tabeli "order_detail".
# 1,1,3,'2024-03-04'
# 2,3,2,'2024-03-05'
# 3,2,1,'2024-03-06'
# 1,4,2,'2024-03-07'
# 2,5,1,'2024-03-08'

import datetime
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'shop'

INSERT_ORDERS = """
INSERT INTO order_detail(client_id, product_id, quantity, order_date) VALUE
(%s, %s, %s, %s);
"""

ORDERS = [
    (4, 1, 3, datetime.date(2024, 3, 4)),
    (2, 6, 2, datetime.date(2024, 3, 5)),
    (3, 2, 1, datetime.date(2024, 3, 6)),
    (4, 7, 2, datetime.date(2024, 3, 7)),
    (2, 5, 1, datetime.date(2024, 3, 8))
]

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.executemany(INSERT_ORDERS, ORDERS)
            cnx.commit()

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
