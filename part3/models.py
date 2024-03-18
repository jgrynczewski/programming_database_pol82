from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


# model Employee
class Employee(Base):
    __tablename__ = "employee"

    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(50))
    last_name = mapped_column(String(100))
    position = mapped_column(String(100))
    salary = mapped_column(Float)
