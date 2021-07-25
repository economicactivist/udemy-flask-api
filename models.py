
from flask import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def db_connect(app):
    db.app = app
    db.init_app(app)


"""Models for Store App."""

class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return "<Store: {}>".format(self.name)

class StoreItem(db.Model):
    __tablename__ = "store_items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("Store", backref=db.backref("store_items", lazy=True))

    def __repr__(self):
        return "<StoreItem: {}>".format(self.name)

