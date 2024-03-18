# Zadanie 15: Zapytanie z warunkiem na połączonych tabelach (przykład na join)
#
# Wykonaj zapytanie, aby wyświetlić pracowników, którzy pracują w określonym dziale.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Employee, Department  # Zakładając, że modele Employee i Department są zdefiniowane w oddzielnym module

# Tworzenie silnika - łączenie się z bazą danych MySQL
engine = create_engine('mysql+mysqlconnector://root:admin@localhost/company_db2')

# Wybór nazwy działu, dla którego chcemy znaleźć pracowników
department_name = 'IT'

# Tworzenie sesji
Session = sessionmaker(bind=engine)
with Session() as session:
    # Wyświetlenie pracowników pracujących w dziale department_name
    employees_in_department = session.query(Employee).join(Department).filter(Department.name == department_name).all()

    print(f"Pracownicy w dziale {department_name}:")
    for employee in employees_in_department:
        print(f"{employee.first_name} {employee.last_name} - {employee.position}")
