from flask_mysqldb import MySQL

mysql = MySQL()

def initDB(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'todos'
    app.config['MYSQL_PASSWORD'] = 'bda'
    app.config['MYSQL_DB'] = 'SkateMotion'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    
    mysql.init_app(app)