# Zadanie 13: Dodanie danych do drugiej tabeli
#
# Dodaj co najmniej dwa działy do tabeli "departments".


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Department  # Zakładając, że model Department jest zdefiniowany w oddzielnym module

# Tworzenie silnika - łączenie się z bazą danych MySQL
engine = create_engine('mysql+mysqlconnector://root:admin@localhost/company_db2')

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Dodawanie nowych działów
department1 = Department(name='HR', manager_id=1)
department2 = Department(name='IT', manager_id=2)

session.add_all([department1, department2])
session.commit()

print("Dodano nowe działy do tabeli 'departments' pomyślnie.")
