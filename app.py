from flask import Flask, request, flash, redirect, url_for, session, render_template
from database import initDB
from controllers.credenciales import login, register, logout
from controllers.productos import patinetas, tablas, ejes, ruedas

app = Flask(__name__)
app.secret_key = 'ggfhgghhggfdghjkmlhgf'
initDB(app)

def landing():
    return render_template('index.html')

app.add_url_rule('/', 'landing', landing)
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET'])

app.add_url_rule('/patinetas', 'patinetas', patinetas)
app.add_url_rule('/tablas', 'tablas', tablas)
app.add_url_rule('/ejes', 'ejes', ejes)
app.add_url_rule('/ruedas', 'ruedas', ruedas)

def cart():
    return 'Welcome to the cart page!'
app.add_url_rule('/cart', 'cart', cart)