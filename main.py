import os
import random
from tkinter import *
from tkinter import messagebox
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
    draw_text = ImageDraw.Draw(txt)

    # Creating text and font object
    text = water_mark.get()
    font = ImageFont.truetype('~/Library/Fonts/Arial.ttf', 32)

    # Text size
    width, height = img.size

    # Lets position the texts
    counter = 0
    for i in range(20):
        counter += width * height / 13.7

        x = counter % width
        y = counter // width

        draw_text.text((x, y * 0.95), text,
                       fill=(255, 255, 255, 100), font=font)

    # Saving the new image with a marked label
    img = Image.alpha_composite(img, txt)
    img = img.convert("RGB")
    try:
        img.save(f"{filename}_marked.{extension}")
    except:
        messagebox.showerror(
            message="There was an error saving the image!")
    else:
        messagebox.showinfo(message="Image saved successfully.")


# -------------------------- SELECT FILE ------------------------------ #


def file_select():
    if len(water_mark.get()) == 0:
        messagebox.showwarning(message="Please enter a Watermark text.")
    else:
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

watermark_label = Label(text="Enter watermark text: ")
watermark_label.grid(column=0, row=1)

file_select_label = Label(text="Please select file to upload: ")
file_select_label.grid(column=0, row=3)

# Inputs
water_mark = Entry(width=20)
water_mark.grid(column=0, row=2)
water_mark.focus()

# Buttons
select_button = Button(text="Select", command=file_select)
select_button.grid(column=0, row=4)

window.mainloop()
