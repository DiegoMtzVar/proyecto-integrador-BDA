from flask import render_template
from models import productos

def patinetas():
    data = productos.getProducts('patinetas')
    return render_template('productos.html', productos=data, tipo='patinetas')

def tablas():
    data = productos.getProducts('tablas')
    return render_template('productos.html', productos=data, tipo='tablas')

def ejes():
    data = productos.getProducts('ejes')
    return render_template('productos.html', productos=data, tipo='ejes')

def ruedas():
    data = productos.getProducts('ruedas')
    return render_template('productos.html', productos=data, tipo='ruedas')