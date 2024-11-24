from flask import render_template, session, flash, url_for, redirect, jsonify
from models.analytics import getUsers, promoteUser, demoteUser
from models.products import getRecommendedProducts, getRecentlyPurchased, getProductsByCategory, getProductById

def verifyAdmin():
    if session.get('user') and session['user']['role'] == 'admin':
        return True
    else:
        flash('No tienes permisos para acceder a esta página', category='error')
        return redirect(url_for('index'))

def dashboard():
    if not verifyAdmin(): return False
    return render_template('dashboard/dashboard.html')

def historialVentas():
    return render_template('dashboard/historialVentas.html')

def historialComprasProveedor():
    return render_template('dashboard/historialComprasProveedor.html')

def usuariosGestion():
    if not verifyAdmin(): return False
    return render_template('dashboard/usuariosGestion.html', users=getUsers())


def promote(userID):
    if not verifyAdmin(): return False
    if promoteUser(userID):
        flash('Usuario promovido', category='info')
    else:
        flash('Error al promover usuario', category='error')
    
    return usuariosGestion()

def demote(userID):
    if not verifyAdmin(): return False
    if demoteUser(userID):
        flash('Usuario bajado', category='info')
    else:
        flash('Error al degradar usuario', category='error')
    
    return usuariosGestion()

def getRecentPurchases(userID):
    if not verifyAdmin(): return False
    return jsonify(getRecentlyPurchased(userID))

def productosGestion():
    return render_template('dashboard/productosGestion.html')

def promociones():
    return render_template('dashboard/promociones.html')


