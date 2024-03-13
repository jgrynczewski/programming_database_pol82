# SQLAlchemy Expression Language (R z CRUD dla DQL) funkcja select, filtry
# Zadanie 7: Warunki w zapytaniu
#
# Wykonaj zapytanie SELECT z warunkiem WHERE, aby wybrać pracowników o pensji większej niż 4500.



from sqlalchemy import create_engine, select

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

stmt = select(employee_table).where(employee_table.c.salary > 4500)

with engine.connect() as conn:
    cursor_result = conn.execute(stmt)  # <class 'sqlalchemy.engine.cursor.CursorResult'>

    for row in cursor_result:
        print(f"({row.id}) {row.first_name} {row.last_name} - {row.position} [{row.salary}]")

print("Done.")
