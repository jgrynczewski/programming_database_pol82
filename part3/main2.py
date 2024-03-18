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
from sqlalchemy.orm import DeclarativeBase, mapped_column

# W ORM tabele są reprezentowane w kodzie przez modele (aka mapped class).
# Model to specjalna klasa (reprezentująca tabelkę),
# klasa która dziedziczy po klasie DeclarativeBase.
# Jak tworzymy modele w SQLAlchemy ?


class Base(DeclarativeBase):
    pass


# model Employee
class Employee(Base):
    __tablename__ = "employee"

    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(50))
    last_name = mapped_column(String(100))
    position = mapped_column(String(100))
    salary = mapped_column(Float)

# # Ale można (i jest zalecane) używanie anotacji (aka type hinting)
# # To jest najnowszy sposób tworzenia modeli w sqlalchemy
# from typing import Optional
# from sqlalchemy.orm import Mapped
# class Employee(DeclarativeBase):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     first_name: Mapped[str] = mapped_column(String(50))
#     last_name: Mapped[str]
#     position: Mapped[Optional[str]]
#     salary: Mapped[float]

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db2"
engine = create_engine(conn_str)

# CREATE TABLE (C z CRUD dla DDL)
Base.metadata.create_all(engine)

# DROP TABLE (D z CRUD dla DDL)
# Base.metadata.drop_all(engine)
print("Done.")

