from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from ResetPass import ResetPass
from Register import Register
from Face_Recognition_Admin import Face_Recognition
from Face_Recognition_Teacher import FaceRecognition
import mysql.connector

class Login:
    def __init__(self, window):
        self.window = window
        self.window.geometry("925x500+0+0")
        # self.window.configure(bg="#1E329D")
        # self.window.state('zoomed')
        self.window.title("Đăng nhập")

        ########-------------VARIABLE-------------------
        self.var_pass = StringVar()
        self.var_username = StringVar()

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/bg2 (1).png")
        img = img.resize((925, 500))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=925, height=500)


        ########-------------IMAGE LOGIN-------------------
        img1 = Image.open(r"assets/image/login.png")

        img1 = img1.resize((350, 400))
        self.photoImg1 = ImageTk.PhotoImage(img1)

        login_img = ttk.Label(self.window, image=self.photoImg1, background=None)
        login_img.place(x=50, y=50)

        ########-------------MAIN_FRAME-------------------
        s = ttk.Style()
        s.configure('new.TFrame', background='white')
        self.main_frame = ttk.Frame(window, width=460, height=404, style='new.TFrame')
        self.main_frame['padding'] = (5, 10, 5, 10)
        self.main_frame.place(x=403, y=50)

        heading = Label(self.main_frame, text="Đăng nhập", font=("Poppins", 24, "bold"), bg="white", fg="#1E329D")
        heading.place(x=146, y=40)

        ########-------------USERNAME-------------------
        self.username_label = Label(self.main_frame, text='Tên đăng nhập', bg="white", font=("Poppins", 12), fg='#1E329D')
        self.username_label.place(x=98, y=100)

        self.txtUsername = ttk.Entry(self.main_frame, width=30, foreground='black', background='white', font=("Poppins", 11), textvariable=self.var_username)
        self.txtUsername.place(x=98, y=130)
        self.txtUsername.focus_set()

        # self.require_label1 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 14))
        # self.require_label1.place(x=357, y=134)

        # frame = Frame(main_frame, width=295, height=2, bg='black')
        # frame.place(x=80, y=124)

        #######-------------PASSWORD-------------------
        self.password_label = Label(self.main_frame, text='Mật khẩu', bg="white", font=("Poppins", 12), fg='#1E329D')
        self.password_label.place(x=98, y=170)

        self.txtPassword = ttk.Entry(self.main_frame, width=30, foreground='black', background='white', show='*', font=("Poppins", 11), textvariable=self.var_pass)
        self.txtPassword.place(x=98, y=200)

        # self.require_label2 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 14))
        # self.require_label2.place(x=357, y=206)

        #########-------------SHOW/HIDE PASSWORD --------
        self.show_image = Image.open('assets/image/icons8-eye-18.png')
        self.photo = ImageTk.PhotoImage(self.show_image)

        self.hide_image = Image.open('assets/image/icons8-hide-18.png')
        self.photo1 = ImageTk.PhotoImage(self.hide_image)

        self.show_button = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo
        self.show_button.place(x=329, y=205)


        ########-------------BUTTON SIGNIN-------------------
        btnLogin = Button(self.main_frame, width=23, pady=7, text="Đăng nhập", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", activeforeground="white", font=("Poppins", 11, "bold"), command=self.login)
        btnLogin.place(x=115, y=265)

        label = Label(self.main_frame, text="Bạn chưa có tài khoản?", fg='black', bg='white', font=("Poppins", 10))
        label.place(x=124, y=308)

        ########-------------BUTTON FORGOT PASSS-------------------
        btnForgot = Button(self.main_frame, width=15, text='Quên mật khẩu?', border=0, bg='white', cursor='hand2', fg='#1E329D',
                           font=("Poppins", 10), activebackground="white", activeforeground="black", command=self.resetPassword_Window)
        btnForgot.place(x=235, y=236)

        ########-------------BUTTON SIGNUP-------------------
        btnSignUp = Button(self.main_frame, width=6, text='Đăng ký', border=0, bg='white', cursor='hand2', fg='#1E329D',
                           font=("Poppins", 10), activebackground="white", activeforeground="black", command=self.register_Window)
        btnSignUp.place(x=267, y=307)

    def show(self):
        self.hide_button = Button(self.main_frame, image=self.photo1, background='white', command=self.hide, activebackground='white',
                                  cursor='hand2', bd=0)
        self.hide_button.image = self.photo1
        self.hide_button.place(x=329, y=205)
        self.txtPassword.config(show='')

    def hide(self):
        self.show_button = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo
        self.show_button.place(x=329, y=205)
        self.txtPassword.config(show='*')

    def login(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()

        if (username == "" or password == ""):
            messagebox.showerror("Error", "Vui lòng nhập Tên đăng nhập và Mật khẩu.")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Pmdnh123!",
                                           database="face_recognition")
            cursor = conn.cursor()

            cursor.execute("select * from register where username=%s and password=%s", (username, password))

            row = cursor.fetchone()

            if row != None:
                if(row[8] == "admin"):
                    messagebox.showinfo("Success", "Mời Bạn Tiến vào Giao Diện Trang Chủ của Admin")
                    self.home_Window = Toplevel(self.window)
                    self.obj = Face_Recognition(self.home_Window)
                else:
                    messagebox.showinfo("Success", "Mời Bạn Tiến vào Giao Diện Trang Chủ của Giảng viên")
                    self.home_Window = Toplevel(self.window)
                    self.obj = FaceRecognition(self.home_Window)
            else:
                messagebox.showerror("Invalid", "Bạn nhập sai Tên đăng nhập hoặc Mật khẩu")

    def resetPassword_Window(self):
        self.resetPass_Window = Toplevel(self.window)
        self.obj = ResetPass(self.resetPass_Window)

    def register_Window(self):
        self.register_Window = Toplevel(self.window)
        self.obj = Register(self.register_Window)


if __name__ == "__main__":
    root = Tk()
    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")
    obj = Login(root)
    root.mainloop()
