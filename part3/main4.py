# SQLAlchemy Expression Language (R z CRUD dla DQL)
# Zadanie 4: Wyświetlanie danych (dql)

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from models import Employee

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db2"
engine = create_engine(conn_str, echo=True)

Session = sessionmaker(bind=engine)

# Wyświetl wszystkich pracowników
with Session() as session:
    employees = session.query(Employee).all()
    for employee in employees:  # <models.Employee object at ...>
        print(f"{employee.first_name} {employee.last_name}")

# Wyświetl pracownika, którego pierwsze imię to `Alice`
with Session() as session:
    employees = session.query(Employee).filter_by(first_name='Alice')
    for employee in employees:  # <models.Employee object at ...>
        print(f"{employee.first_name} {employee.last_name}")

# Pogrupuj pracowników po stanowiskach
with Session() as session:
    result = session.query(Employee.position, func.count()).group_by(Employee.position)
    for row in result:
        print(f"{row}")  # tym razem to już tuple (no ale przecież wyciągamy z bazy tylko wartość position
        # i wynik działania funkcji count)
