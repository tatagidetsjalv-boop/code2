from PIL import Image, ImageEnhance

bad_tiger = Image.open("tiger.webp")

tiger = ImageEnhance.Contrast(bad_tiger).enhance(3)

tiger.save("tiger.jpg")