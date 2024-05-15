from connect import create_connection
from sqlalchemy.orm import sessionmaker
from main import Student

engine = create_connection()

Session = sessionmaker(bind=engine)
session = Session()

''' query students '''
students = session.query(Student).all()
for student in students:
    print(student.id, student.name)

session.close()