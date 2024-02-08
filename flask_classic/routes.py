from wtforms import ValidationError
from flask_classic import app
from flask_classic.models import *
from flask import render_template,request,redirect,flash, url_for
import requests
from config import APIKEY
from datetime import date, datetime

from flask_classic.registroFormulario import RegistroFormulario


def validate_moneda_from(moneda_from, cantidad):
    errores = []
    
    #Calculamos la cantidad de dinero que tenemos disponible para tradear de la moneda_from (llamada a la BD en coin_sum)
    get_moneda = coin_sum(moneda_from)

    #Para evitar un error en caso de no tener X moneda:
    if get_moneda == 0:
        errores.append ('No dispone de esta moneda.') 

    # En caso de no disponer de suficiente saldo, mostrar un error:
        
    elif get_moneda<cantidad:
        errores.append ('No tiene suficiente saldo de esta moneda.') 
    
    return errores
    
    

def calcular_cambio(moneda_from, moneda_to):
    url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_from}/{moneda_to}?apikey={APIKEY}"
    r = requests.get(url)
    lista_api = r.json()
    return lista_api["rate"]


@app.route("/")
def listaMovimientos():
    todos = select_all()
    return render_template("listaMovimientos.html", datos= todos, active_page="listaMovimientos")

@app.route("/purchase", methods=["GET","POST"])
def registroMovimientos():
    form = RegistroFormulario()
    consulta_api = 0 
    validate = []
    #Si es POST cargamos la plantilla html con la información básica que es el form y la que vayamos añadiendo cuando pulsamos los botones
    if request.method == "POST":
        #Si pulsamos Calcular consulta a la api y añade a la plantilla el resultado de las variables
        if form.boton_calculo.data:
            #Para tener euros ilimitados sacamos los euros de la validación:
            if form.moneda_from.data != "EUR":
                validate = validate_moneda_from(form.moneda_from.data, form.cantidad.data)
            if validate:
                return render_template("registroMovimientos.html",dataForm=form, active_page="registroMovimientos",errors=validate)

            consulta_api = calcular_cambio(form.moneda_from.data, form.moneda_to.data)
            rate_formateada = "{:.10f}".format(consulta_api)
            cantidad_cambio = consulta_api * form.cantidad.data
            cantidad_formateada = "{:.10f}".format(cantidad_cambio)
    
        #Si pulsamos ejecutar guardamos los datos que tenemos en los inputs del formulario en la base de datos
        elif form.submit.data:
            insert([
                date.today(),
                datetime.now(),
                form.moneda_from.data,
                form.cantidad.data,
                form.moneda_to.data,
                form.precio_unitario.data
                ])
            
            flash("Movimiento registrado")
            return redirect("/")
        
        #Aquí cargamos la plantilla
        return render_template("registroMovimientos.html", dataForm = form, lista_errores=validate, resultado_api = rate_formateada, precio_cantidad = cantidad_formateada, active_page="registroMovimientos")

    else:
        #si es solo GET cargamos la plantilla con el formulario vacío
        return render_template("registroMovimientos.html",dataForm=form, active_page="registroMovimientos")

@app.route("/status")
def estadoInversion():
    lista_cryptos = []
    
    invertido = total_invertido ('EUR')
    recuperado =  total_obtenido ('EUR')
    
    valor_compra = invertido - recuperado

    #Consulta a la base de datos para saber cuántos tipos de monedas tenemos:
    monedas = total_monedas()

    #Recorremos la lista monedas para quitar los euros y cargar las cryptos en una nueva lista (lista_cryptos):
    for moneda in monedas: 
        if moneda != 'EUR':
            lista_cryptos.append(moneda)

    #Quitamos los duplicados de las cryptos:
    lista_cryptos = list(dict.fromkeys(lista_cryptos))
    total_valor_actual = []
        
    #Recorremos la lista de monedas para sacar el valor actual en euros de cada una:
    for crypto in lista_cryptos:
        valor_diferencia = total_obtenido(crypto) - total_invertido(crypto)
        valor_actual = calcular_cambio(crypto, "EUR") #Llamada a la API para sacar el rate
        print(valor_actual)
        #Hacemos una nueva lista con el valor en euros de cada crypto:
        total_valor_actual.append(valor_diferencia*valor_actual)
            
        # Sumamos todos los elementos de la lista para obtener el total en euros de todas las crypto: 
        
        return render_template("estadoInversion.html", dataInvertido="{:.2f}".format(invertido), dataRecuperado="{:.2f}".format(recuperado), dataValorCompra="{:.2f}".format(valor_compra), dataTotalValorActual="{:.2f}".format(sum(total_valor_actual)),active_page="estadoInversion")
    
    
