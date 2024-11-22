from flask import Flask, request, flash, redirect, url_for, session, render_template
from database import initDB
from controllers.credenciales import login, register, logout
from controllers.productos import productos

app = Flask(__name__)
app.secret_key = 'ggfhgghhggfdghjkmlhgf'
initDB(app)

def landing():
    return render_template('index.html')

# Rutas para la página principal
app.add_url_rule('/', 'landing', landing)
app.add_url_rule('/index', 'index', landing)
app.add_url_rule('/landing', 'landing', landing)


# Rutas para las credenciales
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET'])

# Rutas para los productos
app.add_url_rule('/patinetas', 'patinetas', productos, defaults={'tipo': 'patinetas'})
app.add_url_rule('/tablas', 'tablas', productos, defaults={'tipo': 'tablas'})
app.add_url_rule('/ejes', 'ejes', productos, defaults={'tipo': 'ejes'})
app.add_url_rule('/ruedas', 'ruedas', productos, defaults={'tipo': 'ruedas'})

def cart():
    return 'Welcome to the cart page!'
app.add_url_rule('/cart', 'cart', cart)