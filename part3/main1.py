# Zadanie 1: Tworzenie silnika oraz utworzenie bazy (ddl)
#
# Stwórz silnik SQLAlchemy do łączenia się z bazą danych MySQL.
# Połącz się z serwerem MySQL i stwórz bazę danych "company_db2"

from sqlalchemy import create_engine
from sqlalchemy import text


# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost"

engine = create_engine(conn_str)

stmt = text("""CREATE DATABASE IF NOT EXISTS company_db2;""")
with engine.connect() as conn:
    conn.execute(stmt)

print("Done.")
