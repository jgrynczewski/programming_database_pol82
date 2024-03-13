from sqlalchemy import MetaData, Table, Column, Integer, Float, String

metadata = MetaData()
employee_table = Table(
    'employee',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(100)),
    Column('position', String(100)),
    Column('salary', Float)
)
