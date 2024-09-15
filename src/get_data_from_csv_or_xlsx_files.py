import pandas as pd


def get_data_from_csv(filename: str) -> list[dict]:
    """The function gets data from a csv file and returns a list of dictionaries with transactions"""
    df = pd.read_csv(filename, sep=";", encoding="utf-8")
    result = df.to_dict(orient="records")
    return result


def get_data_from_xlsx(filename: str) -> list[dict]:
    """The function gets data from a xlsx file and returns a list of dictionaries with transactions"""
    df = pd.read_excel(filename)
    result = df.to_dict(orient="records")
    return result
