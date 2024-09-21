import re
from collections import Counter
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


def filter_transactions_by_description(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция принимает список словарей с данными о транзакциях и строку поиска
    Возвращает список словарей, у которых в описании есть данная строка"""
    pattern = rf"{search_string}"
    result_transactions_dict = [
        transaction
        for transaction in transactions
        if re.findall(pattern, transaction["description"], flags=re.IGNORECASE)
    ]
    return result_transactions_dict


def counting_categorys(transactions: list[dict], categories: list[str]) -> dict:
    """Функця принимает список словарей с данными о транзакциях и список категорий
    Возвращает словарь где ключ = название категории, значение = количество оперций в каждой категории"""
    category_list = []
    for transaction in transactions:
        for category in categories:
            pattern = rf"{category}"
            if re.findall(pattern, transaction["description"], flags=re.IGNORECASE):
                category_list.append(transaction["description"])
    result_category_dict = Counter(category_list)
    return dict(result_category_dict)
