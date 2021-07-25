from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from models import db, db_connect, Store, StoreItem

app = Flask(__name__)
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
    return "Hello, World!"

stores = []

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass


