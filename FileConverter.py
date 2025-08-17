import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import os

# Variable to store selected file
filepath = ""
filename = ""

# Conversion functions
def toPNG():
    if filepath:
        print("Converting to PNG:", filepath)
        converted = Image.open(filepath)
        newName = "Converted-" + filename.split('.')[0]
        newPath = os.path.split(filepath)[0]
        converted.save(f"{newPath}/{newName}.png")
    else:
        print("No file selected")

def toJPG():
    if filepath:
        print("Converting to JPG:", filepath)
        converted = Image.open(filepath)
        converted = converted.convert("RGB")
        newName = "Converted-" + filename.split('.')[0]
        newPath = os.path.split(filepath)[0]
        converted.save(f"{newPath}/{newName}.jpg")
    else:
        print("No file selected")

def toPDF():
    if filepath:
        print("Converting to PDF:", filepath)
        converted = Image.open(filepath)
        converted = converted.convert("RGB")
        newName = "Converted-" + filename.split('.')[0]
        newPath = os.path.split(filepath)[0]
        converted.save(f"{newPath}/{newName}.pdf")
    else:
        print("No file selected")

# File browsing function
def browse_file():
    global filepath, filename
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.pdf")])
    browse_Treeview.item(browse_Treeview.get_children()[0], text=filepath)
    filename = os.path.split(filepath)[1]
    print(filename)

# Root of GUI 
root = tk.Tk()
root.title("File Converter")

# Root frame scaling
root.columnconfigure(0, weight=1)

# Frame containing file finding widgets
browserFrame = ttk.Frame(root, padding="5")
browserFrame.grid(row=0, column=0, sticky="news")

# Configure browserFrame resizing
browserFrame.columnconfigure(1, weight=1)

# Button to search for file
browse_Button = ttk.Button(browserFrame, text="Browse", command= lambda: browse_file())
browse_Button.grid(row=0, column=0, sticky="e")

# Treeview to display selected file
browse_Treeview = ttk.Treeview(browserFrame, height=1, show='tree')
browse_Treeview.insert('', 0, text='Select a File.')
browse_Treeview.column('#0', width=100, stretch=True)
browse_Treeview.grid(row=0, column=1, sticky="ew")

# Frame containing file conversion widgets
convertFrame = ttk.Frame(root, padding="5")
convertFrame.grid(row=1, column=0, sticky="news")

# Configure convertFrame resizing
convertFrame.columnconfigure(0, weight=1)
convertFrame.columnconfigure(1, weight=1)
convertFrame.columnconfigure(2, weight=1)

# Conversion buttons
pngButton = ttk.Button(convertFrame, text="Convert to PNG", command=toPNG)
pngButton.grid(row=0, column=0, sticky="ew")

jpgButton = ttk.Button(convertFrame, text="Convert to JPG", command=toJPG)
jpgButton.grid(row=0, column=1, sticky="ew")

pdfButton = ttk.Button(convertFrame, text="Convert to PDF", command=toPDF)
pdfButton.grid(row=0, column=2, sticky="ew")

root.mainloop()
