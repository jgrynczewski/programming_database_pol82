# 4. W bazie danych 'shop stwórz tabele:
#
# A. 'client' z następującymi kolumnami:
# id INT AUTO_INCREMENT PRIMARY KEY,
# first_name VARCHAR(100) NOT NULL,
# last_name VARCHAR(100) NOT NULL,
# email VARCHAR(100) UNIQUE
#
# B. "product" z następującymi kolumnami:
# id INT AUTO_INCREMENT PRIMARY KEY,
# name VARCHAR(100) NOT NULL,
# price DECIMAL(10, 2) NOT NULL,
# stock_quantity INT NOT NULL
#
# C. 'order_detail' z następującymi kolumnami:
# id INT AUTO_INCREMENT PRIMARY KEY,
# client_id INT NOT NULL,
# product_id INT NOT NULL,
# quantity INT NOT NULL,
# order_date DATE NOT NULL
# 'client_id' i 'product_id' to klucze obce odpowiednio do tabel 'client' i 'product'

import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'shop'

CREATE_CLIENT_TABLE = """
CREATE TABLE IF NOT EXISTS client(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100)
)
"""


try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(CREATE_CLIENT_TABLE)
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

