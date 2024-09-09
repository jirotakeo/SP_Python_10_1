import os

import requests
from dotenv import load_dotenv

load_dotenv()
headers = {"apikey": os.getenv("API_KEY")}


def get_currency_converter_to_rubles(currency: str, amount: float) -> float:
    """Converts currency into rubles"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": amount, "from": currency, "to": "RUB"}
    response = requests.get(url, headers=headers, params=payload)
    result = round(response.json()["result"], 2)
    return result
