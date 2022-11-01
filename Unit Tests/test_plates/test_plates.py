from plates import is_valid
import pytest

def test_first():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("A0C") == False
    assert is_valid("2ADB") == False
    assert is_valid("AI") == True
    assert is_valid("00") == False
    assert is_valid(" 2") == False
    assert is_valid("2") == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_for_zero():
    assert is_valid("AB023") == False
    assert is_valid("AB123") == True

def test_nums_end():
    assert is_valid("AB23A") == False
    assert is_valid("AB231") == True

def test_length():
    assert is_valid("AB34567") == False
    assert is_valid("AB3456") == True
    assert is_valid("AB302") == True
    assert is_valid("KI123456789") == False

def test_alpha():
    assert is_valid("AB:23") == False
    assert is_valid("AB,AD-") == False
