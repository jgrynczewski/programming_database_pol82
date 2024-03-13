# SQLAlchemy Expression Language (R z CRUD dla DQL) funkcja select, mappings
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
    mapping_result = cursor_result.mappings()  # <class 'sqlalchemy.engine.result.MappingResult'>

    for mapping in mapping_result:
        print(f"({mapping['id']}) {mapping.get('first_name')} {mapping.get('last_name')} - {mapping.get('position')} [{mapping.get('salary')}]")


print("Done.")
