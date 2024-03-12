# Zadanie 2: Tworzenie tabeli (ddl)

# Stwórz tabelę "employee" w bazie danych "company_db" z następującymi kolumnami:
#
# id (typ: Integer, klucz główny)
# first_name (typ: String o maksymalnej długości 50)
# last_name (typ: String o maksymalnej długości 100)
# position (typ: String o maksymalnej długości 100)
# salary (typ: Float)

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, Float, String

metadata = MetaData()
Table(
    'employee',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(100)),
    Column('position', String(100)),
    Column('salary', Float)
)

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str)

# CREATE TABLE (C z CRUD dla DDL)
metadata.create_all(engine)

# DROP TABLE (D z CRUD dla DDL)
# metadata.create_all(engine)
print("Done.")

# ALTER TABLE (U z CRUD dla DDL)
