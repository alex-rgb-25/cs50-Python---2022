from bank import value
import pytest


def test_full_greet():
    assert value("hello") == 0
    assert value("hello, there!") == 0
    assert value("HELLO") == 0

def test_mid_greet():
    assert value("hey, there!") == 20
    assert value("how are you?") == 20
    assert value("HoW are you?") == 20

def test_no_greet():
    assert value("it's rainy today!") == 100
    assert value("what a beautiful day") == 100
