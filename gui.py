import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

window = tkinter.Tk()
window.title("Image Watermarking")
window.config(padx=20, pady=20)

tkinter.Button(window, text="Open File",
               command=select_file).grid(row=2, column=0)

filename = askopenfilename()
print(filename)
