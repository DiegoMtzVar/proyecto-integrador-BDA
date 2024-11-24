from database import mysql

def getUsers():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerUsuarios')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        cur.close()

def promoteUser():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('promocionarUsuario')
        
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        cur.close()
        
def demoteUser():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('bajarUsuario')
        
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        cur.close()
    