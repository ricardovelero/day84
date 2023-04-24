import os
import random
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont

# ------------------------ WATERMARK FILE ------------------------------ #


def watermark(file):
    # Split filename and extension
    filename, extension = file.split('.')

    # Opening Image
    img = Image.open(file).convert("RGBA")
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

    # Creating draw object
    draw = ImageDraw.Draw(img)

    # Creating text and font object
    text = "Test"
    font = ImageFont.truetype('~/Library/Fonts/Arial.ttf', 27)

    # Positioning Text
    width, height = img.size

    y = 200
    for i in range(12):
        x = random.randint(0, width-300)
        y += random.randrange(0, int(height/8), 19)+random.randint(0, 100)
        draw.text((x, y), text, fill=(255, 255, 255, 75), font=font)

    # Combining both layers and saving new image
    watermarked = Image.alpha_composite(img, txt)

    # Saving the new image with a marked label
    img.save(f"{filename}_marked.{extension}")


# -------------------------- SELECT FILE ------------------------------ #


def file_select():
    file = askopenfilename(initialdir=os.getcwd, title="Select an Image", filetypes=[
        ("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg"), ("WEBP", "*.webp")])
    watermark(file)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermaking")
window.config(padx=50, pady=50)

# canvas = Canvas(width=200, height=200)
# canvas.grid(column=1, row=0)

# Labels
title_label = Label(
    text="This App let's you select a file and add a Watermark to it.")
title_label.grid(column=0, row=0, pady=20)

file_select_label = Label(text="Please select file to upload: ")
file_select_label.grid(column=0, row=1)

# Buttons
select_button = Button(text="Select", command=file_select)
select_button.grid(column=1, row=1)

window.mainloop()
