# SQLAlchemy Expression Language (U z CRUD dla DML) funckja update
# Zadanie 4: Aktualizacja danych (dml)
#
# Zaktualizuj pensję użytkownika o id=4 z tabeli "employee" na 6000.


from sqlalchemy import create_engine, update

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

stmt = update(employee_table).values(salary=6000).where(employee_table.c.id == 4)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

print("Done.")
