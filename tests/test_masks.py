from src.masks import get_mask_account, get_mask_card_number


def test_1_get_mask_card_number():
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"


def test_2_get_mask_card_number(number1, number2, number3, number4, number5):
    assert get_mask_card_number(number1) == ""
    assert get_mask_card_number(number2) == ""
    assert get_mask_card_number(number3) == ""
    assert get_mask_card_number(number4) == ""
    assert get_mask_card_number(number5) == ""


def test_1_get_mask_account():
    assert get_mask_account("35383033474447895560") == "**5560"


def test_2_get_mask_account(number1, number2, number3, number4, number5):
    assert get_mask_account(number1) == ""
    assert get_mask_account(number2) == ""
    assert get_mask_account(number3) == ""
    assert get_mask_account(number4) == ""
    assert get_mask_account(number5) == ""
