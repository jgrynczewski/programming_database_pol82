# 1. Stwórz nową bazę danych o nazwie 'shop'.
from mysql.connector import connect

USER = 'root'
PASSWORD = 'admin'

cnx = connect(user=USER, password=PASSWORD)
cursor = cnx.cursor()

cursor.execute("""CREATE DATABASE shop;""")

cursor.close()
cnx.close()
