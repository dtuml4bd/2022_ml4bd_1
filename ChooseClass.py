from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from ResetPass import ResetPass
from Register import Register
from Face_Recognition_Admin import Face_Recognition
import mysql.connector

class ChooseClass:
    def __init__(self, window):
        self.window = window
        self.window.geometry("450x250+0+0")
        self.window.title("Chọn lớp")

        ########-------------VARIABLE-------------------
        self.var_class = StringVar()

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/chooseclass.png")
        img = img.resize((450, 250))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=450, height=250)

        ########-------------COMBOBOX-------------------
        self.combobox_class = ttk.Combobox(self.window, foreground='black', background='white',
                                                       font=("Poppins", 12), textvariable=self.var_class)
        self.combobox_class["values"] = ("Chọn lớp","CS 221 E", "CS 221 A", "CS 221 Q")
        self.combobox_class.place(x=127, y=90, width=207, height=32)
        self.combobox_class.current(0)

        ########-------------BUTTON-------------------
        btnConfirm = Button(self.window, width=17, pady=6, text="Xác nhận", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", activeforeground="white", font=("Poppins", 12, "bold"))
        btnConfirm.place(x=139, y=165)

if __name__ == "__main__":
    root = Tk()
    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")
    obj = ChooseClass(root)
    root.mainloop()