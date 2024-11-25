from flask_mysqldb import MySQL

mysql = MySQL()

def initDB(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'skatemotion'
    app.config['MYSQL_PASSWORD'] = 'skatemotion'
    app.config['MYSQL_DB'] = 'SkateMotion'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    
    mysql.init_app(app)