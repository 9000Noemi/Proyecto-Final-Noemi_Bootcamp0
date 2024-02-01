import requests
from config import APIKEY

coin_from = ""
coin_to = ""

#invocando al metodo get con la url especifica:
url = f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?apikey={APIKEY}"
#r = requests.get(url)

r={
  "time": "2024-01-30T18:53:45.0000000Z",
  "asset_id_base": "BTC",
  "asset_id_quote": "EUR",
  "rate": 2.48
}



lista_general = r.json()
#lista_monedas = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]


