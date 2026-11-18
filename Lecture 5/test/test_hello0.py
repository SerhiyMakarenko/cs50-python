from hello0 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Serhii") == "hello, Serhii"
