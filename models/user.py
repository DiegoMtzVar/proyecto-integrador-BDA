from database import mysql

def getUserID(email, password):
    cur = mysql.connection.cursor()
    cur.callProc('loginUsuario', (email, password))
    id = cur.fetchall()[0][0]
    return id

def registerUser(name, email, password):
    cur = mysql.connection.cursor()
    try:
        cur.callProc('registrarUsuario', (name, password, email))
        mysql.connection.commit()
        return True
    except:
        return False