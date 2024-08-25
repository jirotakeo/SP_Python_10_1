from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Принимает на вход номер карты/счета и возвращает маску"""
    number = data.split(" ")
    if len(number[-1]) == 20 and number[-1].isdigit():
        return f"{number[0]} {get_mask_account(number[-1])}"
    elif len(number[-1]) == 16 and number[-1].isdigit():
        return f"{' '.join(number[0:-1])} {get_mask_card_number(number[-1])}"
    else:
        return ""


def get_date(date: str) -> str:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    if date != "":
        try:
            formated_date = datetime.strptime(date.split("T")[0], "%Y-%m-%d")
            return datetime.strftime(formated_date, "%d.%m.%Y")
        except ValueError:
            return ""
    else:
        return ""
