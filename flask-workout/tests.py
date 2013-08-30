from sqlalchemy import create_engine
from models import Base, ExpenseContext

#db = create_engine('postgres://davide:uj2Eecha@localhost/test', echo=True)
db = create_engine('sqlite:///expenseapp.db', echo=True)
#Base.metadata.create_all(db)

Session = sessionmaker(bind=engine)
session = Session()

