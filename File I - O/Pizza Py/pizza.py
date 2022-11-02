import csv
from tabulate import tabulate
import sys

items = []
headers = []
table = []
pre = []

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-3:] != "csv":
        sys.exit("Not a CSV file")

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)

        for key in items[0].keys():
            headers.append(key)

        for item in items:
            pre = []
            pre.append(item[headers[0]])
            pre.append(item[headers[1]])
            pre.append(item[headers[2]])
            table.append(pre)
        print(tabulate(table, headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
