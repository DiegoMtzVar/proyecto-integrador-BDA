from database import mysql

def getRecommendedProducts():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosRecomendados')
        
        data = cur.fetchall()
        return data
    except Exception as e:
        print(e)
        return []

def getRecentlyPurchased(userID):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosRecientes', (userID,))
        
        data = cur.fetchall()
        return data
    except:
        return []

def getProductsByCategory(type):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productosPorCategoria', (type,))
        
        data = cur.fetchall()
        return data
    except:
        return []

def getProductById(id):
    try:
        cur = mysql.connection.cursor()
        cur.callproc('productoPorID', (id,))
        
        data = cur.fetchone()
        return data
    except:
        return False

