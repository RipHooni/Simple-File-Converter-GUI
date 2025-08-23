import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import PyPDF2 as pdf
from pdf2image import convert_from_path

# Variable to store selected file(s)
filepath = ""
filename = ""
filepaths = []
filenames = []


# Conversion functions
def toPNG():
    if not filepath:
        print("No file selected")
        messagebox.showinfo("Error", "No File Selected.")
    elif filename.split('.')[1].lower() == "pdf":
        try:
            # Convert image to PNG if PDF
            pages =  convert_from_path(filepath)
            newPath = os.path.split(filepath)[0]
            for i, page in enumerate(pages):
                page.save(f"{newPath}/page_{i + 1}.png", 'PNG')

            # File Saved Message
            browse_Treeview.delete(browse_Treeview.get_children()[0])
            browse_Treeview.configure(height=1)
            browse_Treeview.insert('', 'end', text=f"File(s) saved at {newPath}")
        except Exception as e:
            print("Error in conversion...", e)
            messagebox.showinfo("Error", "Could not Convert.")
    else:
        try:
            # Convert image to PNG
            print("Converting to PNG:", filepath)
            converted = Image.open(filepath)
            newName = "Converted-" + filename.split('.')[0]
            newPath = os.path.split(filepath)[0]
            converted.save(f"{newPath}/{newName}.png")

            # File Saved Message
            browse_Treeview.delete(browse_Treeview.get_children()[0])
            browse_Treeview.configure(height=1)
            browse_Treeview.insert('', 'end', text=f"File saved at {newPath}/{newName}.png")
        except Exception as e:
            print("Error in conversion...", e)
            messagebox.showinfo("Error", "Could not Convert.")

def toJPG():
    if not filepath:
        print("No file selected")
        messagebox.showinfo("Error", "No File Selected.")
    elif filename.split('.')[1].lower() == "pdf":
        try:
            # Convert image to JPG if PDF
            pages =  convert_from_path(filepath)
            newPath = os.path.split(filepath)[0]
            for i, page in enumerate(pages):
                page.save(f"{newPath}/page_{i + 1}.jpg", 'JPEG')

            # File Saved Message
            browse_Treeview.delete(browse_Treeview.get_children()[0])
            browse_Treeview.configure(height=1)
            browse_Treeview.insert('', 'end', text=f"File(s) saved at {newPath}")
        except Exception as e:
            print("Error in conversion...", e)
            messagebox.showinfo("Error", "Could not Convert.")
    else:
        try:
            # Convert image to JPG
            print("Converting to JPG:", filepath)
            converted = Image.open(filepath)
            converted = converted.convert("RGB")
            newName = "Converted-" + filename.split('.')[0]
            newPath = os.path.split(filepath)[0]
            converted.save(f"{newPath}/{newName}.jpg")

            # File Saved Message
            browse_Treeview.delete(browse_Treeview.get_children()[0])
            browse_Treeview.configure(height=1)
            browse_Treeview.insert('', 'end', text=f"File saved at {newPath}/{newName}.jpg")
        except Exception as e:
            print("Error in conversion...", e)
            messagebox.showinfo("Error", "Could not Convert.")

def toPDF():
    if filepath:
        try:
            # Convert image to PDF
            print("Converting to PDF:", filepath)
            converted = Image.open(filepath)
            converted = converted.convert("RGB")
            newName = "Converted-" + filename.split('.')[0]
            newPath = os.path.split(filepath)[0]
            converted.save(f"{newPath}/{newName}.pdf")

            # File Saved Message
            browse_Treeview.delete(browse_Treeview.get_children()[0])
            browse_Treeview.configure(height=1)
            browse_Treeview.insert('', 'end', text=f"File saved at {newPath}/{newName}.pdf")
        except Exception as e:
            print("Error in conversion...", e)
            messagebox.showinfo("Error", "Could not Convert.")
    else:
        print("No file selected")
        messagebox.showinfo("Error", "No File Selected.")

def combinePDFs():
    print("Combining PDFs")
    if not filepaths:
        print("No file(s) selected")
        messagebox.showinfo("Error", "No File Selected.")
        return
    merger = pdf.PdfMerger()
    for file in reversed(filepaths):
        merger.append(file)
    newPath = os.path.split(filepaths[0])[0]
    merger.write(f"{newPath}/combined.pdf")

    for row in pdf_Treeview.get_children():
        pdf_Treeview.delete(row)
    pdf_Treeview.configure(height=1)
    pdf_Treeview.insert('', 'end', text=f"File saved at {newPath}/combined.pdf")

# File browsing function
def browse_file():
    global filepath, filename
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.pdf")])
    if not filepath:
        print("No file(s) selected")
        messagebox.showinfo("Error", "No File Selected.")
        return
    browse_Treeview.item(browse_Treeview.get_children()[0], text=filepath)
    filename = os.path.split(filepath)[1]
    print(filename)

# File browsing function
def browse_files():
    global filepaths, filenames
    filepaths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if not filepaths:
        print("No file(s) selected")
        messagebox.showinfo("Error", "No File Selected.")
        return
    print(filepaths)
    pdf_Treeview.delete(pdf_Treeview.get_children()[0])
    pdf_Treeview.configure(height=len(filepaths))
    for path in filepaths:
        pdf_Treeview.insert('', 'end', text=path)
        filenames.append(os.path.split(path)[1])
    print(filenames)

# Root of GUI 
root = tk.Tk()
root.title("File Manipulator")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Image Conversions')
tabControl.grid(row=0, column=0, sticky="news")
tabControl.add(tab2, text ='PDF Merger')
tabControl.grid(row=0, column=0, sticky="news")

tab1.rowconfigure(0, weight=1)
tab1.columnconfigure(0, weight=1)

tab2.rowconfigure(0, weight=1)
tab2.columnconfigure(0, weight=1)

# Root frame scaling
root.columnconfigure(0, weight=1)

# Frame containing file finding widgets
browserFrame = ttk.Frame(tab1, padding="5")
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

##### Second Tab #####

# Frame containing file finding widgets
pdfBrowserFrame = ttk.Frame(tab2, padding="5")
pdfBrowserFrame.grid(row=0, column=0, sticky="news")

# Configure pdfBrowserFrame resizing
pdfBrowserFrame.columnconfigure(1, weight=1)

# Button to search for file
browse_Button = ttk.Button(pdfBrowserFrame, text="Browse", command= lambda: browse_files())
browse_Button.grid(row=0, column=0, sticky="e")

# Treeview to display selected file
pdf_Treeview = ttk.Treeview(pdfBrowserFrame, height=1, show='tree')
pdf_Treeview.insert('', 0, text='Select a File.')
pdf_Treeview.column('#0', width=100, stretch=True)
pdf_Treeview.grid(row=0, column=1, sticky="ew")

##### Second Tab #####

# Frame containing file conversion widgets (buttons)
convertFrame = ttk.Frame(tab1, padding="5")
convertFrame.grid(row=1, column=0, sticky="news")

# Configure convertFrame resizing
convertFrame.columnconfigure(0, weight=1)
convertFrame.columnconfigure(1, weight=1)
convertFrame.columnconfigure(2, weight=1)

##### Second Tab #####

# Frame containing file conversion widgets (buttons)
mergeFrame = ttk.Frame(tab2, padding="5")
mergeFrame.grid(row=1, column=0, sticky="news")

# Configure mergeFrame resizing
mergeFrame.columnconfigure(0, weight=1)
mergeFrame.columnconfigure(1, weight=1)
mergeFrame.columnconfigure(2, weight=1)

##### Second Tab #####

# Conversion buttons
pngButton = ttk.Button(convertFrame, text="Convert to PNG", command=toPNG)
pngButton.grid(row=0, column=0, sticky="ew")

jpgButton = ttk.Button(convertFrame, text="Convert to JPG", command=toJPG)
jpgButton.grid(row=0, column=1, sticky="ew")

pdfButton = ttk.Button(convertFrame, text="Convert to PDF", command=toPDF)
pdfButton.grid(row=0, column=2, sticky="ew")

# PDF Merge Button
mergeButton = ttk.Button(mergeFrame, text="Merge PDFs", command=combinePDFs)
mergeButton.grid(row=0, column=0, sticky="ew")

root.mainloop()
