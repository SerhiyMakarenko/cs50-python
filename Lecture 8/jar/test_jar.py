import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(10)
    assert jar.capacity == 10
    with pytest.raises(ValueError):
        jar = Jar(-10)
    with pytest.raises(ValueError):
        jar = Jar("cat")
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar(1.5)
    jar = Jar(0)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar.deposit(-3)
    with pytest.raises(ValueError):
        jar.deposit(3)
    jar.deposit(2)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(8)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(4)
    with pytest.raises(ValueError):
        jar.withdraw(-4)
    jar.withdraw(2)
    assert jar.size == 0