from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Recognition:
    def __init__(self, window):
        self.window = window
        self.window.geometry("450x250+0+0")
        # self.window.configure(bg="#1E329D")
        # self.window.state('zoomed')
        self.window.title("Nhận diện khuôn mặt")

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/bg2 (1).png")
        img = img.resize((450, 250))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=450, height=250)

        ########-------------IMAGE-------------------
        img = Image.open(r"assets/image/recognition.png")
        img = img.resize((440, 120))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = ttk.Label(self.window, image=self.photoimg)
        f_lbl.place(x=7, y=0, width=440, height=120)

        ########-------------BUTTON-------------------
        btnTrain = Button(self.window, width=23, pady=7, text="Nhận diện khuôn mặt", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", activeforeground="white", font=("Poppins", 12, "bold"))
        btnTrain.place(x=115, y=170)

if __name__ == "__main__":
    root = Tk()
    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")
    obj = Recognition(root)
    root.mainloop()