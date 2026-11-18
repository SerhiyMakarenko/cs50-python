from calculator1 import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square is not 0")


if __name__ == "__main__":
    main()
