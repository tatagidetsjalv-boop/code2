

from PIL import Image, ImageDraw

# RGB-värden för blå och gul
BLUE = (0, 106, 167)
YELLOW = (254, 204, 0)
GREEN = (0, 128, 0)
RED = (	255, 0, 0)
WHITE = (255, 255, 255)

# Skapa en ny bild
im = Image.new("RGB", (160, 100), GREEN)

# Skapa ett ImageDraw-objekt för att kunna rita grafik
imd = ImageDraw.Draw(im)

# Rita två rektanglar
imd.rectangle([(45, 0), (75, 100)], WHITE)
imd.rectangle([(0, 35), (160, 65)], WHITE)
imd.rectangle([(50, 0), (70, 100)], RED)
imd.rectangle([(0, 40), (160, 60)], RED)

im.save("flag.png")