def main():
    n = int(input("What's n? "))
    for s in sleep(n):
        print(s)


def sleep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()