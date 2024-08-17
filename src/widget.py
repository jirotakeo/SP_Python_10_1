from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Принимает на вход номер карты/счета и возвращает маску"""
    if "Счет" in number:
        return f"{number.split()[0]} {get_mask_account(number.split()[-1])}"
    else:
        return f"{' '.join(number.split()[0:-1])} {get_mask_card_number(number.split()[-1])}"


def get_date(date: str) -> str:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    formated_date = datetime.strptime(date.split("T")[0], "%Y-%m-%d")
    return datetime.strftime(formated_date, "%d.%m.%Y")


data_test = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

date_test = "2024-03-11T02:26:18.671407"

for i in data_test:
    print(mask_account_card(i))

print(get_date(date_test))
