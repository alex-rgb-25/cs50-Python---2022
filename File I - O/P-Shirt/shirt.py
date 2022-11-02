from PIL import Image
from PIL import ImageOps
import sys


try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")
    input = sys.argv[1]
    output = sys.argv[2]
    print(input[-4:])
    if input[-4:] not in [".jpg", ".png"]:
        if input[-5:] != ".jpeg":
            sys.exit("Invalid input")
    if output[-4:] not in [".jpg", ".png"]:
        if output[-5:] != ".jpeg":
            sys.exit("Invalid input")

    if input[-4:] != output[-4:]:
        sys.exit("Input and Output have different extensions")

    imagefile = Image.open(sys.argv[1])

    shirt = Image.open("shirt.png")
    size = shirt.size

    image2 = ImageOps.fit(imagefile, size)        # width height

    image2.paste(shirt, shirt)

    image2.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
