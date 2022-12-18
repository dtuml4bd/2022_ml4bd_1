from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from Student_Details_Teacher import StudentDetails
from Recognition import Recognition
from Attendance import Attendance

class FaceRecognition:
    def __init__(self, window):
        self.window = window
        self.window.geometry("870x640+0+0")
        self.window.title("Trang chủ")

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/main.png")
        img = img.resize((870, 640))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=870, height=640)

        ########-------------BUTTON 1-------------------
        img1 = Image.open(r"assets/image/thông tin sinh viên (17).png")

        img1 = img1.resize((200, 220))
        self.photoImg1 = ImageTk.PhotoImage(img1)

        self.btn_details = Button(self.window, image=self.photoImg1, activebackground='#1f3964', background='white',
                                  cursor='hand2', bd=0, command=self.student_details)
        self.btn_details.place(x=180, y=120)

        ########-------------BUTTON 2-------------------
        img2 = Image.open(r"assets/image/thông tin sinh viên (8).png")

        img2 = img2.resize((200, 220))
        self.photoImg2 = ImageTk.PhotoImage(img2)

        self.btn_faceDetect = Button(self.window, image=self.photoImg2, activebackground='#1f3964', background='white',
                                     cursor='hand2', bd=0, command=self.face_recognition)
        self.btn_faceDetect.place(x=470, y=120)

        ########-------------BUTTON 3-------------------
        img3 = Image.open(r"assets/image/thông tin sinh viên (11).png")

        img3 = img3.resize((200, 220))
        self.photoImg3 = ImageTk.PhotoImage(img3)

        self.btn_attendance = Button(self.window, image=self.photoImg3, activebackground='#1f3964', background='white',
                                     cursor='hand2', bd=0, command=self.attendance)
        self.btn_attendance.place(x=180, y=380)

        ########-------------BUTTON 4------------------
        img8 = Image.open(r"assets/image/thông tin sinh viên (16).png")

        img8 = img8.resize((200, 220))
        self.photoImg8 = ImageTk.PhotoImage(img8)

        self.btn_exit = Button(self.window, image=self.photoImg8, activebackground='#1f3964', background='white',
                               cursor='hand2', bd=0)
        self.btn_exit.place(x=470, y=380)

    def student_details(self):
        self.student_window = Toplevel(self.window)
        self.obj = StudentDetails(self.student_window)

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
    obj = FaceRecognition(root)
    root.mainloop()