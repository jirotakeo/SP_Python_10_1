import json

from src.external_api import get_currency_converter_to_rubles


def get_transactions_from_json(path_to_file: str) -> list[dict]:
    """Returns a list of dictionaries with financial transaction data from a json file"""
    try:
        with open(path_to_file, encoding="utf-8") as f:
            result = json.load(f)
        return result
    except Exception:
        return []


def get_transaction_amount(transaction: dict) -> float:
    """Returns the transaction amount in rubles"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency != "RUB":
        return get_currency_converter_to_rubles(currency, amount)
    else:
        return float(amount)
