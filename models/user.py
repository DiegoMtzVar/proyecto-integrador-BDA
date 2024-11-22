from database import mysql

def getUser(email, password):
    cur = mysql.connection.cursor()
    cur.callproc('loginUsuario', (email, password))
    id = cur.fetchall()[0][0]
    return id

def registerUser(name, email, password):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('registrarUsuario', (name, password, email))
        mysql.connection.commit()
        return True
    except:
        return False