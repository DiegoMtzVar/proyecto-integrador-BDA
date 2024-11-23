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