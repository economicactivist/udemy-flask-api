from app import app
from models import db, Store, StoreItem


db.drop_all()
db.create_all()

s1 = Store(name='Amazon')
s2 = Store(name='Ebay')
s3 = Store(name='Walmart')

si1 = StoreItem(name='Pant', price=10.00, store_id=1)
si2 = StoreItem(name='Shirt', price=15.00, store_id=1)
si3 = StoreItem(name='T-Shirt', price=5.00, store_id=2)
si4 = StoreItem(name='Jeans', price=20.00, store_id=2)
si5 = StoreItem(name='Shoes', price=10.00, store_id=3)
si6 = StoreItem(name='Socks', price=5.00, store_id=3)





db.session.add_all([s1, s2, s3, si1, si2, si3, si4, si5, si6])
db.session.commit()