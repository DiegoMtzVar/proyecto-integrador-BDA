from flask import Flask, request, flash, redirect, url_for, session, render_template
from database import initDB, mysql
from controllers.credentials import login, register, logout, userAPI
from controllers.shop import index, productGallery, cart, single_product, resena, checkout, finalizarCompra, comprasRecientes, cupon
from controllers.dashboard import *
app = Flask(__name__)
app.secret_key = 'ggfhgghhggfdghjkmlhgf'
initDB(app)

# Rutas para la página principal
app.add_url_rule('/', 'index', index)


# Rutas para las credenciales
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout)
app.add_url_rule('/api/user', 'userAPI', userAPI)

# Rutas para la tienda
app.add_url_rule('/patinetas', 'patinetas', productGallery, defaults={'category': 'Completa'})
app.add_url_rule('/tablas', 'tablas', productGallery, defaults={'category': 'Tabla'})
app.add_url_rule('/ruedas', 'ruedas', productGallery, defaults={'category': 'Rueda'})
app.add_url_rule('/ejes', 'ejes', productGallery, defaults={'category': 'Eje'})
app.add_url_rule('/cart', 'cart', cart)
app.add_url_rule('/single-product/<int:id>', 'single_product', single_product)
app.add_url_rule('/checkout','checkout',checkout)
app.add_url_rule('/cupon','cupon',cupon, methods=['POST'])
app.add_url_rule('/finalizarCompra','finalizarCompra',finalizarCompra,methods=['POST'])
app.add_url_rule('/comprasRecientes','comprasRecientes',comprasRecientes)

#ruta para reseña
app.add_url_rule('/resena/<int:id>', 'resena', resena, methods=['GET', 'POST'])

# Rutas para el dashboard
app.add_url_rule('/dashboard', 'dashboard', dashboard)
app.add_url_rule('/dashboard/masCompradoHisto', 'masCompradoHisto', mostSold)
app.add_url_rule('/dashboard/porcentajeProveedor', 'porcentajeProveedor', providerPercentage)

app.add_url_rule('/dashboard/ventas', 'ventas', ventas)
app.add_url_rule('/dashboard/ventas/update/<int:ventaID>/<int:statusID>', 'ventas-updateStatus', updateStatus)

app.add_url_rule('/dashboard/proveedores', 'proveedores', proveedores)

app.add_url_rule('/dashboard/usuariosGestion', 'usuariosGestion', usuariosGestion)
app.add_url_rule('/dashboard/usuariosGestion/promote/<int:userID>', 'usuariosGestion-promote', promote)
app.add_url_rule('/dashboard/usuariosGestion/demote/<int:userID>', 'usuariosGestion-demote', demote)
app.add_url_rule('/dashboard/usuariosGestion/delete/<int:userID>', 'usuariosGestion-delete', deleteUser)
app.add_url_rule('/dashboard/usuariosGestion/getRecentPurchases/<int:userID>', 'getRecentPurchases', getRecentPurchases)
app.add_url_rule('/dashboard/proveedores/getProductsInPurchase/<int:userID>', 'getProductsInPurchase', getProductsInPurchase)
app.add_url_rule('/dashboard/productosGestion', 'productosGestion', productosGestion, methods=['GET', 'POST'])

app.add_url_rule('/dashboard/promociones', 'promociones', promociones)

app.add_url_rule('/dashboard/masCompradoHisto', 'masCompradoHisto', mostSold)
app.add_url_rule('/dashboard/porcentajeProveedor', 'porcentajeProveedor', providerPercentage)
app.add_url_rule('/dashboard/totalProveedorMes', 'totalProveedorMes', totalProveedorMes)
app.add_url_rule('/dashboard/totalProveedor', 'totalProveedor', totalProveedor)
app.add_url_rule('/dashboard/stockProducts', 'stockProducts', stockProducts)


app.register_error_handler(404, lambda e: flash('Página no encontrada', category='error') or redirect(url_for('index')))
app.register_error_handler(500, lambda e: flash('Error interno del servidor', category='error') or redirect(url_for('index')))


@app.route('/f')
def test():
    flash('Esto es una prueba', category='info')
    return render_template('index.html')

@app.route('/sc')
def reset():
    session.clear()
    return redirect(url_for('index'))