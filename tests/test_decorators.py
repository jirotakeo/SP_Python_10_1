from src.decorators import log


@log()
def test_func(a, b):
    return a / b


def test_1_log(caplog):
    assert test_func(2, 0) is None
    assert caplog.record_tuples[0][2] == "Function: test_func -> error: ZeroDivisionError -> inputs: ((2, 0), {})"


def test_2_log(caplog):
    assert test_func(32, 8) == 4
    assert caplog.record_tuples[0][2] == "Function: test_func ok"
