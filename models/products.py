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

def getResenas(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerResenas', (id,))
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getUserPurchases(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerVentasUsuario', (id,))
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getCategories():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerCategorias')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def addProduct(name, price, category, image):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('agregarProducto', (name, price, category, image))
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        if cur: cur.close()

def aniadirCompra(idU,direccion,entrega):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('aniadirCompra', (idU, direccion, entrega))
        result = cur.fetchall()
        id = result[0]["ID"] if result else None
        mysql.connection.commit()
        return id
    except Exception as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")
    finally:
        if cur: cur.close()
    return False

def ultimaCompra(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('ultimaCompra', (id,))
        data = cur.fetchall()
        return data[0]["ID"] if data else None
    except:
        return []
    finally:
        if cur: cur.close()


def aniadirContiene(idU,idC,cantidad):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('aniadirContiene', (idU,idC,cantidad))
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")
    finally:
        if cur: cur.close()
    return False

def getSales():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerVentas')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()