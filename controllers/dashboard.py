from flask import render_template

def dashboard():
    return render_template('dashboard/dashboard.html')

def historialComprasProveedor():
    return render_template('dashboard/historialComprasProveedor.html')

def usuariosGestion():
    return render_template('dashboard/usuariosGestion.html')

def productosGestion():
    return render_template('dashboard/productosGestion.html')

def promociones():
    return render_template('dashboard/promociones.html')