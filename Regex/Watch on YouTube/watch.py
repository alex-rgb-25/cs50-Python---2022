import re
import sys

def main():
     print(parse(input("HTML: ")))

def parse(s):
    url = ""
    if matches := re.search(r"<iframe.*https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)", s):
        url= "https://youtu.be/" + matches.group(1)
        return url
    else:
        return None

if __name__ == "__main__":
    main()
