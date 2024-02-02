from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField,SelectField #creo q no necesito datefield xq no uso fechas
from wtforms.validators import DataRequired, InputRequired, ValidationError
from flask_classic.models import *
import requests
from config import APIKEY

class RegistroFormulario(FlaskForm):
    moneda_from =SelectField(choices=["EUR","BTC","ETH","USDT","BNB", "XRP","ADA","SOL","DOT","MATIC"])
    moneda_to= SelectField(choices=["EUR","BTC","ETH","USDT","BNB", "XRP","ADA","SOL","DOT","MATIC"])
    cantidad= FloatField ('Cantidad: ', validators=[DataRequired(message= "Indica una cantidad.")])
    boton_calculo= SubmitField('Calcular')
    tasa_cambio= FloatField ('Tasa de cambio: ')
    precio_unitario= FloatField ('Precio unitario: ')
    submit= SubmitField('Ejecutar operación')
       
        #lista_general = r
        #precio_unitario = lista_general['rate'] * cantidad_from 
        #response = [lista_general["rate"], precio_unitario]
        #return response

    #calcular= SubmitField('Calculate', calcular_cambio(moneda_from="moneda-from", moneda_to="moneda_to", cantidad_from="cantidad_from"))
    #submit= SubmitField('Guardar')
