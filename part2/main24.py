# SQLAlchemy Expression Language (R z CRUD dla DQL) grupowanie i funkcje agregujące
# Zadanie 9: Grupowanie wyników
#
# Wykonaj zapytanie SELECT grupujące pracowników według ich stanowiska i wyświetlające liczbę osób na danym stanowsku.

from sqlalchemy import create_engine, select, func

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)  # lazy initialization (leniwe inicjalizowanie)

# Sposób I (na bazie funkcji select)
stmt = select(
    employee_table.c.position,
    func.count()
).group_by(
    employee_table.c.position
)

# Sposób II (na bazie metody select)
stmt = employee_table.select(
).with_only_columns(
    employee_table.c.position,
    func.count()
).group_by(
    employee_table.c.position
)

with engine.connect() as conn:
    cursor_result = conn.execute(stmt)  # <class 'sqlalchemy.engine.cursor.CursorResult'>

    for row in cursor_result:
        print(f"({row})")

print("Done.")
