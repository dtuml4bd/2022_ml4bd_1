from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


class StudentDetails:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1196x630+0+0")
        self.window.title("Quản lý sinh viên")

        # =================variables==============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        self.var_search_type = StringVar()
        self.var_search_value = StringVar()

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/bg2 (1).png")
        img = img.resize((1196, 630))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=1196, height=630)

        ########-------------MAIN_FRAME-------------------
        main_frame = ttk.Frame(bg_img)
        main_frame.place(x=25, y=45, width=1145, height=550)

        ########-------------LEFT_FRAME-------------------
        left_frame = ttk.Labelframe(main_frame, text="Thông tin sinh viên")
        left_frame.place(x=10, y=10, width=578, height=530)

        ########-------------STUDENT_DETAILS-------------------
        img_left = Image.open(r"assets/image/left_img.jpg")
        img_left = img_left.resize((578, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = ttk.Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=568, height=130)

        # ---- Current course information
        current_course_frame = ttk.Labelframe(left_frame, text="Thông tin môn học")
        current_course_frame.place(x=5, y=135, width=565, height=122)

        # Department
        department_label = ttk.Label(current_course_frame, text="Ngành:")
        department_label.grid(row=0, column=0, padx=10, sticky=W)

        department_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, foreground='black',
                                        background='white', width=17, state="readonly")
        department_combo["values"] = ("Chọn ngành", "Computer", "IT", "Mechnical")
        department_combo.current(0)
        department_combo.grid(row=0, column=1, padx=5, pady=10, ipadx=20, sticky=W)

        # Course
        course_label = ttk.Label(current_course_frame, text="Khoá học:")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, width=17, state="readonly")
        course_combo["values"] = ("Chọn khóa học", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=10, ipadx=23, sticky=W)

        # year
        year_label = ttk.Label(current_course_frame, text="Năm học:")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, width=17, state="readonly")
        year_combo["values"] = ("Chọn năm học", "2020 - 2021", "2021 - 2022", "2022 - 2023")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, ipadx=20, sticky=W)

        # Semester
        semester_label = ttk.Label(current_course_frame, text="Học kì:")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, width=17, state="readonly")
        semester_combo["values"] = ("Chọn học kì", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=10, ipadx=23, sticky=W)

        # Class students information
        class_student_frame = ttk.Labelframe(left_frame, text="Thông tin Sinh viên")
        class_student_frame.place(x=5, y=260, width=565, height=245)

        # Student ID
        studentId_label = ttk.Label(class_student_frame, text="Mã Sinh viên")
        studentId_label.grid(row=0, column=0, padx=5, sticky=W)

        self.studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20)
        self.studentID_entry.grid(row=0, column=1, padx=3, ipadx=5, sticky=W)
        self.studentID_entry.focus_set()

        # Student name
        studentName_label = ttk.Label(class_student_frame, text="Họ tên")
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20)
        self.studentName_entry.grid(row=0, column=2, padx=93, ipadx=5, sticky=W)

        # Class didvision
        class_div_label = ttk.Label(class_student_frame, text="Phân lớp")
        class_div_label.grid(row=1, column=0, padx=3, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, width=19, state="readonly")
        div_combo["values"] = ("Chọn phân lớp", "CS 221 E", "CS 221 A", "CS 221 Q")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=2, pady=7, ipadx=8, sticky=W)

        # Roll No
        roll_no_label = ttk.Label(class_student_frame, text="Số phòng")
        roll_no_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20)
        roll_no_entry.grid(row=1, column=2, padx=93, ipadx=5, sticky=W)

        # Gender
        gender_label = ttk.Label(class_student_frame, text="Giới tính")
        gender_label.grid(row=2, column=0, padx=3, pady=5, sticky=W)

        self.gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, width=19, state="readonly")
        self.gender_combo["values"] = ("Chọn giới tính", "Nam", "Nữ", "Khác")
        self.gender_combo.current(0)
        self.gender_combo.grid(row=2, column=1, padx=2, pady=7, ipadx=8, sticky=W)

        # DOB
        dob_label = ttk.Label(class_student_frame, text="Ngày sinh")
        dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20)
        self.dob_entry.grid(row=2, column=2, padx=93, ipadx=5, sticky=W)

        # Email
        email_label = ttk.Label(class_student_frame, text="Email")
        email_label.grid(row=3, column=0, padx=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20)
        email_entry.grid(row=3, column=1, padx=3, ipadx=5, sticky=W)

        # Phone
        phone_no_label = ttk.Label(class_student_frame, text="Số điện thoại")
        phone_no_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20)
        phone_no_entry.grid(row=3, column=2, padx=93, ipadx=5, sticky=W)

        # Address
        address_label = ttk.Label(class_student_frame, text="Địa chỉ")
        address_label.grid(row=4, column=0, padx=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20)
        address_entry.grid(row=4, column=1, padx=5, pady=5, ipadx=4, sticky=W)

        # Teacher name
        teacher_name_label = ttk.Label(class_student_frame, text="Giảng viên")
        teacher_name_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20)
        teacher_name_entry.grid(row=4, column=2, padx=93, ipadx=5, sticky=W)

        # # Radio Buttom
        # self.var_radio1 = StringVar()
        # radionbtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Chụp ảnh mẫu", value="yes")
        # radionbtn1.grid(row=6, column=0, sticky=W)
        #
        # radionbtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Không chụp ảnh mẫu",
        #                              value="no")
        # radionbtn2.grid(row=6, column=1, sticky=W)
        #
        # take_photo_btn = Button(class_student_frame, width=13, pady=3, text="Take photos", bg='#e6c511', cursor='hand2',
        #                         fg='white',
        #                         border=0, activebackground="#1E329D", activeforeground="white",
        #                         font=("Poppins", 10, "bold"), command=self.Generate_dataset)
        # take_photo_btn.grid(row=6, column=2, sticky=W)
        #
        # update_photo_btn = Button(class_student_frame, width=13, pady=3, text="Upload photo", bg='#e6c511',
        #                           cursor='hand2', fg='white',
        #                           border=0, activebackground="#1E329D", activeforeground="white",
        #                           font=("Poppins", 10, "bold"))
        # update_photo_btn.grid(row=6, column=2, padx=4)

        # Buttom frame
        # btn_frame = ttk.Frame(class_student_frame, border=5)
        # btn_frame.place(x=0, y=255, width=530, height=40)
        #
        # save_btn = Button(btn_frame, width=15, pady=7, text="Lưu", bg='#e6c511', cursor='hand2', fg='white',
        #                   border=0, activebackground="#1E329D", activeforeground="white", font=("Poppins", 10, "bold"),
        #                   command=self.add_data)
        # save_btn.grid(row=0, column=0, padx=4)
        #
        # update_btn = Button(btn_frame, width=15, pady=7, text="Cập nhật", bg='#e6c511', cursor='hand2', fg='white',
        #                     border=0, activebackground="#1E329D", activeforeground="white",
        #                     font=("Poppins", 10, "bold"), command=self.update_data)
        # update_btn.grid(row=0, column=1, padx=4)
        #
        # delete_btn = Button(btn_frame, width=15, pady=7, text="Xóa", bg='#e6c511', cursor='hand2', fg='white',
        #                     border=0, activebackground="#1E329D", activeforeground="white",
        #                     font=("Poppins", 10, "bold"), command=self.delete_data)
        # delete_btn.grid(row=0, column=2, padx=4)
        #
        # reset_btn = Button(btn_frame, width=15, pady=7, text="Làm mới", bg='#e6c511', cursor='hand2', fg='white',
        #                    border=0, activebackground="#1E329D", activeforeground="white", font=("Poppins", 10, "bold"),
        #                    command=self.reset_data)
        # reset_btn.grid(row=0, column=3, padx=4)

        ########-------------RIGHT_FRAME-------------------
        right_frame = ttk.LabelFrame(main_frame, text="Danh sách sinh viên")
        right_frame.place(x=590, y=10, width=546, height=530)

        ########-------------ATTENDANCE_DETAILS-------------------
        img_right = Image.open(r"assets/image/right-img.jpg")
        img_right = img_right.resize((578, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = ttk.Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=3, y=0, width=535, height=130)

        # ============== SEARCH ====================
        search_frame = ttk.Labelframe(right_frame, text="Tìm kiếm thông tin")
        search_frame.place(x=5, y=135, width=534, height=80)

        search_label = ttk.Label(search_frame, text="Tìm theo:", border=3)
        search_label.grid(row=0, column=0, padx=7, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, width=13, state="readonly", textvariable=self.var_search_type)
        search_combo["values"] = ("Chọn", "Mã môn", "Số điện thoại", "Mã sinh viên")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=10, ipadx=2, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, textvariable=self.var_search_value)
        search_entry.grid(row=0, column=2, padx=5, pady=5, ipadx=10, sticky=W)

        search_btn = Button(search_frame, width=8, pady=2, text="Tìm kiếm", bg='#e6c511', cursor='hand2', fg='white',
                            border=0, activebackground="#1E329D", activeforeground="white",
                            font=("Poppins", 10, "bold"), command=self.search_data)
        search_btn.grid(row=0, column=3, padx=3)

        showAll_btn = Button(search_frame, width=12, pady=2, text="Hiển thị tất cả", bg='#e6c511', cursor='hand2',
                             fg='white',
                             border=0, activebackground="#1E329D", activeforeground="white",
                             font=("Poppins", 10, "bold"), command=self.fetch_data)
        showAll_btn.grid(row=0, column=4, padx=3)

        # ====================Table Frame====================
        table_frame = ttk.Frame(right_frame, border=5)
        table_frame.place(x=5, y=230, width=535, height=279)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "course", "department", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email",
            "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("course", text="Khóa học")
        self.student_table.heading("department", text="Ngành")
        self.student_table.heading("year", text="Niên khóa")
        self.student_table.heading("sem", text="Học kỳ")
        self.student_table.heading("id", text="Mã Sinh viên")
        self.student_table.heading("name", text="Tên sinh viên")
        self.student_table.heading("div", text="Phân lớp")
        self.student_table.heading("roll", text="Mã môn")
        self.student_table.heading("gender", text="Giới tính")
        self.student_table.heading("dob", text="Ngày sinh")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Số điện thoại")
        self.student_table.heading("address", text="Địa chỉ")
        self.student_table.heading("teacher", text="Giảng viên")
        self.student_table.heading("photo", text="Hình ảnh")
        self.student_table["show"] = "headings"

        self.student_table.column("course", width=100)
        self.student_table.column("department", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_content)
        self.fetch_data()

        conn = mysql.connector.connect(host="localhost", username="root", password="Pmdnh123!",
                                       database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")

        myresult = my_cursor.fetchall()
        id = 0;
        for i in myresult:
            id += 1
        id += 1
        self.var_std_id.set(id)

    def add_data(self):

        if self.var_dep.get() == "Chọn ngành" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "Tất cả các trường không được để trống.", parent=self.window)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Pmdnh123!",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_course.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    "null"
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Sinh viên đã được thêm thành công!", parent=self.window)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.window)

    # ============ Fetch data =================
    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='Pmdnh123!',
                                       host='localhost',
                                       database='face_recognition')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ========================get cursor=====================
    def get_content(self, event=""):
        index = self.student_table.focus()
        content = self.student_table.item(index)
        data = content["values"]
        self.var_dep.set(data[1])
        self.var_course.set(data[0])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        # self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_dep.get() == "Chọn ngành" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Tất cả các trường không được để trống.", parent=self.root)
        else:
            try:
                answer = messagebox.askyesno("Update", "Bạn có muốn cập nhật dữ liệu không?")
                if answer > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Pmdnh123!",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set course=%s, department=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s where Student_id=%s ",
                        (
                            self.var_course.get(),
                            self.var_dep.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_std_id.get()
                        ))
                else:
                    if not answer:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Dữ liệu đã được cập nhật thành công!", parent=self.window)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.window)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Mã sinh viên không được để trống.", parent=self.window)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Bạn có muốn xoá dữ liệu này không?")
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Pmdnh123!",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from student where Student_id=%s", (self.var_std_id.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Dữ liệu đã được xoá thành công", parent=self.window)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.window)

    def reset_data(self):
        self.var_course.set("Chọn khóa học"),
        self.var_dep.set("Chọn nghành"),
        self.var_year.set("Chọn năm học"),
        self.var_semester.set("Chọn học kì"),
        self.var_std_name.set(""),
        self.var_div.set("Chọn phân lớp"),
        self.var_roll.set(""),
        self.var_gender.set("Chọn giới tính"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_std_id.set(""),
        # self.var_radio1.set("")

    # +++++++++++++++++++++++++++++++++++++Search +++++++++++++++++++++++++++++++++++++++++
    def search_data(self):
        if self.var_search_type.get() == "Chọn":
            messagebox.showerror("Error", "Bạn phải chọn giá trị cho Tìm theo: ", parent=self.window)
        else:

            conn = mysql.connector.connect(host="localhost", username="root", password="Pmdnh123!",
                                           database="face_recognition")
            my_cursor = conn.cursor()
            if self.var_search_type.get() == "Mã môn":
                my_cursor.execute("select * from student where Roll=%s", (self.var_search_value.get(),))
                data = my_cursor.fetchall()
                if (len(data) != 0):
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit();
            else:
                my_cursor.execute("select * from student where Phone=%s", (self.var_search_value.get(),))
                data = my_cursor.fetchall()
                if (len(data) != 0):
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    if rows == None:
                        messagebox.showerror("Error", "Không có dữ liệu được tìm thấy", parent=self.window)
                    conn.commit();
            conn.close()

    # ++++++++++++++++++++++++++++++Generate dataset or take photo sample+++++++++++++++++++++++++++++++
    def Generate_dataset(self):
        if self.var_dep.get() == "Chọn ngành" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Tất cả các trường không được để trống.", parent=self.window)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Pmdnh123!",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                # my_cursor.execute("select * from student")
                # myresult = my_cursor.fetchall()
                # # id = 0;
                # # for i in myresult:
                # #     id += 1

                my_cursor.execute(
                    "update student set course=%s, department=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s where Student_id=%s ",
                    (
                        self.var_course.get(),
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_std_id.get(),
                        # self.var_radio1.get()

                    ))

                conn.commit()
                self.fetch_data()

                conn.close()

                # ========= Load predifiend date on face frontals from Open-CV =================================
                face_Classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                    fases = face_Classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor =1.3
                    # minimum neighbor =5
                    for (x, y, w, h) in fases:
                        face_croped = img[y:y + h, x:x + w]
                        return face_croped

                masv = self.var_std_id.get()
                print("id ", masv)
                cap = cv2.VideoCapture(0)
                img_id = 0;

                while True:
                    ret, myFrame = cap.read()
                    if face_croped(myFrame) is not None:
                        img_id += 1;
                        face = cv2.resize(face_croped(myFrame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(masv) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                # when eveyting done release capture
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Thu Thập Datasets thành công")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.window)


if __name__ == "__main__":
    root = Tk()
    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")
    obj = StudentDetails(root)
    root.mainloop()
