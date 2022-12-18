from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import mysql.connector
import csv

mydata = []

class Attendance:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1196x635+0+0")
        self.window.title("Điểm danh")

        # =================variables==============
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_statusAttendance = StringVar()

        ########-------------BACKGROUND-------------------
        img = Image.open(r"assets/image/bg2 (1).png")
        img = img.resize((1196, 635))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = ttk.Label(self.window, image=self.photoImg)
        bg_img.place(x=0, y=0, width=1196, height=635)

        ########-------------MAIN_FRAME-------------------
        main_frame = ttk.Frame(bg_img)
        main_frame.place(x=25, y=45, width=1145, height=560)

        ########-------------LEFT_FRAME-------------------
        left_frame = ttk.Labelframe(main_frame, text="Thông tin điểm danh sinh viên")
        left_frame.place(x=10, y=10, width=600, height=540)

        ########-------------STUDENT_ATTENDANCE_DETAILS-------------------
        img_left = Image.open(r"assets/image/left_img.jpg")
        img_left = img_left.resize((589, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = ttk.Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=589, height=130)

        left_insider_frame = ttk.Labelframe(left_frame)
        left_insider_frame.place(x=5, y=135, width=588, height=380)

        # Label and Entry
        # Student ID
        attendance_id_label = ttk.Label(left_insider_frame, text="Mã sinh viên")
        attendance_id_label.grid(row=0, column=0, padx=5, sticky=W)

        attendance_id_entry = ttk.Entry(left_insider_frame, width=20, textvariable=self.var_id)
        attendance_id_entry.grid(row=0, column=1, padx=5,pady=5, ipadx=10, sticky=W)

        # Student name
        student_name_label = ttk.Label(left_insider_frame, text="Họ tên")
        student_name_label.grid(row=1, column=0, padx=5, sticky=W)

        student_name_entry = ttk.Entry(left_insider_frame, width=20, textvariable=self.var_name)
        student_name_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=10, sticky=W)

        # Time
        time_label = Label(left_insider_frame, text="Thời gian")
        time_label.grid(row=2, column=0, padx=5, sticky=W)

        time_entry = ttk.Entry(left_insider_frame, textvariable=self.var_time, width=20)
        time_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=10, sticky=W)

        # Attendance status
        attendance_label = ttk.Label(left_insider_frame, text="Trạng thái điểm danh")
        attendance_label.grid(row=3, column=0, padx=5, sticky=W)

        attendance_status = ttk.Combobox(left_insider_frame, width=17, state="readonly",
                                              textvariable=self.var_statusAttendance, foreground='black',background='white')
        attendance_status["values"] = ("Chọn trạng thái", "Có mặt", "Vắng mặt")
        attendance_status.current(0)
        attendance_status.grid(row=3, column=1, padx=5, pady=5, ipadx=20, sticky=W)

        # Roll
        roll_label = ttk.Label(left_insider_frame, text="Số phòng")
        roll_label.grid(row=0, column=2, padx=5, sticky=W)

        roll_entry = ttk.Entry(left_insider_frame, width=20, textvariable=self.var_roll)
        roll_entry.grid(row=0, column=3, padx=5, pady=5, ipadx=10, sticky=W)

        # Department
        department_label = ttk.Label(left_insider_frame, text="Ngành")
        department_label.grid(row=1, column=2, padx=5, sticky=W)

        department_entry = ttk.Entry(left_insider_frame, width=20, textvariable=self.var_department)
        department_entry.grid(row=1, column=3, padx=5, pady=5, ipadx=10, sticky=W)

        # Attendance date
        date_label = ttk.Label(left_insider_frame, text="Ngày")
        date_label.grid(row=2, column=2, padx=5,sticky=W)

        date_entry = ttk.Entry(left_insider_frame, width=20, textvariable=self.var_date)
        date_entry.grid(row=2, column=3, padx=5, pady=5, ipadx=10, sticky=W)

        # Buttom frame
        btn_frame = ttk.Frame(left_insider_frame, border=5)
        btn_frame.place(x = 0, y = 300, width =574, height =60)

        # importCSV button
        import_btn = Button(btn_frame, width=15, pady=7, text="Nhập CSV", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", command=self.importCSV, activeforeground="white", font=("Poppins", 10, "bold"))
        import_btn.grid(row=0, column=0, padx=10)

        # ExportCSV button
        export_btn = Button(btn_frame, width=15, pady=7, text="Xuất CSV", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", command=self.exportCSV, activeforeground="white", font=("Poppins", 10, "bold"))
        export_btn.grid(row=0, column=1, padx=10)

        # Update button
        update_btn = Button(btn_frame, width=15, pady=7, text="Cập nhật", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D", command=self.update, activeforeground="white", font=("Poppins", 10, "bold"))
        update_btn.grid(row=0, column=2, padx=10)

        # Reset button
        reset_btn = Button(btn_frame, width=15, pady=7, text="Nhập lại", bg='#e6c511', cursor='hand2', fg='white',
                          border=0, activebackground="#1E329D",command=self.reset, activeforeground="white", font=("Poppins", 10, "bold"))
        reset_btn.grid(row=0, column=3, padx=10)

        ########-------------RIGHT_FRAME-------------------
        right_frame = ttk.LabelFrame(main_frame, text="Quản lý điểm danh")
        right_frame.place(x=610, y=10, width=530, height=540)

        ########-------------ATTENDANCE_DETAILS-------------------
        img_right = Image.open(r"assets/image/right-img.jpg")
        img_right = img_right.resize((521, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = ttk.Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=3, y=0, width=521, height=130)

        # # ============== SEARCH ====================
        # search_frame = ttk.Labelframe(right_frame, text="Tìm kiếm thông tin")
        # search_frame.place(x=5, y=135, width=519, height=80)
        #
        # search_label = ttk.Label(search_frame, text="Tìm theo:", border=3)
        # search_label.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        #
        # search_combo = ttk.Combobox(search_frame, width=13, state="readonly")
        # search_combo["values"] = ("Chọn", "Mã môn", "Số điện thoại", "Mã sinh viên")
        # search_combo.current(0)
        # search_combo.grid(row=0, column=1, padx=5, pady=10, ipadx=2, sticky=W)
        #
        # search_entry = ttk.Entry(search_frame, width=15)
        # search_entry.grid(row=0, column=2, padx=2, pady=5, ipadx=10, sticky=W)
        #
        # search_btn = Button(search_frame, width=8, pady=2, text="Tìm kiếm", bg='#e6c511', cursor='hand2', fg='white',
        #                     border=0, activebackground="#1E329D", activeforeground="white",
        #                     font=("Poppins", 10, "bold"))
        # search_btn.grid(row=0, column=3, padx=3)
        #
        # showAll_btn = Button(search_frame, width=12, pady=2, text="Hiển thị tất cả", bg='#e6c511', cursor='hand2',
        #                      fg='white',
        #                      border=0, activebackground="#1E329D", activeforeground="white",
        #                      font=("Poppins", 10, "bold"))
        # showAll_btn.grid(row=0, column=4, padx=3)

        # ====================Table Frame====================
        table_frame = ttk.Frame(right_frame, border=5)
        table_frame.place(x=2, y=135, width=525, height=385)

        # ==================== scroll bar table===============================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Attendance_report_table = ttk.Treeview(table_frame, columns=(
        "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # lenh config dung de di chuyen duoc thanh scrollbar
        scroll_x.config(command=self.Attendance_report_table.xview)
        scroll_y.config(command=self.Attendance_report_table.yview)

        self.Attendance_report_table.heading("id", text="Mã Sinh viên")
        self.Attendance_report_table.heading("roll", text="Số phòng")
        self.Attendance_report_table.heading("name", text="Tên sinh viên")
        self.Attendance_report_table.heading("department", text="Ngành")
        self.Attendance_report_table.heading("time", text="Giờ vào lớp")
        self.Attendance_report_table.heading("date", text="Ngày")
        self.Attendance_report_table.heading("attendance", text="Trạng thái")
        self.Attendance_report_table["show"] = "headings"

        self.Attendance_report_table.column("id", width=100)
        self.Attendance_report_table.column("roll", width=100)
        self.Attendance_report_table.column("name", width=100)
        self.Attendance_report_table.column("department", width=100)
        self.Attendance_report_table.column("time", width=100)
        self.Attendance_report_table.column("date", width=100)
        self.Attendance_report_table.column("attendance", width=100)

        self.Attendance_report_table.pack(fill=BOTH, expand=1)
        self.Attendance_report_table.bind("<ButtonRelease>", self.get_content)

    # ===============================Fetch data============================
    def fetchData(self, rows):
        self.Attendance_report_table.delete(*self.Attendance_report_table.get_children())
        for i in rows:
            self.Attendance_report_table.insert("", END, values=i)

    # ImportCSV
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                             filetypes=(("File CSV", "*csv"), ("ALl File", "*.*")), parent=self.window)
        with open(fln) as file:
            csvread = csv.reader(file, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
        print(mydata)

    # ExportCSV
    def exportCSV(self):
        try:
            if (len(mydata) < 1):
                messagebox.showerror("No Data", "Không có dữ liệu để xuất file.", parent=self.window)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                                   filetypes=(("File CSV", "*csv"), ("ALl File", "*.*")),
                                                   parent=self.window)
            with open(fln, mode="w", newline="") as myfile:
                csvwriter = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    csvwriter.writerow(i)
                messagebox.showinfo("Success","Dữ liệu của bạn đã được xuất thành file " + os.path.basename(fln) + " thành công")
        except Exception as es:
            messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.window)

    def get_content(self, event=""):
        index = self.Attendance_report_table.focus()
        content = self.Attendance_report_table.item(index)
        data = content["values"]
        self.var_id.set(data[0])
        self.var_roll.set(data[1])
        self.var_name.set(data[2])
        self.var_department.set(data[3])
        self.var_time.set(data[4])
        self.var_date.set(data[5])
        self.var_statusAttendance.set(data[6])

    def update(self):
        for i in range(0, len(mydata)):
            for j in range(0, len(mydata[i])):

                if mydata[i][0] == self.var_id.get():
                    mydata[i][0] = self.var_id.get()
                    mydata[i][1] = self.var_roll.get()
                    mydata[i][2] = self.var_name.get()
                    mydata[i][3] = self.var_department.get()
                    mydata[i][4] = self.var_time.get()
                    mydata[i][5] = self.var_date.get()
                    mydata[i][6] = self.var_statusAttendance.get()
                    break
        self.fetchData(mydata)
        messagebox.showinfo("Success", "Dữ liệu đã được cập nhật thành công", parent=self.window)

    def reset(self):
        self.var_statusAttendance.set("Status"),
        self.var_id.set(""),
        self.var_date.set(""),
        self.var_department.set(""),
        self.var_time.set(""),
        self.var_name.set(""),
        self.var_roll.set("")
if __name__ == "__main__":
    root = Tk()
    # Set the initial theme
    style = ttk.Style(root)
    root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "light")
    obj = Attendance(root)
    root.mainloop()