from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired, InputRequired, ValidationError
from flask_classic.models import *

class RegistroFormulario(FlaskForm):

    listaDatos=select_all()
    lista= []

    for dicLista in listaDatos:
        moneda = dicLista.get("moneda_from")
        lista.append(moneda)
    print(lista)

    def validate_moneda_from(form, field, lista):
            for moneda in lista:
                if(moneda != field):
                    raise ValidationError('No dispones de esta moneda para comprar.')           

    moneda_from = StringField("Moneda_from",[InputRequired(), validate_moneda_from])
    print(moneda_from)
    #cantidad_from = ""
    #moneda_to = ""
    #cantidad_to = ""

    
    submit= SubmitField('Guardar')
