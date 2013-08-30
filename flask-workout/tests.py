from sqlalchemy import create_engine
from models import *
from sqlalchemy.orm import sessionmaker

#db = create_engine('postgres://davide:uj2Eecha@localhost/test', echo=True)
db = create_engine('sqlite:///expenseapp.db', echo=False)
Base.metadata.create_all(db)

Session = sessionmaker(bind=db)
session = Session()

# -------- INSERT --------- #

context = ExpenseContext('House')
session.add(context)

category_1 = Category('Food', 2)
category_2 = Category('Technology', 2)
category_3 = Category('Cleaning', 2)
session.add_all([category_1, category_2, category_3])

products = []
products.append(Product('Bistecche', None, 2, None, 1))
products.append(Product('Cellulare', 'Nokia', None, None, 2))
products.append(Product('Detersivo piatti', 'Nelsen', 0.5, None, 3))
products.append(Product('Passata', 'Cirio', 1, '2013-09-05', 1))
session.add_all(products)

# -------- DELETE -------#

#bad_categories = session.query(Product).all()
#for category in bad_categories:
#    session.delete(category)

# ------- QUERY --------#

#session.commit()
#
#contexts = session.query(ExpenseContext).all()
#
#for context in contexts:
#    categories = session.query(Category).filter_by(context_id=context.id).all()
#    for category in categories:
#        products = session.query(Product).filter_by(category_id=category.id).all()
#        print len(products)
