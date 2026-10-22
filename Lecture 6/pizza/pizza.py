import sys
import csv
from tabulate import tabulate

args = sys.argv[1:]

if len(args) > 1:
    sys.exit("Too many command-line arguments")
elif len(args) == 0:
    sys.exit("Too few command-line arguments")
elif len(args) == 1:
    if args[0].endswith("csv"):
        try:
            with open(args[0]) as file:
                pizza_menu = []
                reader = csv.DictReader(file)
                for row in reader:
                    pizza_menu.append(row)
                print(tabulate(pizza_menu))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")