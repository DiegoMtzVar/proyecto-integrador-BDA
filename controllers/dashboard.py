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
    print(analytics.getMonthIn())
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

# Controladores de ventas
@secureRoute
def ventas():
    return render_template('dashboard/ventas.html', sales=products.getSales())

def updateStatus(ventaID, statusID):
    if products.updateSaleStatus(ventaID, statusID):
        flash('Venta actualizada', category='info')
    else:
        flash(f'Error al actualizar venta con ID: {ventaID}', category='error')
    
    return redirect(url_for('ventas'))

# Controladores de proveedores
@secureRoute
def proveedores():
    if request.method == 'POST':
        supplierID = request.form.get("proveedor")
        
        purchaseAdded = products.addPurchase(supplierID)
        if purchaseAdded:
            purchaseID = products.getRecentPurchase(supplierID)
            for i in range(len(request.form.getlist("producto"))):
                product_id = int(request.form.getlist("producto")[i])
                quantity = int(request.form.getlist("cantidad")[i])
                
                if not products.addPurchaseProduct(purchaseID, product_id, quantity):
                    flash('Error al crear compra', category='error')
                    return redirect(url_for('proveedores'))
                
            flash('Compra creada', category='info')
        else:
            flash('Error al crear compra', category='error')
            
    return render_template('dashboard/proveedores.html', 
                           purchases=products.getSupplierPurchases(), 
                           suppliers=products.getSuppliers())

@secureRoute
def getProductsInPurchase(userID):
    return jsonify(products.getProductsInPurchase(userID))

@secureRoute
def getProductsBySupplier(supplierID):
    return jsonify(products.getProductsBySupplier(supplierID))

@secureRoute
def createSupplier():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    
    if not name or not email or not phone or not address:
        return flash('Faltan campos', category='error')
    
    if products.addSupplier(name, email, phone, address):
        flash('Proveedor agregado', category='info')
    else:
        flash('Error al agregar proveedor', category='error')
        
    return redirect(url_for('proveedores'))

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
        flash(f'Error al bajar usuario con ID: {userID}', category='error')
    
    return redirect(url_for('usuariosGestion'))

@secureRoute
def deleteUser(userID):
    result = user.deleteUser(userID)
    if result == True:
        flash('Usuario eliminado', category='info')
    else:
        flash(f'Error al eliminar usuario con ID: {userID} \n {result}', category='error')
    
    return redirect(url_for('usuariosGestion'))

@secureRoute
def getRecentPurchases(userID):
    return jsonify(products.getUserPurchases(userID))

# Controladores de gestión de productos
def crearProducto():
    name = request.form['name']
    price = request.form['price']
    category = request.form['category']
    image = request.files['image']
    supplier = request.form['supplier']
    
    if not name or not price or not category or not image or not supplier:
        return flash('Faltan campos', category='error')
    
    if not image.filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return flash('Formato de imagen no soportado', category='error')
    
    if products.addProduct(name, price, category, image.filename, supplier):
        image.save(f'static/img/products/{image.filename}')
        flash('Producto agregado', category='info')
    else:
        flash('Error al agregar producto', category='error')

@secureRoute
def productosGestion():
    if request.method == 'POST':
        crearProducto()
    return render_template('dashboard/productosGestion.html', 
                            products=products.getProducts(), 
                            categories=products.getCategories(),
                            suppliers=products.getSuppliers())

# Controladores de promociones
def createPromotion():
    if request.method == 'POST':
        name = request.form['name']
        discount = request.form['discount']
        if not name or not discount:
            return flash('Faltan campos', category='error')
        if products.addCoupon(name, discount):
            flash('Promoción creada', category='info')
        else:
            flash('Error al crear promoción', category='error')
    return redirect(url_for('promociones'))

@secureRoute
def promociones():
    if request.method == 'POST':
        createPromotion()
    print(products.getCoupons())
    return render_template('dashboard/promociones.html', coupons=products.getCoupons())


@secureRoute
def updateCoupon(promoCode):
    result = products.updateCoupon(promoCode)
    if result == True:
        flash('Promoción actualizada', category='info')
    else:
        flash(f'Error al actualizar promoción {promoCode} \n {result}', category='error')
    
    return redirect(url_for('promociones'))
