from src.get_data_from_csv_or_xlsx_files import get_data_from_csv, get_data_from_xlsx
from src.processing import filter_by_state, filter_transactions_by_description, sort_by_date
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card


def main():
    """Интерфейс взаимодействия с пользователем"""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями!
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла;
    2. Получить информацию о транзакциях из CSV-файла;
    3. Получить информацию о транзакциях из XLSX-файла."""
    )
    while True:
        user_choise = input("Пользователь: ")
        if user_choise == "1":
            print("Программа: Для обработки выбран JSON-файл.")
            transactions = get_transactions_from_json("../data/operations.json")
            break
        elif user_choise == "2":
            print("Программа: Для обработки выбран CSV-файл.")
            transactions = get_data_from_csv("../data/transactions.csv")
            break
        elif user_choise == "3":
            print("Программа: Для обработки выбран XLSX-файл.")
            transactions = get_data_from_xlsx("../data/transactions_excel.xlsx")
            break
        else:
            print("Такого пункта нет, попробуйте еще раз.")

    status_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы:  EXECUTED, CANCELED, PENDING"""
        )
        status_choise = input("Пользователь: ").upper()
        if status_choise in status_list:
            result = filter_by_state(transactions, status_choise)
            print(f"Программа: Операции отфильтрованы по статусу {status_choise}")
            break
        else:
            print("Такого пункта нет, попробуйте еще раз.")

    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет: ")
        date_sort_choise = input("Пользователь: ").lower()
        if date_sort_choise == "да":
            print("Программа: Отсортировать по возрастанию или по убыванию? ")
            asc_desc_choise = input("Пользователь: ").lower()
            if asc_desc_choise == "по возрастанию":
                result = sort_by_date(result, False)
                break
            elif asc_desc_choise == "по убыванию":
                result = sort_by_date(result)
                break
        elif date_sort_choise == "нет":
            break
        else:
            print("Такого пункта нет, попробуйте еще раз.")

    while True:
        print("Программа: Выводить только рублёвые транзакции? Да/Нет:")
        currency_choise = input("Пользователь: ").lower()
        if currency_choise == "да" and user_choise == "1":
            result = [
                transaction for transaction in result if transaction["operationAmount"]["currency"]["code"] == "RUB"
            ]
            break
        elif currency_choise == "да" and user_choise in ["2", "3"]:
            result = [transaction for transaction in result if transaction["currency_code"] == "RUB"]
            break
        elif currency_choise == "нет":
            break
        else:
            print("Такого пункта нет, попробуйте еще раз.")

    while True:
        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет:")
        sorted_by_description_choise = input("Пользователь: ").lower()
        if sorted_by_description_choise == "да":
            word = input("Программа: Слово для сортировки: ")
            result = filter_transactions_by_description(result, word)
            break
        elif sorted_by_description_choise == "нет":
            break
        else:
            print("Такого пункта нет, попробуйте еще раз.")

    print("Распечатываю итоговый список транзакций...")

    if len(result) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(result)}")
        for tr in result:
            tr_date = get_date(tr["date"])
            if user_choise == "1":
                currency = tr["operationAmount"]["currency"]["code"]
            else:
                currency = tr["currency_code"]

            if tr["description"] == "Открытие вклада":
                from_to = mask_account_card(tr["to"])
            else:
                from_to = mask_account_card(tr["from"]) + " -> " + mask_account_card(tr["to"])

            if user_choise == "1":
                amount = tr["operationAmount"]["amount"]
            else:
                amount = tr["amount"]
            print(
                f"""{tr_date} {tr['description']}
{from_to}
Сумма: {round(float(amount))} {currency}
                """
            )


if __name__ == "__main__":
    main()
