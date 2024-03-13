# SQLAlchemy Expression Language (R z CRUD dla DQL) metoda select obiektu klasy Table
# Zadanie 6: Wykonywanie zapytań
#
# Wykonaj zapytanie SELECT na tabeli "employee" i wyświetl wyniki.



from sqlalchemy import create_engine, select

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

stmt = employee_table.select()

with engine.connect() as conn:
    cursor_result = conn.execute(stmt)  # <class 'sqlalchemy.engine.cursor.CursorResult'>

    for row in cursor_result:
        print(f"({row.id}) {row.first_name} {row.last_name} - {row.position} [{row.salary}]")

print("Done.")
