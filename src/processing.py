from typing import Any


def filter_by_state(data: list[dict[str, Any]], stat="EXECUTED") -> list[dict[str, Any]]:
    """Принимает список словарей и опционально значение для ключа state.
    Возвращает новый список словарей, содержащий словари у которых ключ state соответствует указанному значению
    """
    new_list = []
    for i in data:
        if i.get("state") == stat:
            new_list.append(i)
    return new_list


def sort_by_date(data: list[dict[str, Any]], ascending=True) -> list[dict[str, Any]]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате"""

    return sorted(data, key=lambda x: x["date"], reverse=ascending)


test_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


print(filter_by_state(test_data))
print(filter_by_state(test_data, "EXECUTED"))
print(filter_by_state(test_data, "CANCELED"))


print(sort_by_date(test_data))
print(
    sort_by_date(test_data)
    == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
)
print(sort_by_date(test_data, False))
