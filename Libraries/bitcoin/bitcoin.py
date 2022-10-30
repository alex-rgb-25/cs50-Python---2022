import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    curValue = float(response.json()["bpi"]["USD"]["rate_float"])
    total = curValue * n
    print(f"${total:,.4f}")

except requests.RequestException:
    print("Wrong url")
