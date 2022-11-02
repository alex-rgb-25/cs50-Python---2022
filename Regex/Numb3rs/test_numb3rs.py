import pytest
from numb3rs import validate

def test_range():
    assert validate("255.255.255.255") == "True"
    assert validate("256.255.255.255") == "False"
    assert validate("0.0.133.255") == "True"
    assert validate("-2.255.255.255") == "False"
    assert validate("2..255.255") == "False"
    assert validate("244") == "False"
    assert validate("2") == "False"
    assert validate("") == "False"
    assert validate("asd") == "False"
    assert validate("a.av.abc.a") == "False"
    assert validate("75.456.76.65") == "False"
    assert validate("75.456.476.365") == "False"

    assert validate(r"1.2") == "False"
    assert validate(r"1.2.3.4") == "True"
    assert validate(r"1") == "False"
    assert validate(r"1.2.3") == "False"

def test_groups():
    assert validate("255.255.255") == "False"
    assert validate("255.255.255.255") == "True"
    assert validate("255.255") == "False"


    assert validate(r"255.255.255.255") == "True"
    assert validate(r"512.1.1.1") == "False"
    assert validate(r"1.512.1.1") == "False"
    assert validate(r"1.1.512.1") == "False"
    assert validate(r"1.1.1.512") == "False"
