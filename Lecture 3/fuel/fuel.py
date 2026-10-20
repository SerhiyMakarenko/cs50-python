def main():
    f = get_fraction("Fraction: ")
    if f == 100:
        print("F")
    elif f == 0:
        print("E")
    else:
        print(f"{int(f)}%")


def get_fraction(prompt):
    while True:
        fraction = input(prompt).split("/")
        try:
            if fraction[0].isdigit() is False:
                raise ValueError
            elif fraction[1].isdigit() is False:
                raise ValueError
            elif int(fraction[1]) == 0:
                raise ZeroDivisionError
            elif ((int(fraction[0]) / int(fraction[1])) * 100) > 100:
                raise ValueError
            else:
                return ((int(fraction[0]) / int(fraction[1])) * 100)
        except ValueError:
            print("ValueError")
            pass
        except ZeroDivisionError:
            print("ZeroDivisionError")
            pass


main()