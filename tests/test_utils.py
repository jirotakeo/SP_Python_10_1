from unittest.mock import patch

from src.utils import get_transaction_amount, get_transactions_from_json


def test_get_transactions_from_json_empty_file():
    assert get_transactions_from_json("") == []
    assert get_transactions_from_json("/data/operations.json") == []
    assert get_transactions_from_json("test_operations.json") == []


def test_get_transaction_amount_from_currency_RUB(transaction_RUB):
    assert get_transaction_amount(transaction_RUB) == 67314.70


@patch("src.utils.get_currency_converter_to_rubles")
def test_get_transaction_amount_from_currency_USD(mock_get_currency_converter_to_rubles, transaction_USD):
    mock_get_currency_converter_to_rubles.return_value = 8392976.11
    assert get_transaction_amount(transaction_USD) == 8392976.11


def test_get_transaction_amount2(patch_currency_converter, transaction_USD):
    assert get_transaction_amount(transaction_USD) == 8392976.11
