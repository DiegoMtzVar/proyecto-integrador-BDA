from flask import Flask, request, flash, redirect, url_for, session, render_template
from database import initDB
from controllers.credenciales import login, register, logout
from controllers.shop import index, patinetas

app = Flask(__name__)
app.secret_key = 'ggfhgghhggfdghjkmlhgf'
initDB(app)

def landing():
    if session.get("user") and session["user"].role == 'admin': return render_template('dashboard.html')

    return index()

# Rutas para la página principal
app.add_url_rule('/', 'landing', landing)
app.add_url_rule('/landing', 'landing', landing)


# Rutas para las credenciales
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET'])

# Rutas para los productos
app.add_url_rule('/patinetas', 'patinetas', patinetas)

def cart():
    return 'Welcome to the cart page!'
app.add_url_rule('/cart', 'cart', cart)

@app.route('/test')
def test():
    return render_template('index2.html')