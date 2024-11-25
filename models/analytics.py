from database import mysql
from datetime import datetime
from flask import jsonify

def getTotalEarning():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('gananciasTotales')
        data = cur.fetchone()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def getMonthIn():
    try:
        tiempo = datetime.now()
        anio = tiempo.year
        mes = tiempo.month
        cur = mysql.connection.cursor()
        cur.callproc('ingresosMes', [mes, anio])
        data = cur.fetchone()
        return data
    except:
        return []
    finally:
        if cur: cur.close()
    
def getMonthOut():
    try:
        tiempo = datetime.now()
        anio = tiempo.year
        mes = tiempo.month
        cur = mysql.connection.cursor()
        cur.callproc('egresosMes', [mes, anio])
        data = cur.fetchone()
        return data
    except:
        return []
    finally:
        if cur: cur.close()

def mostSold():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('masVendidos')
        data = cur.fetchall()
        return jsonify(data)
    except:
        return []
    finally:
        if cur: cur.close()

def providerPercentage():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('porcentajeProveedor')
        data = cur.fetchall()
        return jsonify(data)
    except:
        return []
    finally:
        if cur: cur.close()

def totalMonthlySupplier():
    try:
        tiempo = datetime.now()
        anio = tiempo.year
        mes = tiempo.month
        cur = mysql.connection.cursor()
        cur.callproc('totalProveedorMes', [mes, anio])
        data = cur.fetchall()
        return jsonify(data)
    except:
        return []
    finally:
        if cur: cur.close()

def providerTotal():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('totalProveedor')
        data = cur.fetchall()
        return jsonify(data)
    except:
        return []
    finally:
        if cur: cur.close()