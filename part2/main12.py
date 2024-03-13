# SQLAlchemy Expression Language (D z CRUD dla DML) metoda delete obiektu klasy Table
# Zadanie 5: Usuwanie danych
#
# Usuń pracownika o id=3 z tabeli "employee".


from sqlalchemy import create_engine, delete

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

stmt = employee_table.delete().where(employee_table.c.id == 32)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

print("Done.")
