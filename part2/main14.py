# SQLAlchemy Expression Language (R z CRUD dla DQL) funkcja select, dostęp do obiektu Row po indeksie
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
    result = cursor_result.fetchall()  # <class 'list'>

    for row in result:
        print(f"({row[0]}) {row[1]} {row[2]} - {row[3]} [{row[4]}]")  # po indeksie

print("Done.")
