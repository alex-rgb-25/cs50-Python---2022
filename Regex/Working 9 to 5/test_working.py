import pytest

from working import convert


def test_working():
    assert convert("10:32 AM to 4:32 PM") == "10:32 to 16:32"
    assert convert("12:32 AM to 11:00 AM") == "00:32 to 11:00"
    assert convert("12:32 PM to 11:00 PM") == "12:32 to 23:00"
    assert convert("12:32 PM to 11:00 PM") == "12:32 to 23:00"
    assert convert("3:00 PM to 11:00 PM") == "15:00 to 23:00"

def test_errs():
    with pytest.raises(ValueError):
        convert("13:00 AM to 21:23 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM - 10:23 AM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 OM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("17:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("17:00 AM - 3:00 PM")
    with pytest.raises(ValueError):
        convert("17:00 AM - 3:00 AM")

    with pytest.raises(ValueError):
        convert("17:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("17:00 AM to 3:00 PM")
    with pytest.raises(ValueError):
        convert("17:00 AM to 3:00 AM")



def test_shortv():
    assert convert("5 PM to 3 AM") == "17:00 to 03:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
