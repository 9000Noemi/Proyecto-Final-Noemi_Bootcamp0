from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField #creo q no necesito datefield xq no uso fechas
from wtforms.validators import DataRequired, InputRequired, ValidationError
from flask_classic.models import *
import requests
from config import APIKEY

class RegistroFormulario(FlaskForm):
    moneda_from = StringField ('Moneda from: ', validators=[DataRequired(message="Selecciona una moneda." )])
    moneda_to= StringField ('Moneda to: ', validators=[DataRequired(message="Selecciona una moneda.")])
    cantidad= FloatField ('Cantidad: ', validators=[DataRequired(message= "Indica una cantidad.")])
    submit= SubmitField('Calcular')
    tasa_cambio= FloatField ('Tasa de cambio: ', validators=[DataRequired()])
    precio_unitario= FloatField ('Precio unitario: ', validators=[DataRequired()])
    submit= SubmitField('Ejecutar operación')

    listaDatos=select_all()
    lista= []

    coin_from = "EUR"
    coin_to = "BTC"
    
    def validate_moneda_from(listaDatos, form, field, lista):
        for dicLista in listaDatos:
            moneda = dicLista.get("moneda_from")
            lista.append(moneda)
        
        for moneda in lista:
            if(moneda != field):
                raise ValidationError('No dispones de esta moneda para comprar.') 

    def calcular_cambio(moneda_from, moneda_to, cantidad_from):
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
        lista_general = r.json()
        
        
        
        #lista_general = r
        #precio_unitario = lista_general['rate'] * cantidad_from 
        #response = [lista_general["rate"], precio_unitario]
        #return response

    #calcular= SubmitField('Calculate', calcular_cambio(moneda_from="moneda-from", moneda_to="moneda_to", cantidad_from="cantidad_from"))
    #submit= SubmitField('Guardar')
