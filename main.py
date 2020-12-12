"""
@author: Rakesh Yadav & Shivam Yadav
@task: to design UI for doc to pdf convertor.
"""
from tkinter import Tk, Label, LEFT, Frame, Button
from tkinter import messagebox
from tkinter.filedialog import askopenfile

from PIL import ImageTk
from PIL.ImageTk import PhotoImage
from docx2pdf import convert


def openfile():
    file = askopenfile(filetypes=[('Word Files', '*.docx')])
    try:
        convert(file.name)
        messagebox.showinfo("Done", "File Successfully Converted")
    except:
        messagebox.showinfo("Error", "OOPS!!!! File NOT Converted!!")


class Dashboard:
    def __init__(self, win_root):
        self.root = win_root
        self.root.title("DOC to PDF Converter")
        self.root.geometry("700x400")
        self.root.maxsize(730, 430)

        # ------------------ icon of Dashboard ----------------------#
        icon_photo = PhotoImage(file="img/logo.PNG")
        self.root.iconphoto(False, icon_photo)

        # ............... backgroundImage_labelling ..........................#
        self.bg_icon = ImageTk.PhotoImage(file="img/glass_effect.PNG")
        bg_label = Label(self.root, image=self.bg_icon)
        bg_label.pack()

        # ........... Framing_labelling of UI ....................#
        Login_frame = Frame(self.root, bg="light blue")
        Login_frame.place(x=190, y=148)
        self.user_icon = PhotoImage(file="img/doc_2_pdf.PNG")
        user_label = Label(Login_frame, text="DOC ----  PDF", image=self.user_icon, compound=LEFT,
                           font=("time new roman", 15), bg="#eee")
        user_label.grid(row=1, column=0, padx=2, pady=2)

        # ................. button_labelling ....................#
        button = Button(Login_frame, text=' Choose File: ', font=("arial", 15, "bold"), width=10, bg="blue", fg="white",
                        command=openfile)
        button.grid(row=1, column=3, padx=15, pady=2)


root = Tk()
obj = Dashboard(root)
root.mainloop()
