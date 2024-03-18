from sqlalchemy import MetaData, Table, Column, Integer, Float, String, ForeignKey

metadata = MetaData()
# wersja do zadania 25
# employee_table = Table(
#     'employee',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('first_name', String(50)),
#     Column('last_name', String(100)),
#     Column('position', String(100)),
#     Column('salary', Float)
# )

# wersja od zadania 25
employee_table = Table(
    'employee',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(100)),
    Column('position', String(100)),
    Column('salary', Float),
    Column('department_id', Integer, ForeignKey("department.id")),
)

department_table = Table(
    'department',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('manager_id', Integer, ForeignKey('employee.id'), nullable=False)
)
