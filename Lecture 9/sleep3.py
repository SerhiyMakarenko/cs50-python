def main():
    n = int(input("What's n? "))
    for s in sleep(n):
        print(s)


def sleep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
