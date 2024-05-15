from sqlalchemy import create_engine, text


def create_connection():
    username = 'chymezy'
    password = 'password'
    hostname = 'localhost'
    port = '3306'
    database_name = 'josh_db'
    database_url = f'mysql+mysqlconnector://{username}:{password}@{hostname}:{port}/{database_name}'
    database_url

    ''' create access engine to database '''
    engine = create_engine(database_url)
    return engine
database_engine = create_connection()

with database_engine.connect() as conn:
    result = conn.execute(text('SELECT "Hello World"'))
    print(result.all())


