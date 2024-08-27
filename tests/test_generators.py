import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_1_filter_by_currency(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    assert next(generator) == "Генератор исчерпан"
    assert next(generator) == "Генератор исчерпан"


def test_2_filter_by_currency(transactions):
    generator = filter_by_currency(transactions, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }
    assert next(generator) == "Генератор исчерпан"
    assert next(generator) == "Генератор исчерпан"


def test_3_filter_by_currency(transactions):
    generator = filter_by_currency(transactions, "")
    assert next(generator) == "Отсутствуют данные для корректной фильтрации"
    assert next(generator) == "Генератор исчерпан"
    assert next(generator) == "Генератор исчерпан"


def test_4_filter_by_currency(transactions):
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Отсутствуют данные для корректной фильтрации"
    assert next(generator) == "Генератор исчерпан"


def test_1_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Генератор исчерпан"
    assert next(generator) == "Генератор исчерпан"


def test_2_transaction_descriptions():
    generator = transaction_descriptions([])
    assert next(generator) == "Пустой список"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            8,
            13,
            [
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
                "0000 0000 0000 0013",
            ],
        ),
        (
            23569874156,
            23569874160,
            [
                "0000 0235 6987 4156",
                "0000 0235 6987 4157",
                "0000 0235 6987 4158",
                "0000 0235 6987 4159",
                "0000 0235 6987 4160",
            ],
        ),
        (33, 33, ["0000 0000 0000 0033"]),
    ],
)
def test_1_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected


def test_2_card_number_generator():
    generator = card_number_generator(12345678901234567, 12345678901234560)
    assert next(generator) == "Слишком длинный номер карты"
