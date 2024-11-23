from flask import Flask, request, flash, redirect, url_for, session, render_template
from database import initDB
from controllers.credenciales import login, register, logout, userAPI
from controllers.shop import index, productGallery, cart

app = Flask(__name__)
app.secret_key = 'ggfhgghhggfdghjkmlhgf'
initDB(app)

def landing():
    if session.get("user") and session["user"]["role"] == 'admin': return render_template('dashboard.html')

    return index()

# Rutas para la página principal
app.add_url_rule('/', 'landing', landing)
app.add_url_rule('/landing', 'landing', landing)


# Rutas para las credenciales
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET'])
app.add_url_rule('/api/user', 'userAPI', userAPI, methods=['GET'])

# Rutas para los productos
app.add_url_rule('/patinetas', 'patinetas', productGallery, defaults={'category': 'Completa'})
app.add_url_rule('/tablas', 'productGallery', productGallery, defaults={'category': 'Tabla'})
app.add_url_rule('/ruedas', 'productGallery', productGallery, defaults={'category': 'Rueda'})
app.add_url_rule('/ejes', 'productGallery', productGallery, defaults={'category': 'Eje'})
app.add_url_rule('/cart', 'cart', cart)


