import sys

lines = []
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-2:] != "py":
        sys.exit("Not a Python file")
    with open(sys.argv[1]) as file:
        for line in file:
            if(len(line) != 1):
                try:
                    if line.lstrip()[0] != "#":
                        lines.append(line)
                #if it throws this error it means the line is all spaces so we skip it
                except IndexError:
                    continue

    print(len(lines))
except FileNotFoundError:
    sys.exit("File does not exists")
