# sql injection
# 5. Dodaj kilka rekordów do tabeli "klienci" zawierających imiona, nazwiska i adresy e-mail klientów.
# 'John','Doe','john.doe@example.com'
# 'Alice','Smith','alice.smith@example.com'
# 'Michael','Johnson','michael.johnson@example.com'
# 'Emily','Brown','emily.brown@example.com'
# 'David','Jones','david.jones@example.com'


import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'shop'


product_name = input("Poodaj nazwę produktu: ")
product_price = int(input("Podaj cenę produktu: "))
stock_quantity = input("Podaj liczbę produktów na stanie: ")

# INSERT_PRODUCT = """
# INSERT INTO product (name, price, stock_quantity) VALUE
# (%s, %s, %s);
# """

# """'telefon', 100, 3); DELETE TABLE order_detail;--"""
"""telefon', 100, 3);DELETE TABLE order_detail;--"""
INSERT_PRODUCT = f"""
INSERT INTO product (name, price, stock_quantity) VALUE
('{product_name}', {product_price}, {stock_quantity});
"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            # cursor.execute(INSERT_PRODUCT, [product_name, product_price, stock_quantity])
            cursor.execute(INSERT_PRODUCT, multi=True)
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
