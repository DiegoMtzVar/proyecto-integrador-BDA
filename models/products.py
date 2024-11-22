from database import mysql

def getRecommendedProducts():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosRecomendados')
        
        data = cur.fetchall()
        return data
    except:
        return []

def getRecentlyPurchased(userID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosRecientes', (userID,))
        
        data = cur.fetchall()
        return data
    except:
        return []

def getProductsByType(type):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosPorTipo', (type,))
        
        data = cur.fetchall()
        return data
    except:
        return []

def getProductById(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productoPorId', (id,))
        
        data = cur.fetchone()
        return data
    except:
        return False