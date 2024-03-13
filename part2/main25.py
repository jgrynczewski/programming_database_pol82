# Zadanie 10: Tworzenie tabeli (ddl) - powiązania

# Stwórz drugą tabelę o nazwie "departments" z kolumnami:
# id (klucz główny),
# name (nazwa działu)
# manager_id (id menedżera, klucz obcy do tabeli employee, NOT NULL)
#
# Dodatkowo w tabeli employee stwórz klucz obcy do tabeli deparment. Wartość klucza będzie
# wskazywać w jakiej jednostce znajduje się pracownik.

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, Float, String, ForeignKey

metadata = MetaData()
Table(
    'employee',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(100)),
    Column('position', String(100)),
    Column('salary', Float),
    Column('department_id', Integer, ForeignKey("department.id")),
)

Table(
    'department',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('manager_id', Integer, ForeignKey('employee.id'), nullable=False)
)

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str)

# CREATE TABLE (C z CRUD dla DDL)
metadata.create_all(engine)

# DROP TABLE (D z CRUD dla DDL)
# metadata.drop_all(engine)  # to nie zadziała, bo sqlalchemy.exc.CircularDependencyError
# Usuwanie tabel powiązanych (tutaj mamy w obu tabelach klucze obce, więc trzeba zrobić myk)
# SET FOREIGN_KEY_CHECKS=0;
# DROP TABLE department;
# DROP TABLE employee;
# SET FOREIGN_KEY_CHECKS=1;

print("Done.")
