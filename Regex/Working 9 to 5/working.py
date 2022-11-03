import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    h1= ""
    h2 = ""
    m1 = "00"
    m2 = "00"
    if matches := re.search(r"^([0-9]|[0-1][0-2])(?::(0[0-9]|[1-5][0-9]))? ([A|P]M) (to) ([0-9]|[0-1][0-2])(?::(0[0-9]|[1-5][0-9]))? ([A|P]M)", s):
        try:
            if matches.group(4) != "to":
                raise ValueError
            if int(matches.group(1)) == None:
                    raise ValueError
            if int(matches.group(5)) == None:
                    raise ValueError

            if matches.group(3) == "PM":
                if int(matches.group(1)) != 12:
                    h1 = int(matches.group(1)) + 12
                else:
                    h1 = int(matches.group(1))
                if h1 == 24:
                    h1 = "00"
                if matches.group(7) == "PM":
                    if int(matches.group(5)) != 12:
                        h2 = int(matches.group(5)) + 12
                    else:
                        h2 = int(matches.group(5))
                    if h2 == 24:
                        h2 = "00"
                else:
                    if int(matches.group(5)) == 12:
                        h2 = "00"
                    else:
                        h2 = int(matches.group(5))
                m1 = matches.group(2)
                m2 = matches.group(6)
            elif matches.group(3) == "AM":
                if int(matches.group(1)) == 12:
                    h1 = "00"
                else:
                    h1 = int(matches.group(1))
                if matches.group(7) == "PM":
                    if int(matches.group(5)) != 12:
                        h2 = int(matches.group(5)) + 12
                    else:
                        h2 = int(matches.group(5))
                    if h2 == 24:
                        h2 = "00"
                else:
                    h2 = int(matches.group(5))
                m1 = matches.group(2)
                m2 = matches.group(6)


            if h1 == 0:
                h1="00"
            if h2 == 0:
                h2="00"
            if m1 == None:
                m1="00"
            if m2 == None:
                m2="00"

            if len(str(h1)) == 1:
                hour1 = str(h1).zfill(2)
            else:
                hour1 = h1
            if len(str(h2)) == 1:
                hour2 = str(h2).zfill(2)
            else:
                hour2 = h2

            return f"{hour1}:{m1} to {hour2}:{m2}"
        except ValueError:
            sys.exit("Invalid Hours!")
    else:
        raise ValueError

if __name__ == "__main__":
    main()
