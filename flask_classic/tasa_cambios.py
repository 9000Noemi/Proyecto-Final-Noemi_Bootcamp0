import requests
from config import APIKEY

moneda_from = ""
moneda_to = ""

#invocando al metodo get con la url especifica:
url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_from}/{moneda_to}?apikey={APIKEY}"
r = requests.get(url)

lista_general = r.json()



