from PIL import Image
import sys

try:
    im = Image.open("pillow-logo-248x250.png")

except IOError:
    print("Check your image format")
    sys.exit(1)

im.show()
