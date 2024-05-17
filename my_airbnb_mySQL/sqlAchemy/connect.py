from sqlalchemy import create_engine

def create_connection():
    username = 'chymezy'
    password = 'password'
    hostname = 'localhost'
    port = 3306
    database_name = 'josh_db'

    connection_string = f'mysql+mysqlconnector://{username}:{password}@{hostname}:{port}/{database_name}'
    engine = create_engine(connection_string)

    return engine
