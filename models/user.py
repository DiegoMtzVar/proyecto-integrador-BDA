from database import mysql

def getUser(email, password):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('loginUsuario', (email, password))
        
        data = cur.fetchone()
        return data
    except:
        return False
    finally:
        cur.close()

def registerUser(name, email, password):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('registrarUsuario', (name, password, email))
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        cur.close()