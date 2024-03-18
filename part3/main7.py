# Zadanie 12: Relacje między tabelami
#
# Utwórz drugi model "Department" reprezentujący działy w firmie i dodaj relację między "Employee" a "Department".


from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship

# Tworzenie silnika - łączenie się z bazą danych MySQL
engine = create_engine('mysql+mysqlconnector://root:admin@localhost/company_db2')


# Deklarowanie klasy bazowej dla modeli
class Base(DeclarativeBase):
    pass


# Definicja modelu Employee
class Employee(Base):
    __tablename__ = 'employee'

    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(50))
    last_name = mapped_column(String(100))
    position = mapped_column(String(100))
    salary = mapped_column(Float)
    department_id = mapped_column(Integer, ForeignKey('department.id'))

    # Definicja relacji między Employee a Department
    department = relationship("Department", back_populates="employees")


# Definicja modelu Department
class Department(Base):
    __tablename__ = 'department'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    manager_id = mapped_column(Integer)

    # Definicja relacji między Department a Employee
    employees = relationship("Employee", back_populates="department")


# Tworzenie tabeli w bazie danych na podstawie modelu
Base.metadata.create_all(engine)

print("Done.")
