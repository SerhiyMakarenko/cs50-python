import sys

args = sys.argv[1:]

if len(args) > 1:
    sys.exit("Too many command-line arguments")
elif len(args) == 0:
    sys.exit("Too few command-line arguments")
elif len(args) == 1:
    if args[0].endswith("py"):
        try:
            with open(args[0]) as file:
                lines = 0
                for line in file:
                    lines += 1
                print(lines)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")