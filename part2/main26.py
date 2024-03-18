# Zadanie 11 : Wstawianie danych (dml)
#
# Dodaj co najmniej trzy rekordy do tabeli "employee".
# Przykładowe dane:
# {'first_name': 'John', 'last_name': 'Doe', 'position': 'Manager', 'salary': 5000.00},
# {'first_name': 'Jane', 'last_name': 'Smith', 'position': 'Developer', 'salary': 4000.00},
# {'first_name': 'Alice', 'last_name': 'Johnson', 'position': 'HR', 'salary': 4500.00}

# Dodaj co najmniej trzy rekordy do tabeli "department".
# Przykładowe dane:
# {'name':'HR', 'manager_id': 2},
# {'name':'IT', 'manager_id': 3}

from sqlalchemy import create_engine, insert, update

from tables import employee_table, department_table

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

insert_employees_query = insert(employee_table).values([
    {'first_name': 'John', 'last_name': 'Doe', 'position': 'Manager', 'salary': 5000.00},
    {'first_name': 'Jane', 'last_name': 'Smith', 'position': 'Developer', 'salary': 4000.00},
    {'first_name': 'Alice', 'last_name': 'Johnson', 'position': 'HR', 'salary': 4500.00}
])

insert_departments_query = insert(department_table).values([
    {'name':'HR', 'manager_id': 2},
    {'name':'IT', 'manager_id': 3}
])

update_employee1_query = update(employee_table).where(employee_table.c.id == 1).values(department_id=2)
update_employee2_query = update(employee_table).where(employee_table.c.id == 2).values(department_id=1)
update_employee3_query = update(employee_table).where(employee_table.c.id == 3).values(department_id=2)

with engine.connect() as conn:
    conn.execute(insert_employees_query)
    conn.execute(insert_departments_query)
    conn.execute(update_employee1_query)
    conn.execute(update_employee2_query)
    conn.execute(update_employee3_query)
    conn.commit()

print("Done.")
