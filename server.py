from flask import Flask,request
import json
from config import DB
app = Flask(__name__)#__name__ this is using for the name of the folder.

@app.get('/')
def home():
    return "Hello from flask"

@app.get('/testing')
def testing():
    return "Hello from another page"

#create 2 more API (about page and blog page)

@app.get('/about')
def about():
    me = {"name": "Mauricio"}
    return json.dumps(me)

@app.get('/blog')
def blog():
    return "This is the blog page"

@app.get('/version')
def version():
    version = {"name": "mouse", "version": "2", "build": 123456}
    return json.dumps(version)
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj
# this time we need to read and write in to the server
products = []
@app.get('/api/products')
def get_products():
    
    products = list(DB.products.find({}))
    return json.dumps(products)

@app.post('/api/products')
def save_products():
    product = request.get_json()
    DB.products.insert_one(product)
    # products.append(product)
    return json.dumps(fix_id(product))
app.run(debug=True) # Apply the changes on the code,live 


# API / Endpoints
#transform JSON / convert JSON in an object again






