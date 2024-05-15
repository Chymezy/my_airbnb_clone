from connect import create_connection
from sqlalchemy.orm import sessionmaker
from main import Student

engine = create_connection()

Session = sessionmaker(bind=engine)
session = Session()

new_student = Student(name='Samuel Ude')
session.add(new_student)
session.commit()

session.close()