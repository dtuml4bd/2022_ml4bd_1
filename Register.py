from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, window):
        self.window = window
        self.window.geometry("925x555+0+0")
        # self.window.configure(bg="#1E329D")
        # self.window.state('zoomed')
        self.window.title("Đăng ký")

        ########-------------VARIABLE-------------------
        self.var_firstname = StringVar()
        self.var_lastname = StringVar()
        self.var_sercurity_Q = StringVar()
        self.var_security_A = StringVar()
        self.var_email = StringVar()
        self.var_contactNo = StringVar()
        self.var_pass = StringVar()
        self.var_confirm_pass = StringVar()
        self.var_username = StringVar()

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/bg2 (1).png")
        img = img.resize((925, 555))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=925, height=555)

        ########-------------IMAGE REGISTER-------------------
        img1 = Image.open(r"assets/image/register.png")

        img1 = img1.resize((280, 506))
        self.photoImg1 = ImageTk.PhotoImage(img1)

        login_img = ttk.Label(self.window, image=self.photoImg1, background=None)
        login_img.place(x=50, y=22)

        ########-------------MAIN_FRAME-------------------
        s = ttk.Style()
        s.configure('new.TFrame', background='white')
        self.main_frame = ttk.Frame(window, width=540, height=510, style='new.TFrame')
        self.main_frame['padding'] = (3, 4, 3, 4)
        self.main_frame.place(x=334, y=22)

        heading = Label(self.main_frame, text="Đăng ký", font=("Poppins", 24, "bold"), bg="white", fg="#1E329D")
        heading.place(x=197, y=17)

        ########-------------ROW 1-------------------
        #-----------Last Name----------
        lastname_label = Label(self.main_frame, text='Họ', bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        lastname_label.place(x=45, y=63)

        self.txtLastName = ttk.Entry(self.main_frame, width=24, foreground='black', background='white',
                                     font=("Poppins", 11), textvariable=self.var_lastname)
        self.txtLastName.place(x=45, y=93)
        self.txtLastName.focus_set()

        require_label1 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label1.place(x=255, y=101)

        # -----------First Name----------
        firstname_label = Label(self.main_frame, text='Tên', bg="white", font=("Poppins", 12),
                               fg='#1E329D')
        firstname_label.place(x=286, y=63)

        self.txtFirstName = ttk.Entry(self.main_frame, width=24, foreground='black', background='white',
                                     font=("Poppins", 11), textvariable=self.var_firstname)
        self.txtFirstName.place(x=286, y=93)

        require_label2 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label2.place(x=495, y=101)

        ########-------------ROW 2-------------------
        # -----------Contact----------
        contact_lbl = Label(self.main_frame, text='Số điện thoại', bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        contact_lbl.place(x=45, y=133)

        self.txtContact = ttk.Entry(self.main_frame, width=24, foreground='black', background='white',
                                     font=("Poppins", 11), textvariable=self.var_contactNo)
        self.txtContact.place(x=45, y=163)

        require_label3 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label3.place(x=255, y=171)

        # -----------Email----------
        email_lbl = Label(self.main_frame, text='Email', bg="white", font=("Poppins", 12),
                            fg='#1E329D')
        email_lbl.place(x=286, y=133)

        self.txtEmail = ttk.Entry(self.main_frame, width=24, foreground='black', background='white',
                                    font=("Poppins", 11), textvariable=self.var_email)
        self.txtEmail.place(x=286, y=163)

        require_label4 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label4.place(x=495, y=171)

        ########-------------ROW 3-------------------
        # -----------Security Question----------
        security_Question_lbl = Label(self.main_frame, text="Câu hỏi bảo mật", bg="white", font=("Poppins", 12),
                                      fg='#1E329D')
        security_Question_lbl.place(x=45, y=203)

        self.combobox_security_Question = ttk.Combobox(self.main_frame, foreground='black', background='white',
                                                      font=("Poppins", 11), textvariable=self.var_sercurity_Q)
        self.combobox_security_Question["values"] = (
            "Chọn câu hỏi", "Nơi sinh của bạn?", "Tên bạn thân nhất của bạn?", "Tên thú cưng của bạn?")
        self.combobox_security_Question.place(x=45, y=233, width=207, height=32)
        self.combobox_security_Question.current(0)

        require_label5 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label5.place(x=255, y=241)

        # -----------Security Answer----------
        security_Answer_lbl = Label(self.main_frame, text="Câu trả lời", bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        security_Answer_lbl.place(x=286, y=203)

        self.txtSecurity_Answer = ttk.Entry(self.main_frame, width=24, foreground='black', background='white',
                                            font=("Poppins", 11), textvariable=self.var_security_A)
        self.txtSecurity_Answer.place(x=286, y=233)

        require_label6 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label6.place(x=495, y=241)

        ########-------------ROW 3-------------------
        # -----------USERNAME----------
        username_label = Label(self.main_frame, text='Tên đăng nhập', bg="white", font=("Poppins", 12),
                                    fg='#1E329D')
        username_label.place(x=45, y=273)

        self.txtUsername = ttk.Entry(self.main_frame, width=24, foreground='black', background='white',
                                     font=("Poppins", 11), textvariable=self.var_username)
        self.txtUsername.place(x=45, y=303)

        require_label7 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label7.place(x=255, y=311)

        # -----------PASSWORD----------
        password_label = Label(self.main_frame, text='Mật khẩu', bg="white", font=("Poppins", 12), fg='#1E329D')
        password_label.place(x=286, y=273)

        self.txtPassword = ttk.Entry(self.main_frame, width=24, foreground='black', background='white', show='*',
                                     font=("Poppins", 11), textvariable=self.var_pass)
        self.txtPassword.place(x=286, y=303)

        require_label8 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label8.place(x=495, y=311)

        ########-------------ROW 3-------------------
        # -----------CONFIRM PASSWORD----------
        confirmpass_label = Label(self.main_frame, text='Xác nhận mật khẩu', bg="white", font=("Poppins", 12), fg='#1E329D')
        confirmpass_label.place(x=286, y=343)

        self.txtConfirmPass = ttk.Entry(self.main_frame, width=24, foreground='black', background='white', show='*',
                                     font=("Poppins", 11), textvariable=self.var_confirm_pass)
        self.txtConfirmPass.place(x=286, y=373)

        require_label9 = Label(self.main_frame, text='*', fg='red', background='white', font=("Poppins", 13))
        require_label9.place(x=495, y=381)

        # -----------CHECK BUTTON ----------------
        self.var_check = IntVar()
        self.check_btn = Checkbutton(self.main_frame, variable=self.var_check,
                                     text="Tôi đồng ý Điều khoản & Điều kiện.",
                                     font=("Poppins", 10), onvalue=1, offvalue=0, fg="#1E329D", bg="white")
        self.check_btn.place(x=42, y=405)

        ########-------------BUTTON SIGNUP-------------------
        self.btnSignUp = Button(self.main_frame, width=23, pady=7, text="Đăng ký", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", activeforeground="white", font=("Poppins", 11, "bold"), command=self.register_data)
        self.btnSignUp.place(x=162, y=440)

        #########-------------SHOW/HIDE PASSWORD --------
        self.show_image = Image.open('assets/image/icons8-eye-18.png')
        self.photo = ImageTk.PhotoImage(self.show_image)

        self.hide_image = Image.open('assets/image/icons8-hide-18.png')
        self.photo1 = ImageTk.PhotoImage(self.hide_image)

        self.show_button = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.showPass)
        self.show_button.image = self.photo
        self.show_button.place(x=471, y=310)

        #########-------------SHOW/HIDE CONFITM PASSWORD --------
        self.show_buttonConfirm = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.showConfirm)
        self.show_buttonConfirm.image = self.photo
        self.show_buttonConfirm.place(x=471, y=381)

    def showPass(self):
        self.hide_button = Button(self.main_frame, image=self.photo1, background='white', command=self.hidePass,
                                      activebackground='white',
                                      cursor='hand2', bd=0)
        self.hide_button.image = self.photo1
        self.hide_button.place(x=471, y=310)
        self.txtPassword.config(show='')

    def hidePass(self):
        self.show_button = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                      cursor='hand2', bd=0, command=self.showPass)
        self.show_button.image = self.photo
        self.show_button.place(x=471, y=310)
        self.txtPassword.config(show='*')

    def showConfirm(self):
        self.hide_button = Button(self.main_frame, image=self.photo1, background='white', command=self.hideConfirm,
                                      activebackground='white',
                                      cursor='hand2', bd=0)
        self.hide_button.image = self.photo1
        self.hide_button.place(x=471, y=381)
        self.txtConfirmPass.config(show='')

    def hideConfirm(self):
        self.show_button = Button(self.main_frame, image=self.photo, background='white', activebackground='white',
                                      cursor='hand2', bd=0, command=self.showConfirm)
        self.show_button.image = self.photo
        self.show_button.place(x=471, y=381)
        self.txtConfirmPass.config(show='*')

    def register_data(self):
        if self.var_firstname.get() == "" or self.var_email.get() == "" or self.var_sercurity_Q.get() == "Chọn câu hỏi":
            messagebox.showerror("Error", "Bạn phải nhập đầy đủ dữ liệu.", parent=self.window)
        elif self.var_pass.get() != self.var_confirm_pass.get():
            messagebox.showerror("Error", "Mật khẩu và xác nhận mật khẩu phải trùng nhau.", parent=self.window)
        elif self.var_check.get() == 0:
            messagebox.showerror('Error', "Bạn chưa xác nhận Điều khoản & Điều kiện", parent=self.window)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Pmdnh123!",
                                           database="face_recognition")
            cursor = conn.cursor()

            cursor.execute("select * from register where email=%s", (self.var_email.get(),))
            row = cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Email đã tồn tại. Vui lòng chọn Email khác!")
            else:
                cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_firstname.get(),
                    self.var_lastname.get(),
                    self.var_contactNo.get(),
                    self.var_email.get(),
                    self.var_sercurity_Q.get(),
                    self.var_security_A.get(),
                    self.var_username.get(),
                    self.var_pass.get(),
                    "user"
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success", "Bạn đã đăng ký tài khoản thành công.")
                self.window.destroy()


if __name__ == "__main__":
    root = Tk()

    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")

    obj = Register(root)
    root.mainloop()