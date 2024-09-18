import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_currency_converter_to_rubles

load_dotenv()

url = "https://api.apilayer.com/exchangerates_data/convert"
headers = {"apikey": os.getenv("API_KEY")}
payload = {"amount": 3, "from": "EUR", "to": "RUB"}


@patch("requests.get")
def test_get_currency_converter_to_rubles(mock_get):
    mock_get.return_value.json.return_value = {"result": 30.00}
    assert get_currency_converter_to_rubles("EUR", 3) == 30.00
    mock_get.assert_called_once_with(url, headers=headers, params=payload)
