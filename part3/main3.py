# C z CRUD dla DML (insert)
# Zadanie 3: Wstawianie danych (dml)
#
# Dodaj co najmniej trzy rekordy do tabeli "employee".
# Przykładowe dane:
# {'first_name': 'John', 'last_name': 'Doe', 'position': 'Manager', 'salary': 5000.00},
# {'first_name': 'Jane', 'last_name': 'Smith', 'position': 'Developer', 'salary': 4000.00},
# {'first_name': 'Alice', 'last_name': 'Johnson', 'position': 'HR', 'salary': 4500.00}

from sqlalchemy import create_engine, text

from sqlalchemy.orm import sessionmaker
from models import Employee

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db2"
engine = create_engine(conn_str, echo=True)

e1 = Employee(first_name='John', last_name='Doe', position='Manager', salary=5000.00)
e2 = Employee(first_name='Jane', last_name='Smith', position='Developer', salary=4000.00)
e3 = Employee(first_name='Alice', last_name='Johnson', position='HR', salary=4500.00)

Session = sessionmaker(bind=engine)
session = Session()

# można tak
# session.add(e1)
# session.add(e2)
# session.add(e3)
# session.commit()

# a można tak
session.add_all([e1, e2, e3])
session.commit()

print("Done.")
