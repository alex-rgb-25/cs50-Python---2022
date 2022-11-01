from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("50/100") == 50
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ZeroDivisionError):
        convert("30/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(75) =="75%"
    assert gauge(1) == "E"
