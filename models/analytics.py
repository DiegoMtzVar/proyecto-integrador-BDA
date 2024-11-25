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

def mostBought():
    try:
        cur = mysql.connection.cursor()
        cur.callproc('masComprados')
        data = cur.fetchall()
        return jsonify(data)
    except:
        return []
    finally:
        if cur: cur.close()