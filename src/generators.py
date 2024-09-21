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
