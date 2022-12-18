from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from Student_Details_Admin import Student_Details
from Train import Train
from Recognition import Recognition
from Attendance import Attendance
import mysql.connector

class Face_Recognition:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x740+0+0")
        # self.window.configure(bg="#1E329D")
        # self.window.state('zoomed')
        self.window.title("Trang chủ")

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/main.png")
        img = img.resize((1366, 740))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=1366, height=740)

        ########-------------BUTTON 1-------------------
        img1 = Image.open(r"assets/image/thông tin sinh viên (17).png")

        img1 = img1.resize((200, 220))
        self.photoImg1 = ImageTk.PhotoImage(img1)

        self.btn_details = Button(self.window, image=self.photoImg1, activebackground='#1f3964', background='white',
                                  cursor='hand2', bd=0, command=self.student_details)
        self.btn_details.place(x=130, y=140)

        ########-------------BUTTON 2-------------------
        img2 = Image.open(r"assets/image/thông tin sinh viên (8).png")

        img2 = img2.resize((200, 220))
        self.photoImg2 = ImageTk.PhotoImage(img2)

        self.btn_faceDetect = Button(self.window, image=self.photoImg2, activebackground='#1f3964', background='white',
                                  cursor='hand2', bd=0, command=self.face_recognition)
        self.btn_faceDetect.place(x=430, y=140)

        ########-------------BUTTON 3-------------------
        img3 = Image.open(r"assets/image/thông tin sinh viên (11).png")

        img3 = img3.resize((200, 220))
        self.photoImg3 = ImageTk.PhotoImage(img3)

        self.btn_attendance = Button(self.window, image=self.photoImg3, activebackground='#1f3964', background='white',
                                  cursor='hand2', bd=0, command=self.attendance)
        self.btn_attendance.place(x=730, y=140)

        ########-------------BUTTON 4-------------------
        img4 = Image.open(r"assets/image/thông tin sinh viên (12).png")

        img4 = img4.resize((200, 220))
        self.photoImg4 = ImageTk.PhotoImage(img4)

        self.btn_help = Button(self.window, image=self.photoImg4, activebackground='#1f3964', background='white',
                                  cursor='hand2', bd=0)
        self.btn_help.place(x=1030, y=140)

        ########-------------BUTTON 5------------------
        img5 = Image.open(r"assets/image/thông tin sinh viên (13).png")

        img5 = img5.resize((200, 220))
        self.photoImg5 = ImageTk.PhotoImage(img5)

        self.btn_train = Button(self.window, image=self.photoImg5, activebackground='#1f3964', background='white',
                               cursor='hand2', bd=0, command=self.train_data)
        self.btn_train.place(x=130, y=450)

        ########-------------BUTTON 6------------------
        img6 = Image.open(r"assets/image/thông tin sinh viên (14).png")

        img6 = img6.resize((200, 220))
        self.photoImg6 = ImageTk.PhotoImage(img6)

        self.btn_images = Button(self.window, image=self.photoImg6, activebackground='#1f3964', background='white',
                                cursor='hand2', bd=0)
        self.btn_images.place(x=430, y=450)

        ########-------------BUTTON 7------------------
        img7 = Image.open(r"assets/image/thông tin sinh viên (15).png")

        img7 = img7.resize((200, 220))
        self.photoImg7 = ImageTk.PhotoImage(img7)

        self.btn_development = Button(self.window, image=self.photoImg7, activebackground='#1f3964', background='white',
                                 cursor='hand2', bd=0)
        self.btn_development.place(x=730, y=450)

        ########-------------BUTTON 8------------------
        img8 = Image.open(r"assets/image/thông tin sinh viên (16).png")

        img8 = img8.resize((200, 220))
        self.photoImg8 = ImageTk.PhotoImage(img8)

        self.btn_exit = Button(self.window, image=self.photoImg8, activebackground='#1f3964', background='white',
                                      cursor='hand2', bd=0)
        self.btn_exit.place(x=1030, y=450)

    def student_details(self):
        self.student_window = Toplevel(self.window)
        self.obj = Student_Details(self.student_window)

    def train_data(self):
        self.student_window = Toplevel(self.window)
        self.obj = Train(self.student_window)

    def face_recognition(self):
        self.student_window = Toplevel(self.window)
        self.obj = Recognition(self.student_window)

    def attendance(self):
        self.attendance_window = Toplevel(self.window)
        self.obj = Attendance(self.attendance_window)

if __name__ == "__main__":
    root = Tk()
    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")
    obj = Face_Recognition(root)
    root.mainloop()