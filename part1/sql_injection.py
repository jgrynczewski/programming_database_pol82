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

username = input("Poodaj login: ")  # admin';--
password = input("Poodaj hasło: ")

stmt = f"""
    SELECT * FROM user
    WHERE username='{username}' AND password='{password}';
"""
print(stmt)
try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            result = cursor.execute(stmt)
            data = cursor.fetchone()
            if data:
                print(f"Witaj {data[1]}!")
            else:
                print("Podano nieprawidłowe dane.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists.")
    elif err.errno == errorcode.ER_PARSE_ERROR:
        print("SQL syntax error\n", err)
    else:
        print("An error occured\n", err)

