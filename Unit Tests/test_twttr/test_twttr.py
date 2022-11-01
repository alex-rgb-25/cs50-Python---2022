from twttr import shorten
import pytest

def test_shorten():
    assert shorten("alex") == "lx"
    assert shorten("setting up my twitter") == "sttng p my twttr"
    assert shorten("Alex is HEre") == "lx s Hr"
    assert shorten("One, two, three") == "n, tw, thr"
    assert shorten("1, 2, three") == "1, 2, thr"
