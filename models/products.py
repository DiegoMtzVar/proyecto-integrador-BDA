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

def addProduct(name, price, category, image, supplier):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('crearProducto', (name, price, category, image, supplier))
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")
        return False
    finally:
        if cur: cur.close()

def aniadirCompra(idU,direccion,entrega,total):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('aniadirCompra', (idU, direccion, entrega,total))
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


def aniadirContiene(idU,idC,cantidad,promocion):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('aniadirContiene', (idU,idC,cantidad,promocion))
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")
    finally:
        if cur: cur.close()
    return False

def getCoupons():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerCupones')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getCuponesbyID(cupon):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerCuponesbyID', (cupon,))
        
        data = cur.fetchone() if cur else False
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def addCoupon(name, discount):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('crearCupon', (name, discount))
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        if cur: cur.close()

def updateCoupon(couponID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('actualizarCupon', (couponID,))
        
        mysql.connection.commit()
        return True
    except Exception as e:
        return e
    finally:
        if cur: cur.close()


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

def updateSaleStatus(ventaID, statusID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('actualizarEstadoVenta', (ventaID, statusID))
        mysql.connection.commit()
        return True
    except:
        return False
    finally:
        if cur: cur.close()

def getSupplierPurchases():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('comprasProveedores')
        
        data = cur.fetchall()
        
        return data
    except Exception:
        return []
    finally:
        if cur: cur.close()

def getProductsInPurchase(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosEnCompra', (id,))
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getProductsBySupplier(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosProveedor', (id,))
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getSuppliers():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerProveedores')
        
        data = cur.fetchall()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def addPurchase(supplierID):
    try:
        cur = mysql.connection.cursor()
        
        cur.callproc('crearCompra', (supplierID,))
        
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")
        return False
    finally:
        if cur: cur.close()

def getRecentPurchase(supplierID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('obtenerUltimaCompra', (supplierID,))
        data = cur.fetchone()
        return data["ID"]
    except:
        return []
    finally:
        if cur: cur.close()

def addPurchaseProduct(purchaseID, productID, quantity):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('agregarProductoCompra', (purchaseID, productID, quantity))
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error al ejecutar agregarProductoCompra: {e}")
        return False
    finally:
        if cur: cur.close()

def addSupplier(name, email, phone, address):
    try:
        print(name, email, phone, address)
        cur = mysql.connection.cursor()
        cur.callproc('crearProveedor', (name, phone, email, address))
        mysql.connection.commit()
        return True
    except Exception as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")
        return False
    finally:
        if cur: cur.close()