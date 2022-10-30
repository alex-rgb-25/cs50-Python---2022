from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
arr = figlet.getFonts()

if(len(sys.argv) == 1):
    #random font:
    txt = input("input: ")
    figlet.setFont(font = random.choice(arr))
    print(figlet.renderText(txt))
elif len(sys.argv) == 3 and (sys.argv[1]=="-f" or sys.argv[1] =="--font"):
    if sys.argv[2] in arr:
        txt = input("input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(txt))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
