import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("73654108430135874305 Счет", ""),
        ("7158300734726758 Master Card", ""),
        ("Visa Classic 71583000734726758", ""),
        ("", ""),
    ],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", ""),
        ("2024-13-42T02:26:18.671407", ""),
    ],
)
def test_get_date(input_data, expected):
    assert get_date(input_data) == expected
