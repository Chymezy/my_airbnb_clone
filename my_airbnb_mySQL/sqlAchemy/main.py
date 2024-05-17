from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

''' create engine to your database '''
engine = create_engine('mysql+mysqlconnector://chymezy:password@localhost/josh_db')

''' create a connection or traction handler with db '''
Session = sessionmaker(bind=engine)
session = Session()

''' handles your model definitions and packaging '''
Base = declarative_base()

''' model your table '''
class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    department = Column(String(20))
    email = Column(String(50))
    phone = Column(String(20))


''' create table in database. metadata collates ur table structure '''
Base.metadata.create_all(engine)

# ''' insert data into the created table '''
# new_student = Student(name='Joshua Benjamin')
# session.add(new_student)
# session.commit()

# ''' retrieved data '''
# students = session.query(Student).all()
# for student in students:
#     print(student.id, student.name)
    


