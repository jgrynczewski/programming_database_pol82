# Zadanie 12: Wybór danych z połączonych tabel (join)
#
# Wykonaj zapytanie SELECT, które połączy dane z tabel "employee" i "department" tak,
# aby wyświetlić imiona i nazwiska pracowników razem z nazwami ich działów.

from sqlalchemy import create_engine, select

from tables import employee_table, department_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

# Sposób I (funkcja select)
stmt = select(
    employee_table.c.first_name,
    employee_table.c.last_name,
    department_table.c.name
).join(
   department_table, employee_table.c.department_id == department_table.c.id
)

# Sposób II (metoda select)
stmt = employee_table.select(
).with_only_columns(
    employee_table.c.first_name,
    employee_table.c.last_name,
    department_table.c.name
).join(
    department_table, employee_table.c.department_id == department_table.c.id
)

with engine.connect() as conn:
    cursor_result = conn.execute(stmt)  # <class 'sqlalchemy.engine.cursor.CursorResult'>
    result = cursor_result.fetchall()  # <class 'list'>

    for row in result:
        print(f"{row[0]} {row[1]} - {row[2]}")

print("Done.")
