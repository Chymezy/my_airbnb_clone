from connect import create_connection
from sqlalchemy.orm import sessionmaker
from main import Company

engine = create_connection()

Session = sessionmaker(bind=engine)
session = Session()

new_staff = Company(name='Samuel Ude', department='Engineering', email='USamuel@engineering.com', phone="0810716094")
session.add(new_staff)
session.commit()

session.close()