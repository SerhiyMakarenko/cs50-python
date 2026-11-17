import sys
import csv

args = sys.argv[1:]

students = []

if len(args) > 2:
    sys.exit("Too many command-line arguments")
elif len(args) <= 1:
    sys.exit("Too few command-line arguments")
elif len(args) == 2:
    if args[0].endswith("csv"):
        try:
            with open(args[0]) as before:
                reader = csv.DictReader(before)
                for row in reader:
                    last, first = row["name"].split(",")
                    house = row["house"]
                    students.append({"first": first.strip(), "last": last, "house": house})
        except FileNotFoundError:
            sys.exit(f"Could not read {args[0]}")
        try:
            with open(args[1], "w") as after:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(after, fieldnames=fieldnames)

                writer.writeheader()
                for student in students:
                    writer.writerow(student)
        except FileNotFoundError:
            sys.exit(f"Could not read {args[1]}")