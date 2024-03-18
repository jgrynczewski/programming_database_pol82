# Reflecting All Tables at Once (metoda reflect)
# https://docs.sqlalchemy.org/en/20/core/reflection.html#reflecting-all-tables-at-once
from sqlalchemy import create_engine, MetaData, Table

metadata_obj = MetaData()

# Tworzenie silnika - łączenie się z bazą danych MySQL
engine = create_engine("mysql+mysqlconnector://root:admin@localhost/world")

# use the given engine to query the database for information about the country table
metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)
print(metadata_obj.tables.keys())  # reflected `city` and `country`
