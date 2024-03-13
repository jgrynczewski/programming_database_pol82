# BEGIN once
# Zadanie 3: Wstawianie danych (dml)
#
# Dodaj co najmniej trzy rekordy do tabeli "employee".
# Przykładowe dane:
# {'first_name': 'John', 'last_name': 'Doe', 'position': 'Manager', 'salary': 5000.00},
# {'first_name': 'Jane', 'last_name': 'Smith', 'position': 'Developer', 'salary': 4000.00},
# {'first_name': 'Alice', 'last_name': 'Johnson', 'position': 'HR', 'salary': 4500.00}

from sqlalchemy import create_engine, text

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db"
engine = create_engine(conn_str, echo=True)

stmt1 = text("""
INSERT INTO employee(first_name, last_name, position, salary) VALUE
('John', 'Doe', 'Manager', 5000.00)
;""")
stmt2 = text("""
INSERT INTO employee(first_name, last_name, position, salary) VALUE
('Jane', 'Smith', 'Developer', 4000.00)
;""")
stmt3 = text("""
INSERT INTO employee(first_name, last_name, position, salary) VALUE
('Alice', 'Johnson', 'HR', 4500.00)
;""")

# BEGIN once
with engine.begin() as conn:
    conn.execute(stmt1)
    conn.execute(stmt2)
    conn.execute(stmt3)

print("Done.")
