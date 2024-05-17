from tabulate import tabulate
from connect import create_connection
from sqlalchemy.orm import sessionmaker
from main import Company

engine = create_connection()

Session = sessionmaker(bind=engine)
session = Session()

''' query students '''
staff = session.query(Company).all()
# for employee in staff:
#     print(employee.name, employee.department)

''' convert the query result to a list of dictionaries '''
data = [dict(row.__dict__) for row in staff]
print(tabulate(data, headers='keys'))


session.close()