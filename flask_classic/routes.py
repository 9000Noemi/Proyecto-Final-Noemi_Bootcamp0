from flask_classic import app
from flask_classic.models import *
from flask import render_template,request,redirect,flash
import requests
from config import APIKEY

#from flask_classic.registroFormulario import RegistroFormulario

@app.route("/")
def listaMovimientos():
    datos = select_all()
    return render_template("listaMovimientos.html", datos= datos)

@app.route("/purchase")#, methods=["GET","POST"])
def registroMovimientos():
    #form = RegistroFormulario()
    
    coin_from = "EUR"
    coin_to = "BTC"
    url = f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?apikey={APIKEY}"
    r = requests.get(url)

    lista_general = r.json()

    #if request.method == "GET":
    return render_template("registroMovimientos.html", dataForm = lista_general)
    #else:
        #if form.validate_on_submit():
            #insert([form.date.data.isoformat(),
                #form.concept.data,
                #form.quantity.data
                #])#aqui llamo a la funcion para registro
            
            #flash("Movimiento registrado correctamente!!!")
            #return redirect("/")
        #else:
            #return render_template("registroMovimientos.html",dataForm=form)
    

    