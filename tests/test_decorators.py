from src.decorators import log


@log()
def test_func(a, b):
    return a / b


def test_1_log(capsys):
    test_func(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "Function: test_func -> error: ZeroDivisionError -> inputs: ((2, 0), {})\n"


def test_2_log(capsys):
    test_func(32, 8)
    captured = capsys.readouterr()
    assert captured.out == "Function: test_func ok\n"
