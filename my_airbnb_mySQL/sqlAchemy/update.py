
from connect import create_connection
from main import Company
from sqlalchemy.orm import sessionmaker


engine = create_connection()
Session = sessionmaker(bind=engine)
session = Session()

''' query data '''
staff = session.query(Company).filter_by(name='Samuel Ude').first()
print(staff)
if staff:
    staff.phone = '390-0309'
    session.commit()
    print('staff profile updated successfully')
else:
    print('staff not found')
