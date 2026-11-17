from jar import Jar


def test_init():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(-3)
    assert deposit(jar) == "The number of coockies can't be negative."
    jar.deposit(13)
    assert deposit(jar) == "The deposite exids the capacity of the jar."


def test_withdraw():
    ...