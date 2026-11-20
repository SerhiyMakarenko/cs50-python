def main():
    yell("This", "is", "CS50", "and", "I", "love", "it")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()