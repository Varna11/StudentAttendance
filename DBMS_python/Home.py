import mysql.connector as ms
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk


class Home:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.title('Home')
        self.lbl_title = Label(self.root, text="STUDENT ATTENDANCE MANAGEMENT SYSTEM", font=("Roboto", 30, "bold"),
                               fg="dark blue", bg="light blue", relief=RAISED, bd=10)
        self.lbl_title.place(x=0, y=1, relwidth=1)
        self.root.geometry('700x600')
        self.root.config(bg="#1572A1")

        self.frame = tk.Frame(self.root, bg="#1572A1")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Buttons
        self.Admin_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                   text="Admin", command=self.Admin)
        self.Admin_btn.grid(row=0, column=0, padx=20)

        self.Faculty_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", text="Faculty",
                                     font=("Comic sans", 12, "bold"), command=self.Faculty)
        self.Faculty_btn.grid(row=0, column=1, padx=20)

        self.Student_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", text="Student",
                                     font=("Comic sans", 12, "bold"), command=self.Student)
        self.Student_btn.grid(row=0, column=2, padx=20)

        # Buttons
        self.Admin_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 20, "bold"),
                                   text="Admin", command=self.Admin)
        self.Admin_btn.grid(row=0, column=0, padx=20)

        self.Faculty_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", text="Faculty",
                                     font=("Comic sans", 20, "bold"), command=self.Faculty)
        self.Faculty_btn.grid(row=0, column=1, padx=20)

        self.Student_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", text="Student",
                                     font=("Comic sans", 20, "bold"), command=self.Student)
        self.Student_btn.grid(row=0, column=2, padx=20)

    def Admin(self):
        self.frame.destroy()
        self.another = login(self.root)

    def Faculty(self):
        self.frame.destroy()
        self.another = Attendance(self.root)

    def Student(self):
        self.frame.destroy()
        self.another = ViewAtt(self.root)


class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry('700x400')
        self.root.title('Attendance')

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.C_id_label = Label(self.frame, text='Select Course Id : ', font=('Helvetica', 10))
        self.C_id_label.grid(row=0, column=0)
        self.USN_label = Label(self.frame, text='Select Valid USN :', font=('Helvetica', 10))
        self.USN_label.grid(row=1, column=0)
        self.F_id_label = Label(self.frame, text='Select Valid Faculty Id :', font=('Helvetica', 10))
        self.F_id_label.grid(row=2, column=0)
        self.At_id_label = Label(self.frame, text='Enter Attendance Id : ', font=('Helvetica', 10))
        self.At_id_label.grid(row=3, column=0)
        self.At_pct_label = Label(self.frame, text='Enter Attendance Percentage: ', font=('Helvetica', 10))
        self.At_pct_label.grid(row=4, column=0)

        self.At_id = Entry(self.frame, width=30)
        self.At_id.grid(row=3, column=1, padx=10, pady=10)
        self.At_pct = Entry(self.frame, width=30)
        self.At_pct.grid(row=4, column=1, padx=10)

        self.create_btn = Button(self.frame, text='Submit Attendance', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 13, "bold"), command=self.create)
        self.create_btn.grid(row=5, column=1, padx=10, pady=10)

        # drop down for course
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select C_id from Course"
        c.execute(sql)
        # records = c.fetchall()
        values = [item[0] for item in c.fetchall()]
        mydb.commit()
        self.options1 = values
        self.clicked1 = StringVar(self.frame)

        self.drop = OptionMenu(self.frame, self.clicked1, *self.options1)
        self.drop.grid(row=0, column=1)

        # drop down for usn
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select USN from Student"
        c.execute(sql)
        # records = c.fetchall()
        records = [item[0] for item in c.fetchall()]
        mydb.commit()
        self.options2 = records
        self.clicked2 = StringVar(self.frame)

        self.drop = OptionMenu(self.frame, self.clicked2, *self.options2)
        self.drop.grid(row=1, column=1)

        # drop down for Fac_id
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select F_id from Faculty"
        c.execute(sql)
        result = c.fetchall()
        mydb.commit()
        self.options = list(item[0] for item in result)
        self.clicked3 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked3, *self.options)
        self.drop.grid(row=2, column=1, columnspan=2)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='Go Back', width="20", height="2", bg="light blue",
                                    font=("Comic sans", 13, "bold"), command=self.back)
        self.cancel_btn.grid(row=6, column=1, pady=7, padx=7)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Home(self.root)

    def create(self):
        self.c_id = self.clicked1.get()
        self.usn = self.clicked2.get()
        self.f_id = self.clicked3.get()
        self.at_id = self.At_id.get()
        self.at_pcnt = self.At_pct.get()

        records = (self.c_id, self.usn, self.f_id, self.at_id, self.at_pcnt)
        print(records)
        if self.c_id == '' or self.usn == '' or self.f_id == '' or self.at_id == '' or self.at_pcnt == '':
            messagebox.showinfo('Error', 'All fields required')
        else:
            mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = mydb.cursor()
            sql = "Insert into Attendance (C_id,USN,F_id,At_id,At_percent) values (%s,%s,%s,%s,%s)"
            c.execute(sql, records)
            mydb.commit()
            messagebox.showinfo('Course Assign', 'Successfully Inserted')
            mydb.close()


class ViewAtt:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x500')
        self.root.title('View Attendance')

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.config(background='white')

        self.USN_label = Label(self.frame, text='Select Valid USN :', font=('bold', 12))
        self.USN_label.grid(row=0, column=0)

        # drop down for usn
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select Distinct USN from Attendance"
        c.execute(sql)
        records = [item[0] for item in c.fetchall()]
        mydb.commit()
        self.options1 = records
        self.clicked1 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked1, *self.options1)
        self.drop.grid(row=0, column=1, pady=15)

        # tree view styling
        self.style = ttk.Style()
        self.style.configure("Treeview", background="silver", foreground="black", fieldbackground="silver")
        self.style.map("Treeview", background=[('selected', "#00ff00")])

        self.cols = ('Course_id', 'USN', 'Faculty_id', 'Attendance_id', 'Attendance_Percent')
        self.listBox = ttk.Treeview(self.frame, columns=self.cols, show='headings')

        # treeview
        for col in self.cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.grid(row=1, column=0)
            self.listBox.column("#1", anchor=CENTER, width=100)
            self.listBox.column("#2", anchor=CENTER, width=100)
            self.listBox.column("#3", anchor=CENTER, width=120)
            self.listBox.column("#4", anchor=CENTER, width=100)
            self.listBox.column("#5", anchor=CENTER, width=100)

        self.create_btn = Button(self.frame, text='Check Attendance', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 13, "bold"), command=self.create)
        self.create_btn.grid(row=2, column=0, padx=10, pady=10)

        self.cancel_btn = tk.Button(self.frame, text='Go Back', width="20", height="2", bg="light blue",
                                    font=("Comic sans", 13, "bold"), command=self.back)
        self.cancel_btn.grid(row=2, column=1, columnspan=1)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Home(self.root)

    def create(self):
        self.usn = self.clicked1.get()

        if (self.clicked1 == ''):
            messagebox.showinfo('Error', 'USN required!!')
        else:
            mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = mydb.cursor()
            sql = f"Select * from Attendance where USN = '{self.usn}' "
            c.execute(sql)
            self.records = c.fetchall()
            for i, (C_id, USN, F_id, At_id, At_Percent) in enumerate(self.records, start=1):
                self.listBox.insert("", "end", values=(C_id, USN, F_id, At_id, At_Percent))
            mydb.commit()
            # messagebox.showinfo('Course Assign', 'Successfully Inserted')
            mydb.close()


class login:
    def __init__(self, root):
        self.root = root
        self.root.config(background='#1572A1')
        self.root.title('Admin Login')
        self.root.geometry('700x600')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.config(background='white')

        self.photo2 = PhotoImage(file='login.png')
        self.photo = tk.Label(self.frame, image=self.photo2, bg='white')
        self.photo.grid(row=0, column=10)

        # Labels
        self.username_label = tk.Label(self.frame, text="Username:", font=('Helvetica', 15), bg='white')
        self.username_label.grid(row=4, column=9, pady=10)

        self.username = tk.Entry(self.frame, bg='white')
        self.username.grid(row=4, column=10, pady=10)

        self.password_label = tk.Label(self.frame, text="Password:", font=('Helvetica', 15), bg='white')
        self.password_label.grid(row=8, column=9, pady=10)

        self.password = tk.Entry(self.frame, bg='white')
        self.password.grid(row=8, column=10, pady=10)
        self.password.config(show="*")

        # Login button
        self.login_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                   text="Login", command=self.Login)
        self.login_btn.grid(row=10, column=10, pady=10)

        self.back_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                  text='Go Back', command=self.back)
        self.back_btn.grid(row=15, column=10, pady=10)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Home(self.root)

    # login fn
    def Login(self):
        self.uname = self.username.get()
        self.pwd = self.password.get()

        if (self.uname == "" and self.pwd == ""):
            messagebox.showinfo("LoginError", "Blank Entries not allowed")
        elif (self.uname == "Admin" and self.pwd == "Admin123"):
            messagebox.showinfo('Welcome', 'Login Successful')
            self.frame.destroy()
            self.another = Records(self.root)

        else:
            messagebox.showinfo('LoginError', 'Incorrect Username and Password')


class Records:
    def __init__(self, root):
        self.root = root
        self.root.title('Insert Profile')
        self.root.geometry('700x600')
        self.frame = tk.Frame(self.root, bg="#1572A1")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # create btns
        self.Student_btn = Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                  text='Insert Student Profile', command=self.Student)
        self.Student_btn.grid(row=1, column=1, pady=10)

        self.Faculty_btn = Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                  text='Insert Faculty Profile', command=self.Faculty)
        self.Faculty_btn.grid(row=2, column=1, pady=10)

        self.AddBranch_btn = Button(self.frame, width="20", height="2", bg="light blue",
                                    font=("Comic sans", 12, "bold"), text='Add Branch', command=self.Branch)
        self.AddBranch_btn.grid(row=3, column=1, pady=10)

        self.AddCourse_btn = Button(self.frame, width="20", height="2", bg="light blue",
                                    font=("Comic sans", 12, "bold"), text='Add Course', command=self.Course)
        self.AddCourse_btn.grid(row=4, column=1, pady=10)

        self.back_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                  text='Go Back', command=self.back)
        self.back_btn.grid(row=5, column=1, pady=10)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Home(self.root)

    def Student(self):
        self.frame.destroy()
        self.another = StuRec(self.root)

    def Faculty(self):
        self.frame.destroy()
        self.another = FacultyRec(self.root)

    def Branch(self):
        self.frame.destroy()
        self.another = AddBranch(self.root)

    def Course(self):
        self.frame.destroy()
        self.another = AddCourse(self.root)


class StuRec:
    def __init__(self, root):
        self.root = root
        self.root.title('StudentRecords')
        self.root.geometry('700x600')

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create Text Box Labels
        self.USN_label = Label(self.frame, text='Enter USN', font=('bold', 12))
        self.USN_label.grid(row=0, column=0)
        self.S_Name_label = Label(self.frame, text='Enter Name', font=('bold', 12))
        self.S_Name_label.grid(row=1, column=0)
        self.S_Phone_label = Label(self.frame, text='Enter Phone Number', font=('bold', 12))
        self.S_Phone_label.grid(row=2, column=0)
        self.S_Email_label = Label(self.frame, text='Enter mail', font=('bold', 12))
        self.S_Email_label.grid(row=3, column=0)
        self.S_Address_label = Label(self.frame, text='Enter Address', font=('bold', 12))
        self.S_Address_label.grid(row=4, column=0)

        # Create Text boxes
        self.USN = Entry(self.frame, width=30)
        self.USN.grid(row=0, column=1, pady=10)
        self.S_Name = Entry(self.frame, width=30)
        self.S_Name.grid(row=1, column=1, pady=10)
        self.S_Phone = Entry(self.frame, width=30)
        self.S_Phone.grid(row=2, column=1, pady=10)
        self.S_Email = Entry(self.frame, width=30)
        self.S_Email.grid(row=3, column=1, pady=10)
        self.S_Address = Entry(self.frame, width=30)
        self.S_Address.grid(row=4, column=1, pady=10)

        # Submit button
        self.submit_btn = Button(self.frame, text='Submit Profile', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 12, "bold"), command=self.submit)
        self.submit_btn.grid(row=6, column=0, padx=10, pady=10)

        # Delete button
        self.delete_btn = Button(self.frame, text='Delete Profile', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 12, "bold"), command=self.DelProfile)
        self.delete_btn.grid(row=6, column=1, padx=10, pady=10)

        # Query Button
        self.query_btn = Button(self.frame, text='Show Profiles', width="20", height="2", bg="light blue",
                                font=("Comic sans", 12, "bold"), command=self.GetProfile)
        self.query_btn.grid(row=6, column=2, padx=10, pady=10)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='Go Back', width="20", height="2", bg="light blue",
                                    font=("Comic sans", 12, "bold"), command=self.back)
        self.cancel_btn.grid(row=9, column=2, padx=10, pady=20)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Records(self.root)

    # Submit fn
    def submit(self):
        self.usn = self.USN.get()
        self.name = self.S_Name.get()
        self.phone = self.S_Phone.get()
        self.email = self.S_Email.get()
        self.address = self.S_Address.get()

        self.records = (self.usn, self.name, self.phone, self.email, self.address)

        if (self.usn == '' or self.name == '' or self.phone == '' or self.email == '' or self.address == ''):
            messagebox.showinfo('Insert Status', 'All fields are required')
        else:
            conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = conn.cursor()
            sql = "Insert into student(USN, S_Name, S_Phone, S_Email, S_Address) values (%s,%s,%s,%s,%s)"
            c.execute(sql, self.records)
            conn.commit()
            c.close()
            messagebox.showinfo("Insert Status", "Record is inserted successfully")
            # conn.close()

        # clear the fields
        self.USN.delete(0, END)
        self.S_Name.delete(0, END)
        self.S_Phone.delete(0, END)
        self.S_Email.delete(0, END)
        self.S_Address.delete(0, END)

    # Create delete fn
    def DelProfile(self):

        self.usn = self.USN.get()
        print(f"usn: [{self.usn}]")
        if (self.usn == " "):
            messagebox.showinfo("Delete Status", "USN not found")
        else:
            conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = conn.cursor()
            sql = f"DELETE FROM student WHERE USN='{self.usn}'"
            print(sql)

            print(conn.is_connected())
            result = c.execute(sql)
            conn.commit()
            print(f'Cursor rowcount: {c.rowcount} row(s) deleted')
            if result == None and c.rowcount == 1:
                messagebox.showinfo("Delete Status", "Record deleted successfully")
            else:
                messagebox.showinfo("Delete Status", "Unsuccessful")
            # conn.close()
            c.close()

        # clear the fields
        self.USN.delete(0, END)

    # create query fn
    def GetProfile(self):
        self.frame.destroy()
        self.another = StuShowProfile(self.root)


class StuShowProfile:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Profiles')
        self.root.geometry('600x400')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.style = ttk.Style()
        self.style.configure("Treeview", background="silver", foreground="black", fieldbackground="silver")
        self.style.map("Treeview", background=[('selected', "#00ff00")])

        self.cols = ('USN', 'Name', 'Phone Number', 'Email', 'Address')
        self.listBox = ttk.Treeview(self.frame, columns=self.cols, show='headings')

        for col in self.cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.grid(row=4, column=0)
            self.listBox.column("#1", anchor=CENTER, width=100)
            self.listBox.column("#2", anchor=CENTER, width=100)
            self.listBox.column("#3", anchor=CENTER, width=120)
            self.listBox.column("#4", anchor=CENTER, width=100)
            self.listBox.column("#5", anchor=CENTER, width=100)

        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select * from Student"
        c.execute(sql)
        self.records = c.fetchall()
        for i, (USN, S_Name, S_Phone, S_Email, S_Address) in enumerate(self.records, start=1):
            self.listBox.insert("", "end", values=(USN, S_Name, S_Phone, S_Email, S_Address))
        mydb.commit()
        # messagebox.showinfo('Course Assign', 'Successfully Inserted')
        mydb.close()

        self.back_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                  text='Go Back', command=self.back)
        self.back_btn.grid(row=5, column=1, padx=10, pady=10)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = StuRec(self.root)


class FacultyRec:
    def __init__(self, root):
        self.root = root
        self.root.title('FacultyRecords')
        self.root.geometry('600x400')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create Text Box Labels
        self.F_id_label = Label(self.frame, text='Enter Faculty Id', font=('bold', 12))
        self.F_id_label.grid(row=0, column=0)
        self.F_Name_label = Label(self.frame, text='Enter Faculty Name', font=('bold', 12))
        self.F_Name_label.grid(row=2, column=0)
        self.F_Phone_label = Label(self.frame, text='Enter Phone Number', font=('bold', 12))
        self.F_Phone_label.grid(row=4, column=0)
        self.F_Email_label = Label(self.frame, text='Enter mail', font=('bold', 12))
        self.F_Email_label.grid(row=6, column=0)
        self.F_Address_label = Label(self.frame, text='Enter Address', font=('bold', 12))
        self.F_Address_label.grid(row=8, column=0)

        # Create Text boxes
        self.F_id = Entry(self.frame, width=30)
        self.F_id.grid(row=0, column=1, pady=10)
        self.F_Name = Entry(self.frame, width=30)
        self.F_Name.grid(row=2, column=1)
        self.F_Phone = Entry(self.frame, width=30)
        self.F_Phone.grid(row=4, column=1, pady=10)
        self.F_Email = Entry(self.frame, width=30)
        self.F_Email.grid(row=6, column=1, pady=10)
        self.F_Address = Entry(self.frame, width=30)
        self.F_Address.grid(row=8, column=1, pady=10)

        # Submit button

        self.submit_btn = Button(self.frame, text='Submit Profile', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 12, "bold"), command=self.submit)
        self.submit_btn.grid(row=12, column=0, padx=10, pady=10)

        # Delete button
        self.delete_btn = Button(self.frame, text='Delete Profile', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 12, "bold"), command=self.DelProfile)
        self.delete_btn.grid(row=12, column=1, padx=10, pady=10)

        # Query Button
        self.query_btn = Button(self.frame, text='Show Profiles', width="20", height="2", bg="light blue",
                                font=("Comic sans", 12, "bold"), command=self.GetProfile)
        self.query_btn.grid(row=12, column=2, padx=10, pady=10)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='Go Back', width="20", height="2", bg="light blue",
                                    font=("Comic sans", 12, "bold"), command=self.back)
        self.cancel_btn.grid(row=16, column=2, padx=10, pady=20)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Records(self.root)

    # Submit fn
    def submit(self):
        # global USN, S_Name, S_Phone, S_Email, S_Address
        self.Fac_id = self.F_id.get()
        self.Fac_Name = self.F_Name.get()
        self.Fac_phone = self.F_Phone.get()
        self.Fac_email = self.F_Email.get()
        self.Fac_address = self.F_Address.get()

        self.records = (self.Fac_id, self.Fac_Name, self.Fac_phone, self.Fac_email, self.Fac_address)

        if (
                self.Fac_id == '' or self.Fac_Name == '' or self.Fac_phone == '' or self.Fac_email == '' or self.Fac_address == ''):
            messagebox.showinfo('Insert Status', 'All fields are required')
        else:
            conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = conn.cursor()
            sql = "Insert into Faculty(F_id, F_Name, F_Phone, F_Email, F_Address) values (%s,%s,%s,%s,%s)"
            c.execute(sql, self.records)
            conn.commit()
            c.close()
            messagebox.showinfo("Insert Status", "Record is inserted successfully")
            # conn.close()

        # clear the fields
        self.F_id.delete(0, END)
        self.F_Name.delete(0, END)
        self.F_Phone.delete(0, END)
        self.F_Email.delete(0, END)
        self.F_Address.delete(0, END)

    # Create delete fn
    def DelProfile(self):

        self.Fac_id = self.F_id.get()
        print(f"usn: [{self.Fac_id}]")
        if (self.Fac_id == " "):
            messagebox.showinfo("Delete Status", "USN not found")
        else:
            conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = conn.cursor()
            sql = f"DELETE FROM faculty WHERE F_id ='{self.Fac_id}'"
            print(sql)

            print(conn.is_connected())
            result = c.execute(sql)
            conn.commit()
            print(f'Cursor rowcount: {c.rowcount} row(s) deleted')
            if result == None and c.rowcount == 1:
                messagebox.showinfo("Delete Status", "Record deleted successfully")
            else:
                messagebox.showinfo("Delete Status", "Unsuccessful")
            # conn.close()
            c.close()

        # clear the fields
        self.F_id.delete(0, END)

    # create query fn
    def GetProfile(self):
        self.frame.destroy()
        self.another = FacShowProfile(self.root)


class FacShowProfile:
    def __init__(self, root):
        self.root = root
        self.root.title('Faculty Profiles')
        self.root.geometry('600x400')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.style = ttk.Style()
        self.style.configure("Treeview", background="silver", foreground="black", fieldbackground="silver")
        self.style.map("Treeview", background=[('selected', "#00ff00")])

        self.cols = ('F_id', 'F_Name', 'F_Phone', 'F_Email', 'F_Address')
        self.listBox = ttk.Treeview(self.frame, columns=self.cols, show='headings')

        for col in self.cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.grid(row=4, column=0)
            self.listBox.column("#1", anchor=CENTER, width=100)
            self.listBox.column("#2", anchor=CENTER, width=100)
            self.listBox.column("#3", anchor=CENTER, width=120)
            self.listBox.column("#4", anchor=CENTER, width=100)
            self.listBox.column("#5", anchor=CENTER, width=100)

        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select * from Faculty"
        c.execute(sql)
        self.records = c.fetchall()
        for i, (F_id, F_Name, F_Phone, F_Email, F_Address) in enumerate(self.records, start=1):
            self.listBox.insert("", "end", values=(F_id, F_Name, F_Phone, F_Email, F_Address))
        mydb.commit()
        mydb.close()

        self.back_btn = tk.Button(self.frame, width="20", height="2", bg="light blue", font=("Comic sans", 12, "bold"),
                                  text='Go Back', command=self.back)
        self.back_btn.grid(row=5, column=1, padx=10, pady=10)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = FacultyRec(self.root)


class AddBranch:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x600')
        self.root.title('Add Branch')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        # self.frame.config(background='grey')

        # creating Text Labels
        self.Branch_Name_label = Label(self.frame, text='Select Branch Name', font=('bold', 12))
        self.Branch_Name_label.grid(row=1, column=0)
        self.USN_label = Label(self.frame, text='Select Valid USN:', font=('bold', 12))
        self.USN_label.grid(row=2, column=0)
        self.F_id_label = Label(self.frame, text='Select Valid Faculty Id:', font=('bold', 12))
        self.F_id_label.grid(row=3, column=0)

        # creating a Create button

        self.create_btn = Button(self.frame, text='Register', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 12, "bold"), command=self.create)
        self.create_btn.grid(row=4, column=1, padx=10, pady=10)

        # dropdown for Branch Name
        self.options = [
            "Computer Science",
            "Electronics",
            "Mechanical",
            "Information Science"]
        self.clicked = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked, *self.options)
        self.drop.grid(row=1, column=1, pady=10)

        # drop down for USN
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select USN from Student"
        c.execute(sql)
        records = c.fetchall()
        mydb.commit()
        self.options1 = list(item[0] for item in records)
        self.clicked1 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked1, *self.options1)
        self.drop.grid(row=2, column=1, pady=10)

        # drop down for Fac_id
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select F_id from Faculty"
        c.execute(sql)
        result = c.fetchall()
        mydb.commit()
        self.options = list(item[0] for item in result)
        self.clicked2 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked2, *self.options)
        self.drop.grid(row=3, column=1, pady=10)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='Go Back', width="20", height="2", bg="light blue",
                                    font=("Comic sans", 12, "bold"), command=self.back)
        self.cancel_btn.grid(row=5, column=1)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Records(self.root)

    def create(self):
        self.Branch_Name = self.clicked.get()
        self.USN = self.clicked1.get()
        self.Fac_id = self.clicked2.get()
        records = (self.Branch_Name, self.USN, self.Fac_id)
        print(self.clicked1.get())
        print(self.clicked2.get())

        if self.Branch_Name == '' or self.USN == '' or self.Fac_id == '':
            messagebox.showinfo('Error', 'All fields required')
        else:
            mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = mydb.cursor()
            sql = "Insert into Branch values (%s,%s,%s)"
            c.execute(sql, records)
            mydb.commit()
            messagebox.showinfo('Branch Assign', 'Successfully Inserted')
            mydb.close()

        # clear the fields
        self.Branch_Name.delete(END, 0)
        self.USN.delete(END, 0)
        self.Fac_id.delete(END, 0)


class AddCourse:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x500')
        self.root.title('Course')

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        # self.frame.config(background='white')

        self.C_id_label = Label(self.frame, text='Enter Course Id : ', font=('bold', 12))
        self.C_id_label.grid(row=0, column=0)
        self.C_Name_label = Label(self.frame, text='Enter Course Name :', font=('bold', 12))
        self.C_Name_label.grid(row=1, column=0)
        self.USN_label = Label(self.frame, text='Enter Valid USN :', font=('bold', 12))
        self.USN_label.grid(row=2, column=0)
        self.F_id_label = Label(self.frame, text='Enter Valid Faculty Id :', font=('bold', 12))
        self.F_id_label.grid(row=3, column=0)

        self.C_id = Entry(self.frame, width=30)
        self.C_id.grid(row=0, column=1, pady=10)
        self.C_Name = Entry(self.frame, width=30)
        self.C_Name.grid(row=1, column=1, pady=10)

        self.create_btn = Button(self.frame, text='Register', width="20", height="2", bg="light blue",
                                 font=("Comic sans", 12, "bold"), command=self.create)
        self.create_btn.grid(row=4, column=1, padx=10, pady=10)

        # drop down for usn
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select USN from Student"
        c.execute(sql)
        records = [item[0] for item in c.fetchall()]
        mydb.commit()
        self.options1 = records
        self.clicked1 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked1, *self.options1)
        self.drop.grid(row=2, column=1, pady=10)

        # drop down for Fac_id
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select F_id from Faculty"
        c.execute(sql)
        result = c.fetchall()
        mydb.commit()
        self.options = list(item[0] for item in result)
        self.clicked2 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked2, *self.options)
        self.drop.grid(row=3, column=1, pady=10)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='Go Back', width="20", height="2", bg="light blue",
                                    font=("Comic sans", 12, "bold"), command=self.back)
        self.cancel_btn.grid(row=5, column=1, padx=10, pady=10)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Records(self.root)

    def create(self):
        self.c_id = self.C_id.get()
        self.c_name = self.C_Name.get()
        self.usn = self.clicked1.get()
        self.f_id = self.clicked2.get()

        records = (self.c_id, self.c_name, self.usn, self.f_id)
        print(records)
        if self.c_id == '' or self.c_name == '' or self.usn == '' or self.f_id == '':
            messagebox.showinfo('Error', 'All fields required')
        else:
            mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = mydb.cursor()
            sql = "Insert into Course (C_id,C_Name,USN,F_id) values (%s,%s,%s,%s)"
            c.execute(sql, records)
            mydb.commit()
            messagebox.showinfo('Course Assign', 'Successfully Inserted')
            mydb.close()

        self.C_id.delete(0, END)
        self.C_Name.delete(0, END)
        self.clicked1.delete(0, END)
        self.clicked2.delete(0, END)


root = tk.Tk()
run = Home(root)
root.mainloop()
