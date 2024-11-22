from flask import render_template
from models import products

def index():
    products = products.getRe()
    
    return render_template('index.html')

def patinetas():
    return render_template('patinetas.html', productos=products.getProductsbyType("patineta"))