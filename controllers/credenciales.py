from flask import request, flash, redirect, url_for, session, render_template
from models.user import getUser, registerUser

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = getUser(email, password)
        
        if user:
            session['user'] = user
            flash('Has iniciado sesión', 'info')
            return redirect(url_for('landing'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
        
    return render_template('login.html')

def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        
        if registerUser(name, email, password):
            flash('Usuario registrado', 'info')
            return redirect(url_for('login'))
        else:
            flash('Error al registrar usuario', 'error')
        
    return render_template('register.html')

def logout():
    session.pop('user', None)
    flash('Has salido de sesión', 'info')
    return url_for('landing')