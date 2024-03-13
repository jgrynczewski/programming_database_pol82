# SQLAlchemy Expression Language (R z CRUD dla DQL) funkcja select, limit
# Zadanie 8: Limit
#
# Wykonaj zapytanie SELECT z warunkiem WHERE, aby wybrać pracowników o pensji większej niż 4500.
# Wynik posortuj alfabetycznie po kolumnie last_name, wyświetl 2 pierwszych pracowników



from sqlalchemy import create_engine, select

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)  # lazy initialization (leniwe inicjalizowanie)

stmt = select(employee_table) \
    .where(employee_table.c.salary > 4500) \
    .order_by(employee_table.c.last_name) \
    .limit(2)  # lazy evaluation aka lazy load (leniwe wykonywanie)

with engine.connect() as conn:
    cursor_result = conn.execute(stmt)  # <class 'sqlalchemy.engine.cursor.CursorResult'>

    for row in cursor_result:
        print(f"({row.id}) {row.first_name} {row.last_name} - {row.position} [{row.salary}]")

print("Done.")
