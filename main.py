import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from docx2pdf import convert

win = tk.Tk()
win.title("Word To PDF Converter")


def openfile():
    file = askopenfile(filetypes=[('Word Files', '*.docx')])
    print(file)
    convert(file.name)
    showinfo("Done", "File Successfully Converted")


label = tk.Label(win, text='Choose File: ')
label.grid(row=0, column=0, padx=5, pady=5)

button = ttk.Button(win, text='Select', width=30, command=openfile)
button.grid(row=0, column=1, padx=5, pady=5)

win.mainloop()
