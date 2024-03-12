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

INSERT_CLIENT_1 = """
INSERT INTO client (first_name, last_name, email) VALUE 
('John','Doe','john.doe@example.com');
"""

INSERT_CLIENT_2 = """
INSERT INTO client (first_name, last_name, email) VALUE 
('Alice','Smith','alice.smith@example.com');
"""

INSERT_CLIENT_3 = """
INSERT INTO client (first_name, last_name, email) VALUE 
('Michael','Johnson','michael.johnson@example.com');
"""

INSERT_CLIENT_4 = """
INSERT INTO client (first_name, last_name, email) VALUE 
('Emily','Brown','emily.brown@example.com');
"""

INSERT_CLIENT_5 = """
INSERT INTO client (first_name, last_name, email) VALUE 
('David','Jones','david.jones@example.com');
"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(INSERT_CLIENT_1)
            cursor.execute(INSERT_CLIENT_2)
            cursor.execute(INSERT_CLIENT_3)
            cursor.execute(INSERT_CLIENT_4)
            cursor.execute(INSERT_CLIENT_5)

            # obowiązkowo dla DML
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
