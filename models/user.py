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
        if cur: cur.close()

def registerUser(name, email, password):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('registrarUsuario', (name, password, email))
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        if cur: cur.close()

def getUsers():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerUsuarios')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def promoteUser(userID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('promocionarUsuario', (userID,))
        
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        if cur: cur.close()
        
def demoteUser(userID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('bajarUsuario', (userID,))
        
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        if cur: cur.close()

def deleteUser(userID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('eliminarUsuario', (userID,))
        
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        if cur: cur.close()