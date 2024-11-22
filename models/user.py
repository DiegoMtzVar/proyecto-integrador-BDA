from database import mysql

def getUser(email, password):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('loginUsuario', (email, password))
        
        data = cur.fetchall()
        return data.idUsuario
    except:
        return False

def registerUser(name, email, password):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('registrarUsuario', (name, password, email))
        mysql.connection.commit()
        return True
    except:
        return False