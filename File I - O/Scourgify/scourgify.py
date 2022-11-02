import sys
import csv

people = []
dictPeople = {}

try:

    if len(sys.argv) > 3:
        sys.exit("Too many comand-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few comand-line arguments")

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for line in reader:
            last, first = line["name"].split(", ")
            # dictPeople["first"] = first
            # dictPeople["last"] = last
            # dictPeople["house"] = line["house"]
            dictPeople = { "first": first, "last": last, "house": line["house"]}
            people.append(dictPeople)

    with open(sys.argv[2], "w", newline="") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        for line in people:
            writer.writerow(line)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
