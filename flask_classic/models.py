from flask_classic.db_conexion import Conexion

def insert(registroForm):
    conectarInsert = Conexion("insert into Movimientos(date,time,moneda_from,cantidad_from,moneda_to,cantidad_to) values(?,?,?,?,?,?);",registroForm)
    conectarInsert.con.commit()
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
    conectar.con.close() 
    
    return lista_diccionario   

#COMPROBAMOS SI TENEMOS SUFICIENTE SALDO DE UNA MONEDA - Llamada a la BD y suma:
def coin_sum(moneda_to):

    resultado = ""
    #Comporbamos el saldo de una criptomoneda:
    #  1. Sumamos todas las cantidades_to en filas cuya moneda_to es la criptomoneda buscada
    conectar = Conexion("SELECT SUM(cantidad_to) FROM Movimientos WHERE moneda_to=?", (moneda_to,))
    resultado_to = conectar.res.fetchall()
    conectar.con.close()

    #Si hay datos en resultado_to significa que tenemos saldo y por tanto hacemos la siguiente operación
    if(''.join(map(str,resultado_to[0])) != 'None'):
        #  2. Sumamos todas la cantidades_from en filas cuya moneda_from es la criptomoneda buscada para restar si nos hemos gastado algo(más adelante)
        conectar = Conexion("SELECT SUM(cantidad_from) FROM Movimientos WHERE moneda_from=?", (moneda_to,))
        resultado_from = conectar.res.fetchall()
        conectar.con.close()
        
        if (''.join(map(str,resultado_from[0])) != 'None'):
            #  3. El saldo es la resta (1 - 2)
            #Transformamos los datos de la BD en str y luego en float para evitar el type error de la tupla: float(''.join(map(str, xxx)))
            resultado = float(''.join(map(str,resultado_to[0]))) - float(''.join(map(str,resultado_from[0])))
        else:
            resultado = float(''.join(map(str,resultado_to[0]))) 

    else:
        #Si no hay datos devolvemos 0 en resultado_to
        resultado = 0    

    return resultado
    
def total_invertido(moneda_from):
    conectar = Conexion("SELECT SUM (cantidad_from) FROM Movimientos WHERE moneda_from =?", (moneda_from,))
    resultado_bd = conectar.res.fetchall()
    conectar.con.close()

    if (''.join(map(str,resultado_bd[0])) != 'None'):
        resultado = float(''.join(map(str,resultado_bd[0])))
    else:
        resultado = 0

    return resultado

def total_obtenido(moneda_to):
    conectar = Conexion("SELECT SUM (cantidad_to) FROM Movimientos WHERE moneda_to = ?", (moneda_to,))
    resultado_bd = conectar.res.fetchall()
    conectar.con.close()
   
    if (''.join(map(str,resultado_bd[0])) != 'None'):
        resultado = float(''.join(map(str,resultado_bd[0])))
    else:
        resultado = 0
    
    return resultado


def total_monedas():
    conectar = Conexion("SELECT (moneda_to) FROM Movimientos")
    resultado = conectar.res.fetchall()
    conectar.con.close()

    lista = []

    for elemento in resultado:
        lista.append(elemento[0])

    return lista




