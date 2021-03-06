from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from models import db, db_connect, Store, StoreItem, StoreSchema
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///udemy_stores'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "KJOJKLJKJLKJL"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug=True

debug = DebugToolbarExtension(app)

db_connect(app)
# db.drop_all()
db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

stores = []

@app.route('/store', methods=['POST'])
def create_store():
    pass
    
@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    stores = Store.query.all()
    print(stores)
    store_schema = StoreSchema(many=True)
    print(store_schema)
    output = store_schema.dump(stores)
    return jsonify({'stores': output})

    

   
    # serialized_stores = [store.serialize_store() for store in stores]
    # serialized_items = [item.serialize_store_item() for item in store_items]
    
    # return jsonify(stores=serialized_stores, items=serialized_items)
    # return render_template('stores.html', stores=stores)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass



