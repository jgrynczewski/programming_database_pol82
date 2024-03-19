from sqlalchemy import create_engine, MetaData, Table

metadata_obj = MetaData()

# Tworzenie silnika - łączenie się z bazą danych MySQL
engine = create_engine("mysql+mysqlconnector://root:admin@localhost/world")

# use the given engine to query the database for information about the country table
city = Table(
    "city",
    metadata_obj,
    autoload_with=engine
)

print([c.name for c in city.columns])

# When tables are reflected, if a given table references another one via foreign key,
# a second Table object is created within the MetaData object representing the connection.
print(metadata_obj.tables.keys())  # reflected `city` and `country`

stmt = city.select().limit(10)

with engine.connect() as conn:
    result = conn.execute(stmt)
    for country in result:
        print(country.Name)


# # można również odbijać tabelę z równoczesną jej modyfikacją
# # https://docs.sqlalchemy.org/en/20/core/reflection.html#overriding-reflected-columns
# mytable = Table(
#     "mytable",
#     metadata_obj,
#     Column(
#         "id", Integer, primary_key=True
#     ),  # override reflected 'id' to have primary key
#     Column("mydata", Unicode(50)),  # override reflected 'mydata' to be Unicode
#     # additional Column objects which require no change are reflected normally
#     autoload_with=some_engine,
# )
#
# # można odbijać widoki
# # https://docs.sqlalchemy.org/en/20/core/reflection.html#overriding-reflected-columns

