from flask import Flask, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
from controllers.credenciales import login, signup, logout

app = Flask(__name__)

app.config['MYSQL_HOST'] = '34.27.155.252'
app.config['MYSQL_USER'] = 'todos'
app.config['MYSQL_PASSWORD'] = 'bda'
app.config['MYSQL_DB'] = 'SkateMotion'

mysql = MySQL(app)

def landing():
    return 'Welcome to the landing page!'

app.add_url_rule('/', 'landing', landing)
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/signup', 'signup', signup, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET'])
app.add_url_rule('/productos', 'productos')