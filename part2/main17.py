# SQLAlchemy Expression Language (R z CRUD dla DQL) funkcja select, fetchone
# Zadanie 5: Usuwanie danych
#
# Usuń pracownika o id=3 z tabeli "employee".



from sqlalchemy import create_engine, select

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

stmt = select(employee_table)

with engine.connect() as conn:
    cursor_result = conn.execute(stmt)  # <class 'sqlalchemy.engine.cursor.CursorResult'>
    row = cursor_result.fetchone()  # <class 'sqlalchemy.engine.row.Row'>

    while row:
        print(f"({row.id}) {row.first_name} {row.last_name} - {row.position} [{row.salary}]")
        row = cursor_result.fetchone()

print("Done.")
