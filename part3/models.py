from sqlalchemy import Integer, Float, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Definicja modelu Employee do zadań 1-6
# class Employee(Base):
#     __tablename__ = "employee"
#
#     id = mapped_column(Integer, primary_key=True)
#     first_name = mapped_column(String(50))
#     last_name = mapped_column(String(100))
#     position = mapped_column(String(100))
#     salary = mapped_column(Float)


# Definicja modelu Employee do zadań 7-10
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


# Definicja modelu Department do zadań 7-10
class Department(Base):
    __tablename__ = 'department'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    manager_id = mapped_column(Integer)

    # Definicja relacji między Department a Employee
    employees = relationship("Employee", back_populates="department")
