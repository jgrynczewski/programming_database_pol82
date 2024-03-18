# sql injection
# Tabela user
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(100) NOT NULL,
#     password VARCHAR(50)

# użytkownicy:
#     'johndoe','tajne'
#     'janedoe','test'
#     'admin','admin'
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'shop'

CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL
)
"""
INSERT_USER_1 = """
INSERT INTO user (username, password) VALUE 
('johndoe','tajne');
"""
INSERT_USER_2 = """
INSERT INTO user (username, password) VALUE 
('janedoe','test');
"""
INSERT_USER_3 = """
INSERT INTO user (username, password) VALUE 
('admin','admin');
"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(CREATE_USER_TABLE)
            cursor.execute(INSERT_USER_1)
            cursor.execute(INSERT_USER_2)
            cursor.execute(INSERT_USER_3)

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
