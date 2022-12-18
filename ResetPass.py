from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class ResetPass:
    def __init__(self, window):
        self.window = window
        self.window.geometry("800x490+0+0")
        # self.window.configure(bg="#1E329D")
        # self.window.state('zoomed')
        self.window.title("Đổi mật khẩu")

        ########-------------VARIABLE-------------------
        self.var_sercurity_Q = StringVar()
        self.var_security_A = StringVar()
        self.var_pass = StringVar()
        self.var_username = StringVar()

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/bg2 (1).png")
        img = img.resize((820, 490))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=820, height=490)

        ########-------------IMAGE RESET-------------------
        img1 = Image.open(r"assets/image/reset.png")

        img1 = img1.resize((330, 420))
        self.photoImg1 = ImageTk.PhotoImage(img1)

        login_img = ttk.Label(self.window, image=self.photoImg1, background=None)
        login_img.place(x=39, y=32)

        ########-------------MAIN_FRAME-------------------
        s = ttk.Style()
        s.configure('new.TFrame', background='white')
        self.main_frame = ttk.Frame(window, width=400, height=424, style='new.TFrame')
        self.main_frame['padding'] = (5, 8, 5, 8)
        self.main_frame.place(x=373, y=32)

        heading = Label(self.main_frame, text="Đổi mật khẩu", font=("Poppins", 24, "bold"), bg="white", fg="#1E329D")
        heading.place(x=87, y=20)

        ########-------------USERNAME-------------------
        self.username_label = Label(self.main_frame, text='Tên đăng nhập', bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        self.username_label.place(x=65, y=70)

        self.txtUsername = ttk.Entry(self.main_frame, width=28, foreground='black', background='white',
                                     font=("Poppins", 11), textvariable=self.var_username)
        self.txtUsername.place(x=66, y=100)
        self.txtUsername.focus_set()

        require_label1 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 14))
        require_label1.place(x=310, y=106)

        ########-------------SECURITY QUESTIONS-------------------
        security_Question_lbl = Label(self.main_frame, text="Câu hỏi bảo mật", bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        security_Question_lbl.place(x=65, y=140)

        self.combobox_security_Question = ttk.Combobox(self.main_frame, foreground='black', background='white',
                                     font=("Poppins", 11), textvariable=self.var_sercurity_Q)
        self.combobox_security_Question["values"] = (
            "Chọn câu hỏi", "Nơi sinh của bạn?", "Tên bạn thân nhất của bạn?", "Tên thú cưng của bạn?")
        self.combobox_security_Question.place(x=66, y=170, width=240, height=32)
        self.combobox_security_Question.current(0)

        require_label3 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 14))
        require_label3.place(x=310, y=176)

        ########-------------SECURITY ANSWER-------------------
        security_Answer_lbl = Label(self.main_frame, text="Câu trả lời", bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        security_Answer_lbl.place(x=65, y=210)

        self.txtSecurity_Answer = ttk.Entry(self.main_frame, width=28, foreground='black', background='white',
                                     font=("Poppins", 11), textvariable=self.var_security_A)
        self.txtSecurity_Answer.place(x=66, y=240)

        require_label2 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 14))
        require_label2.place(x=310, y=247)

        ########-------------NEW PASSWORD-------------------
        newPassword_lbl = Label(self.main_frame, text="Mật khẩu mới", bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        newPassword_lbl.place(x=65, y=280)

        self.txtNewPassword = ttk.Entry(self.main_frame, width=28, foreground='black', background='white',
                                     font=("Poppins", 11), show='*', textvariable=self.var_pass)
        self.txtNewPassword.place(x=66, y=310)

        require_label3 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 14))
        require_label3.place(x=310, y=315)

        #########-------------SHOW/HIDE PASSWORD --------
        self.show_image = Image.open('assets/image/icons8-eye-18.png')
        self.photo = ImageTk.PhotoImage(self.show_image)

        self.hide_image = Image.open('assets/image/icons8-hide-18.png')
        self.photo1 = ImageTk.PhotoImage(self.hide_image)

        self.show_button = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo
        self.show_button.place(x=282, y=315)

        ########-------------BUTTON RESET-------------------
        btnReset = Button(self.main_frame, width=19, pady=7, text="Đổi mật khẩu", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", activeforeground="white", font=("Poppins", 11, "bold"), command=self.reset_password)
        btnReset.place(x=97, y=355)

    def show(self):
        self.hide_button = Button(self.main_frame, image=self.photo1, background='white', command=self.hide,
                                      activebackground='white',
                                      cursor='hand2', bd=0)
        self.hide_button.image = self.photo1
        self.hide_button.place(x=282, y=315)
        self.txtNewPassword.config(show='')

    def hide(self):
        self.show_button = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                      cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo
        self.show_button.place(x=282, y=315)
        self.txtNewPassword.config(show='*')

    def reset_password(self):
        if self.txtUsername.get() == "":
            messagebox.showerror("Error", "Vui lòng Nhập tên đăng nhập!")
        elif self.combobox_security_Question.get() == "Chọn câu hỏi":
            messagebox.showerror("Error", "Vui lòng Chọn câu hỏi bảo mật!")
        elif self.txtSecurity_Answer.get() == "":
            messagebox.showerror("Error", "Vui lòng Nhập câu trả lời!")
        elif self.txtNewPassword.get() == "":
            messagebox.showerror("Error", "Vui lòng Nhập mật khẩu mới!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Pmdnh123!",
                                           database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("select * from register where username=%s and securityQ=%s and securityA=%s",
                           (self.txtUsername.get(),
                            self.combobox_security_Question.get(), self.txtSecurity_Answer.get()
                            ))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Vui lòng Nhập thông tin đúng!")
            else:
                cursor.execute("update register set password=%s where username=%s",
                               (self.txtNewPassword.get(), self.txtUsername.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success",
                                    "Bạn đã thay đổi mật khẩu thành công. Vui lòng tiến hành đăng nhập với mật khẩu mới.")
                self.window.destroy()
if __name__ == "__main__":
    root = Tk()
    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")
    obj = ResetPass(root)
    root.mainloop()