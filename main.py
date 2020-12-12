from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile

from PIL import ImageTk
from PIL.ImageTk import PhotoImage
from docx2pdf import convert


def openfile():
    file = askopenfile(filetypes=[('Word Files', '*.docx')])
    # convert(file)
    convert(file.name, "output.pdf")
    # convert(file.name)
    messagebox.showinfo("Done", "File Successfully Converted")


class LoginDashboard:

    def __init__(self, win_root):
        self.root = win_root
        self.root.title("Word To PDF Converter")
        self.root.geometry("700x400")
        self.root.maxsize(730, 430)
        # self.root.minsize(400, 200)

        # ------------------ icon of LogIn Dashboard ----------------------#
        icon_photo = PhotoImage(file="logo.PNG")
        self.root.iconphoto(False, icon_photo)

        self.bg_icon = ImageTk.PhotoImage(file="glass_effect.PNG")
        self.user_icon = PhotoImage(file="doc_2_pdf.PNG")

        # ............... background-image labelling ..........................#
        bg_label = Label(self.root, image=self.bg_icon)
        bg_label.pack()

        Login_frame = Frame(self.root, bg="light blue")
        Login_frame.place(x=190, y=148)

        # ........... Username -  image_icon + entry_field Labelling ....................#
        user_label = Label(Login_frame, text="DOCx --->  PDF", image=self.user_icon, compound=LEFT,
                           font=("time new roman", 15), bg="#eee")
        user_label.grid(row=1, column=0, padx=2, pady=2)

        # ................. button-labelling ....................#
        button = Button(Login_frame, text=' Choose File: ', font=("arial", 15, "bold"), width=10, bg="blue", fg="red",
                        command=openfile)
        button.grid(row=1, column=3, padx=15, pady=2)


root = Tk()
obj = LoginDashboard(root)
root.mainloop()
