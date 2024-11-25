from flask import request, flash, redirect, url_for, session, render_template, jsonify
from models.user import getUser, registerUser
from hashlib import sha256

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = sha256(password.encode()).hexdigest()
        user = getUser(email, hashed_password)
        
        if user:
            session['user'] = user
            #flash('Has iniciado sesión', category='success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', category='error')
    return render_template('credentials/login.html')

def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        
        hashed_password = sha256(password.encode()).hexdigest()
        if registerUser(name, email, hashed_password):
            flash('Usuario registrado', 'info')
            return redirect(url_for('login'))
        else:
            flash('Ya existe esta registrado este correo, intente de nuevo', category='error')
        
    return render_template('credentials/register.html')

def logout():
    session.clear()
    #flash('Has salido de sesión', category='info')
    return redirect(url_for('index'))

def userAPI():
    if session.get('user'):
        return jsonify(session['user'])
    else:
        return jsonify({'error': 'No hay sesión activa'})