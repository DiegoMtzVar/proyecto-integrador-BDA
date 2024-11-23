from flask import Flask, request, flash, redirect, url_for, session, render_template
from database import initDB
from controllers.credenciales import login, register, logout, userAPI
from controllers.shop import index, productGallery, cart, single_product
from controllers.dashboard import dashboard

app = Flask(__name__)
app.secret_key = 'ggfhgghhggfdghjkmlhgf'
initDB(app)

# Rutas para la página principal
app.add_url_rule('/', 'landing', index)
app.add_url_rule('/landing', 'landing', index)


# Rutas para las credenciales
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET'])
app.add_url_rule('/api/user', 'userAPI', userAPI, methods=['GET'])

# Rutas para los productos
app.add_url_rule('/patinetas', 'patinetas', productGallery, defaults={'category': 'Completa'})
app.add_url_rule('/tablas', 'tablas', productGallery, defaults={'category': 'Tabla'})
app.add_url_rule('/ruedas', 'ruedas', productGallery, defaults={'category': 'Rueda'})
app.add_url_rule('/ejes', 'ejes', productGallery, defaults={'category': 'Eje'})
app.add_url_rule('/cart', 'cart', cart)


