"""Tests for the integer calculator."""


import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_add_negative():
    assert calculator.add(-1, -2) == -3


def test_subtract():
    assert calculator.subtract(5, 3) == 2


def test_subtract_negative_result():
    assert calculator.subtract(3, 5) == -2


def test_multiply():
    assert calculator.multiply(4, 3) == 12


def test_multiply_by_zero():
    assert calculator.multiply(7, 0) == 0


def test_divide():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    assert calculator.divide(5, 0) is None


def test_divide_truncates():
    assert calculator.divide(7, 2) == 3


def test_calculate_add():
    assert calculator.calculate("2", "+", "3") == 5


def test_calculate_unknown_operator():
    assert calculator.calculate("2", "x", "3") is None


def test_calculate_malformed():
    assert calculator.calculate("a", "+", "3") is None
    assert calculator.calculate("2", "+", "b") is None


def test_cli_success(capsys):
    rc = calculator.main(["2", "+", "3"])
    captured = capsys.readouterr()
    assert rc == 0
    assert captured.out.strip() == "5"


def test_cli_division_by_zero(capsys):
    rc = calculator.main(["5", "/", "0"])
    captured = capsys.readouterr()
    assert rc == 1
    assert "Error" in captured.err


def test_cli_bad_args(capsys):
    rc = calculator.main(["2", "+"])
    captured = capsys.readouterr()
    assert rc == 1
    assert "Usage" in captured.err
