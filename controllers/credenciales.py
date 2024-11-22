from flask import request, flash, redirect, url_for, session
from models.user import getUserID, registerUser

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        id = getUserID(email, password)
        
        if id:
            session['user'] = id
            flash('Has iniciado sesión', 'info')
            return redirect(url_for('landing'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
        
    return 'Welcome to the login page!'

def signup():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        
        if registerUser(name, email, password):
            flash('Usuario registrado', 'info')
            return redirect(url_for('login'))
        else:
            flash('Error al registrar usuario', 'error')
        
    return 'Welcome to the registro page!'

def logout():
    session.pop('user', None)
    flash('Has salido de sesión', 'info')
    return url_for('landing')