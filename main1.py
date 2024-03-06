from mysql.connector import connect
from mysql.connector import MySQLConnection

USER = 'root'
PASSWORD = 'admin'

cnx = connect(user=USER, password=PASSWORD)
cursor = cnx.cursor()

cursor.execute("""CREATE DATABASE shop2;""")

cursor.close()
cnx.close()
