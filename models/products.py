from database import mysql

def getRecommendedProducts():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosRecomendados')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getRecentlyPurchased(userID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosRecientes', (userID,))
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getProductsByCategory(type):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosPorCategoria', (type,))
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getProductById(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productoPorID', (id,))
        
        data = cur.fetchone()
        return data
    except:
        return False
    finally:
        if cur: cur.close()

def aniadirResena(idU,idP,calificacion,comentario):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('aniadirResena', (idU,idP,calificacion,comentario))
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")
    finally:
        if cur: cur.close()
    return False

def getProducts():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerProductos')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()