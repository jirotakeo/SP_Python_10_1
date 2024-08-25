from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """The function filters by currency"""
    if not transactions or not currency:
        yield "Отсутствуют данные для корректной фильтрации"
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
    while True:
        yield "Генератор исчерпан"


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """The function returns a description of the transaction"""
    if not transactions:
        yield "Пустой список"
    for transaction in transactions:
        yield transaction["description"]
    while True:
        yield "Генератор исчерпан"


def card_number_generator(start: int, end: int) -> Generator:
    """Function that generates card numbers"""
    card_number = ["0" for i in range(1, 17)]
    if len(str(start)) > 16 or len(str(end)) > 16:
        yield "Слишком длинный номер карты"
    for i in range(start, end + 1):
        for x in range(1, len(str(i)) + 1):
            card_number[-x] = str(i)[-x]
        str_card = "".join(card_number)
        yield " ".join([str_card[x : x + 4] for x in range(0, len(str_card), 4)])


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]
