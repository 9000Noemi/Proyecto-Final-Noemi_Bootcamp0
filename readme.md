<h1 align="center"> PROYECTO FINAL NOEMI MARTIN: CRIPTOPYN </h1>


### Programa hecho en Python con el framework Flask, base de datos SQLite y consulta a una API

***
#### Instalación:

- Obtener una apikey en https://docs.coinapi.io/ ingresando un correo electrónico para poder consultar el valor de las criptomonedas en  www.coinapi.io
- Guardamos la apikey en config.py de la siguiente manera: 
```
APIKEY = "AQUI VA SU APIKEY"
```

- Crear un entorno virtual de python con una de estas opciones:
```
py -m venv entorno
python -m venv entorno
python3 -m venv entorno
```

- Activar el entorno: 
```
En windows: .\entorno\Scripts\activate
En mac o linux: source entorno/bin/activate 
```


***
#### Librerías

- Obtener todas las librerías necesarías para la aplicación:
````
pip install -r requirements.txt
````
***
#### Base de datos
- Crear en SQLite la tabla Movimientos indicada en data/Movimientos_create.sql

***
#### Ejecución del programa

- Iniciar el servidor de flask 
```
En windows: set FLASK_APP=main.py
En mac: export FLASK_APP=main.py 
```
- Otra opción de ejecución es crear un archivo .env y agregar lo siguiente: 
```
FLASK_APP=main.py 
FLASK_DEBUG=True
```
- Tras esto podemos ejecutar en la terminal el siguiente comando: 
```
flask run
```

***
#### Características de la aplicación

Se trata de una aplicación en la cual el usuario puede comprar, vender y tradear con cryptomonedas.

Dispondrá de tres menús con diferentes funciones:
- **Menú "Inicio"**: en el cual se presenta la lista de movimientos realizados.

- **Menú "Compra"**: donde se podrán ejecutar las operaciones de compra, venta y tradeo. Se presentan dos desplegables (*moneda_from* y *moneda_to*) con las opciones de moneda y cryptomonedas con las que trabaja la aplicación, y un campo para indicar la cantidad que queremos comprar. Pulsando el botón *"Calcular"* nos indicará la tasa de cambio actual y el precio unitario, pudiendo realizar la transacción pulsando el botón *"Ejecutar operación"*.

- **Menú "Status"**: aquí el usuario podrá ver el estado de sus inversiones, a saber: el dinero invertido, el recuperado, el valor de la compra y el valor actual en euros de sus cryptomonedas.

***
#### Funcionalidades
- Todas las páginas tienen el mismo *header* y *footer*, así como el menú con las opciones *Inicio*, *Compra* y *Status*.

- En cada una de las páginas está inactiva la opción de menú en la que nos encontramos.

- La opción de menú en la que nos encontramos aparece pintada en amarillo.

- En el menú *Inicio*, si no hay movimientos registrados aún aparece el texto *"Sin movimientos"*.

- La cantidad de euros que podemos gastar es ilimitada.

- Si se pretende tradear o vender una criptomoneda, el sistema no permitirá vender más cantidad de la criptomoneda que se pretende vender que el saldo de la misma que figure en la tabla movimientos. Así tendremos dos mensajes de error: 
```
"No tiene suficiente saldo de esta moneda.": cuando disponemos de dicha moneda pero no de la cantidad con la que se quiere trabajar.

"No dispone de esta moneda": cuando no disponemos de dicha moneda.
```

