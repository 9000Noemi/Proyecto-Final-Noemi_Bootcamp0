import sqlite3
from flask_classic import ORIGIN_DATA
from flask_classic.db_conexion import Conexion

def insert(registroForm):
    conectarInsert = Conexion("insert into movements(date,concept,quantity) values(?,?,?);",registroForm)
    conectarInsert.con.commit()#funcion para validar el registro
    conectarInsert.con.close()

def select_all():

    conectar = Conexion("select * from Movimientos order by date ASC;")

    filas = conectar.res.fetchall()#datos de columnas (2024-01-01,Nomina Enero,1500)
    columnas = conectar.res.description#nombres de columnas(id,000000)(date,0000)(concep)

    lista_diccionario =[]
 
    for fila in filas:
        posicion=0
        diccionario ={}
        for columna in columnas:
            diccionario[columna[0]] = fila[posicion]
            posicion +=1
        print(diccionario)
        lista_diccionario.append(diccionario) 
    conectar.con.close()
    
    print(lista_diccionario)
    return lista_diccionario   

