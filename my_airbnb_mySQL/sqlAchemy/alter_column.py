from connect import create_connection
from sqlalchemy import MetaData, Table, Column, String

# Create a connection to the database
engine = create_connection()

# Reflect the database schema
metadata = MetaData()
metadata.reflect(bind=engine)

# Get the 'company' table from the metadata
staff_update = metadata.tables['company']

# Begin a transaction
with engine.connect() as connection:
    with connection.begin():
        # Alter the 'name' column of the 'company' table to have a new name
        staff_update.c.name.alter(name='manager')