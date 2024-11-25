from flask import render_template, session, flash, url_for, redirect, jsonify, request
from models import analytics, user, products
from functools import wraps

# Función decoradora para asegurar que solo los administradores puedan acceder a las rutas
def secureRoute(route):
    @wraps(route)
    def wrapped_route(*args, **kwargs):
        if not session.get('user') or not session['user']['role'] == 'administrador':
            return redirect(url_for('index'))
        return route(*args, **kwargs)
    return wrapped_route

# Controladores del dashboard
@secureRoute
def dashboard():
    return render_template('dashboard/dashboard.html',  
                           gTotales = analytics.getTotalEarning(), 
                           inmes = analytics.getMonthIn(), 
                           outmes = analytics.getMonthOut())

@secureRoute
def mostSold():
    return analytics.mostSold()

@secureRoute
def providerPercentage():
    return analytics.providerPercentage()

@secureRoute
def totalProveedorMes():
    return analytics.totalMonthlySupplier()

@secureRoute
def totalProveedor():
    return analytics.providerTotal()

@secureRoute
def stockProducts():
    return analytics.stockProducts()

# Controladores de ventas y proveedores
@secureRoute
def ventas():
    return render_template('dashboard/ventas.html')

# Controladores de proveedores
@secureRoute
def proveedores():
    return render_template('dashboard/proveedores.html')

# Controladores de gestión de usuarios
@secureRoute
def usuariosGestion():
    return render_template('dashboard/usuariosGestion.html', users=user.getUsers())

@secureRoute
def promote(userID):
    if user.promoteUser(userID):
        flash('Usuario promovido', category='info')
    else:
        flash(f'Error al promover usuario con ID: {userID}', category='error')
    
    return redirect(url_for('usuariosGestion'))

@secureRoute
def demote(userID):
    if user.demoteUser(userID):
        flash('Usuario bajado', category='info')
    else:
        flash(f'Error al bajar usuario con ID:{userID}', category='error')
    
    return redirect(url_for('usuariosGestion'))

@secureRoute
def deleteUser(userID):
    if user.deleteUser(userID):
        flash('Usuario eliminado', category='info')
    else:
        flash(f'Error al eliminar usuario con ID:{userID}', category='error')
    
    return redirect(url_for('usuariosGestion'))

@secureRoute
def getRecentPurchases(userID):
    return jsonify(products.getRecentlyPurchased(userID))

# Controladores de gestión de productos
def agregarProducto():
    name = request.form['name']
    price = request.form['price']
    category = request.form['category']
    provider = request.form['provider']
    image = request.files['image']
    
    if not name or not price or not category or not provider or not image:
        return flash('Faltan campos', category='error')
    
    if not image.filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return flash('Formato de imagen no soportado', category='error')
    
    if products.addProduct(name, price, category, image.filename):
        image.save(f'static/img/products/{image.filename}')
        flash('Producto agregado', category='info')
    else:
        flash('Error al agregar producto', category='error')

@secureRoute
def productosGestion():
    if request.method == 'POST':
        agregarProducto()
    print(products.getProducts())
    return render_template('dashboard/productosGestion.html', 
                            products=products.getProducts(), 
                            categories=products.getCategories())

# Controladores de promociones
@secureRoute
def promociones():
    return render_template('dashboard/promociones.html')