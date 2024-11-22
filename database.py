from flask_mysqldb import MySQL

mysql = MySQL()

def initDB(app):
    app.config['MYSQL_HOST'] = '35.188.177.160'
    app.config['MYSQL_USER'] = 'todos'
    app.config['MYSQL_PASSWORD'] = 'bda'
    app.config['MYSQL_DB'] = 'SkateMotion'
    
    mysql.init_app(app)