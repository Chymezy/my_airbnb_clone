from sqlalchemy import create_engine, text

# create engine
engine = create_engine("mysql+mysqlconnector://chymezy:password@localhost:3306/josh_db")

with engine.connect() as connection:
    # Create a text construct for the SQL query
    query = text('select "Hello"')
    
    # Execute the query
    result = connection.execute(query)
    
    # Fetch and print the results
    print(result.fetchall())
