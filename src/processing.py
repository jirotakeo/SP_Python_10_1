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
