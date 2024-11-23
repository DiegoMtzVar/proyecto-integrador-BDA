from flask import render_template
from models.analytics import getUsers

def dashboard():
    return render_template('dashboard/dashboard.html')

def historialComprasProveedor():
    return render_template('dashboard/historialComprasProveedor.html')


def usuariosGestion():
    users = getUsers()
    
    return render_template('dashboard/usuariosGestion.html', users=users)

def productosGestion():
    return render_template('dashboard/productosGestion.html')

def promociones():
    return render_template('dashboard/promociones.html')

