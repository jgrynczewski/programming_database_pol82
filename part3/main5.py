# SQLAlchemy Expression Language (U z CRUD dla DML) metoda update obiektu klasy Table
# Zadanie 4: Aktualizacja danych (dml)
#
# Zaktualizuj pensję użytkownika o first_name=Alice z tabeli "employee" na 6000.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Employee

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db2"
engine = create_engine(conn_str, echo=True)

Session = sessionmaker(bind=engine)
with Session() as session:
    session.query(Employee).filter_by(first_name='Alice').update({'salary': 6000})
    session.commit()

# Ale można spotkać też i taki kod
with Session() as session:
    employees = session.query(Employee).filter_by(first_name='Alice')

    for employee in employees:
        employee.salary = 6000
        session.commit()


print("Done.")
