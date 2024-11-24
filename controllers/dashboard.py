from flask import render_template, session, flash, url_for, redirect, jsonify
from models import analytics, user
from models.products import getRecommendedProducts, getRecentlyPurchased, getProductsByCategory, getProductById
from functools import wraps

def secureRoute(route):
    @wraps(route)
    def wrapped_route(*args, **kwargs):
        if not session.get('user') or not session['user']['role'] == 'administrador':
            flash('Debes iniciar sesión para acceder a esta página', category='error')
            return redirect(url_for('login'))
        return route(*args, **kwargs)
    return wrapped_route

@secureRoute
def dashboard():
    return render_template('dashboard/dashboard.html')

@secureRoute
def historialVentas():
    return render_template('dashboard/historialVentas.html')

@secureRoute
def historialComprasProveedor():
    return render_template('dashboard/historialComprasProveedor.html')

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
    return jsonify(getRecentlyPurchased(userID))

@secureRoute
def productosGestion():
    return render_template('dashboard/productosGestion.html')

@secureRoute
def promociones():
    return render_template('dashboard/promociones.html')


