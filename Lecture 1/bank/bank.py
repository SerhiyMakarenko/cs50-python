greeting = input("Greeting: ")

greeting = greeting.lower()

match greeting:
    case greeting if greeting.startswith("hello"):
        print("$0")
    case greeting if greeting.startswith("h"):
        print("$20")
    case _:
        print("$100")