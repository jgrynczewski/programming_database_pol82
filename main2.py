# using context managers
from mysql.connector import connect

USER = 'root'
PASSWORD = 'admin'

CREATE_DATABASE_QUERY = """CREATE DATABASE shop2;"""

with connect(user=USER, password=PASSWORD) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute(CREATE_DATABASE_QUERY)
