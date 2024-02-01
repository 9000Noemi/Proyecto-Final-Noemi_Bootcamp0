import sqlite3
from flask_classic import ORIGIN_DATA
from flask_classic.db_conexion import Conexion

def insert(registroForm):
    conectarInsert = Conexion("insert into Movimientos(date,time,moneda_from,cantidad_from,moneda_to,cantidad_to) values(?,?,?,?,?,?);",registroForm)
    conectarInsert.con.commit()#funcion para validar el registro
    conectarInsert.con.close()

def select_all():

    conectar = Conexion("select * from Movimientos order by date ASC;")

    filas = conectar.res.fetchall()#este trae los datos que hay en la tabla
    columnas = conectar.res.description#este trae los titulos de las columnas

    lista_diccionario =[]  #creamos una lista vacía para recorrer la tabla con un for e ir cargando los datos
 
    for fila in filas:
        posicion=0
        diccionario ={} #creamos un dicc vacío
        for columna in columnas:
            diccionario[columna[0]] = fila[posicion] #los titulos de columnas siempre estan en posicion 0
            posicion +=1
       
        lista_diccionario.append(diccionario) 
    conectar.con.close() #Esto está bien????????????
    
    return lista_diccionario   

