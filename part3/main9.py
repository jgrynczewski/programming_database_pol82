# Zadanie 13: Update istniejących userów o department_id
#
# Dopisz department_id istniejącym użytkownikom


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Employee, Department  # Zakładając, że model Department jest zdefiniowany w oddzielnym module

# Tworzenie silnika - łączenie się z bazą danych MySQL
engine = create_engine('mysql+mysqlconnector://root:admin@localhost/company_db2')

# Tworzenie sesji
Session = sessionmaker(bind=engine)
with Session() as session:
    session.query(Employee).filter_by(id=1).update({'department_id': 2})
    session.query(Employee).filter_by(id=2).update({'department_id': 1})
    session.query(Employee).filter_by(id=3).update({'department_id': 2})
    session.commit()

print("Update userów przebiegł pomyślnie.")
