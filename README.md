# Виджет банковских операций
Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.

## Зависимости
- flake8 = "^7.1.1"
- mypy = "^1.11.1"
- black = "^24.8.0"
- isort = "^5.13.2"

## Функции
- Функция `get_mask_card_number` скрывающая номер карты
- Функция `get_mask_account` скрывающая номер счета
- Функция `filter_by_state` фильтрует операции по счетам по статусу
- Функция `sort_by_date` сортировка по дате
- Функция `filter_by_currency` фильтрует транзакции по коду валюты
- Функция `transaction_descriptions` возвращает описание транзакций
- Функция `card_number_generator` гененрирует номера карт в заданном диапазоне

## Инструкция по установке
Чтобы скачать репозиторий:

`git clone https://github.com/jirotakeo/SP_Python_10_1`

## Тестирование
Для тестирования используется pytest
Введите в терминале команду `pytest`, чтобы запустить тесты
