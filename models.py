
from flask import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_marshmallow import Marshmallow

db = SQLAlchemy()


def db_connect(app):
    db.app = app
    db.init_app(app)

ma = Marshmallow(app)

"""Models for Store App."""

class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    items = db.relationship('StoreItem', backref=backref('store_items', cascade="all, delete"))
    
    def __repr__(self):
        return "<Store: {}>".format(self.name)
        
    # def serialize_store(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name
    #     }

class StoreItem(db.Model):
    __tablename__ = "store_items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('Store')
    
    

    def __repr__(self):
        return "<StoreItem: {}>".format(self.name)

    # def serialize_store_item(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "price": self.price,
    #         "store_id": self.store_id
    #     }

class StoreSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Store

    id = ma.auto_field()
    name = ma.auto_field()
    items = ma.auto_field(many=True)
    

class StoreItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StoreItem
        include_fk = True

    






