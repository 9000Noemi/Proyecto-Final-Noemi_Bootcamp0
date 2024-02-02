from flask_classic import app
from flask_classic.models import *
from flask import render_template,request,redirect,flash
import requests
from config import APIKEY
from datetime import date, datetime



from flask_classic.registroFormulario import RegistroFormulario

'''
def validate_moneda_from(moneda_to, form):
    get_moneda = coin_sum(moneda_to)
    if get_moneda<=0:
        raise ValidationError('No dispones de esta moneda para comprar.') 
         
def validate_cantidad_from(cantidad_to,form):
    get_cantidad = coin_sum
'''
def calcular_cambio(moneda_from, moneda_to):
    url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_from}/{moneda_to}?apikey={APIKEY}"
    r = requests.get(url)
    '''
    r={
    "time": "2024-01-30T18:53:45.0000000Z",
    "asset_id_base": "BTC",
    "asset_id_quote": "EUR",
    "rate": 2.48
    }
    '''
    lista_api = r.json()
    return lista_api["rate"]

@app.route("/")
def listaMovimientos():
    todos = select_all()
    return render_template("listaMovimientos.html", datos= todos)

@app.route("/purchase", methods=["GET","POST"])
def registroMovimientos():
    form = RegistroFormulario()
    consulta_api = 0

    #Si es POST cargamos la plantilla html con la información básica que es el form y la que vayamos añadiendo cuando pulsamos los botones
    if request.method == "POST":
        #Si pulsamos Calcular consulta a la api y añade a la plantilla el resultado de las variables
        if form.boton_calculo.data:
            consulta_api = calcular_cambio(form.moneda_from.data, form.moneda_to.data)
            rate_formateada = "{:.10f}".format(consulta_api)
            cantidad_cambio = consulta_api * form.cantidad.data
            cantidad_formateada = "{:.10f}".format(cantidad_cambio)
    
        #Si pulsamos ejecutar guardamos los datos que tenemos en los inputs del formulario en la base de datos
        elif form.submit.data:
            print("BOTON")
            test = insert([
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
        return render_template("registroMovimientos.html", dataForm = form, resultado_api = rate_formateada, precio_cantidad = cantidad_formateada )

    else:
        #si es solo GET cargamos la plantilla con el formulario vacío
        return render_template("registroMovimientos.html",dataForm=form)

@app.route("/status")
def estadoInversion():
    return render_template("estadoInversion.html")
