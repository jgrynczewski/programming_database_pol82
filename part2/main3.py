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

stmt = text("""
INSERT INTO employee(first_name, last_name, position, salary) VALUES
('John', 'Doe', 'Manager', 5000.00),
('Jane', 'Smith', 'Developer', 4000.00),
('Alice', 'Johnson', 'HR', 4500.00)
;""")

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

print("Done.")
