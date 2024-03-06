from mysql.connector import connect
from mysql.connector import MySQLConnection

USER = 'root'
PASSWORD = 'admin'


with connect(user=USER, password=PASSWORD) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("""CREATE DATABASE shop2;""")
