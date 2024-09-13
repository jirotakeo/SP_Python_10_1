import logging

logging.basicConfig(
    filename="../logs/masks.log",
    filemode="w",
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    logger.info(f"Запуск функции {get_mask_card_number.__name__}")
    if card_number.isdigit() and len(card_number) == 16:
        logger.info(f"Успешное завершении работы функции {get_mask_card_number.__name__}")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.error("Ошибка. Некорректный номер карты")
        return ""


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    logger.info(f"Запуск функции {get_mask_account.__name__}")
    if account_number.isdigit() and len(account_number) == 20:
        logger.info(f"Успешное завершение работы функции {get_mask_account.__name__}")
        return f"**{account_number[-4:]}"
    else:
        logger.error("Ошибка. Некорректный номер счета")
        return ""
