from flask_classic import app
from flask_classic.models import *
from flask import render_template,request,redirect,flash
import requests
from config import APIKEY
from datetime import date,datetime

from flask_classic.registroFormulario import RegistroFormulario

@app.route("/")
def listaMovimientos():
    datos = select_all()
    return render_template("listaMovimientos.html", datos= datos)

@app.route("/purchase", methods=["GET","POST"])
def registroMovimientos():
    form = RegistroFormulario()
    
    if request.method == "GET":
        return render_template("registroMovimientos.html", dataForm = form)
    else:
        if form.validate_on_submit():
            insert([form.date.data.isoformat(),
                form.time,
                form.moneda_from.data,
                form.cantidad_from.data,
                form.moneda_to.data,
                form.cantidad_to.data
                ])#aqui llamo a la funcion para registro
            
            flash("Movimiento registrado correctamente!!!")
            return redirect("/")
        else:
            return render_template("registroMovimientos.html",dataForm=form)
    

@app.route("/status")
def estadoInversion():
    return render_template("estadoInversion.html")
