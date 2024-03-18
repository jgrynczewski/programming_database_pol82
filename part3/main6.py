# SQLAlchemy Expression Language (D z CRUD dla DML)
# Zadanie 4: Usuwanie danych (dml)
#
# Usuń użytkownika o first_name=Alice.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Employee

# napis połączeniowy (ang. connection string)
conn_str = "mysql+mysqlconnector://root:admin@localhost/company_db2"
engine = create_engine(conn_str, echo=True)

Session = sessionmaker(bind=engine)
with Session() as session:
    session.query(Employee).filter_by(first_name='Alice').delete()
    session.commit()

# Albo tak
with Session() as session:
    employees = session.query(Employee).filter_by(first_name='Alice')

    for employee in employees:
        session.delete(employee)
        session.commit()


print("Done.")
