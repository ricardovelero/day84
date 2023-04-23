import random
from PIL import Image, ImageDraw, ImageFont

# Let's open the Image
img = Image.open(r'cake.webp').convert("RGBA")

# Create a text Layer
txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

text = "Soluciones iO"
font = ImageFont.truetype(
    "/Users/ricardorodriguez/Library/Fonts/Arial.ttf", 27)

draw = ImageDraw.Draw(txt)

# Text position
width, height = img.size

# Loop to paste multiple marks
y = 200
for i in range(7):
    x = random.randint(0, width-300)
    y += random.randrange(0, int(height/8), 19) + random.randint(0, 100)
    draw.text((x, y), text, fill=(255, 255, 255, 90), font=font)

#  Combine both layers
watermarked = Image.alpha_composite(img, txt)
watermarked.save(r'cake_marked.webp')
