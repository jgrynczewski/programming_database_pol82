# SQLAlchemy Expression Language (R z CRUD dla DQL) funkcja select, dostęp do obiektu Row - rozpakowywanie sekwencji
# Zadanie 6: Wykonywanie zapytań
#
# Wykonaj zapytanie SELECT na tabeli "employee" i wyświetl wyniki.



from sqlalchemy import create_engine, select

from tables import employee_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

stmt = select(employee_table)

with engine.connect() as conn:
    cursor_result = conn.execute(stmt)  # <class 'sqlalchemy.engine.cursor.CursorResult'>
    result = cursor_result.fetchall()  # <class 'list'>

    for row in result:
        # Klasa Row zachowuje się identycznie jak namedtuple (z modułu collection)
        print(f"({row.id}) {row.first_name} {row.last_name} - {row.position} [{row.salary}]")  # po atrybucie
print("Done.")
