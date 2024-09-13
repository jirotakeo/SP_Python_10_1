import json
import logging

from src.external_api import get_currency_converter_to_rubles

logging.basicConfig(
    filename="../logs/utils.log",
    filemode="w",
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def get_transactions_from_json(path_to_file: str) -> list[dict]:
    """Returns a list of dictionaries with financial transaction data from a json file"""
    logger.info(f"Запуск функции {get_transactions_from_json.__name__}")
    try:
        with open(path_to_file, encoding="utf-8") as f:
            result = json.load(f)
        logger.info(f"Успешное завершение работы функции {get_transactions_from_json.__name__}")
        return result
    except Exception as e:
        logger.error(f"Ошибка. {e}.")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """Returns the transaction amount in rubles"""
    logger.info(f"Запуск функции {get_transaction_amount.__name__}")
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        if currency != "RUB":
            logger.info(f"Успешное завершение работы функции {get_transaction_amount.__name__}")
            return get_currency_converter_to_rubles(currency, amount)
        else:
            logger.info(f"Успешное завершение работы функции {get_transaction_amount.__name__}")
            return float(amount)
    except Exception as e:
        logger.error(f"Ошибка. {e}.")
