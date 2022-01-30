import sys
import textwrap
import mysql.connector as ms
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk, Image


class Home:
    def __init__(self, root):
        self.root = root
        self.root = root
        # self.photo2 = PhotoImage(file='login.png')
        # self.photo = tk.Label(self.root, image=self.photo2, bg='white')
        # self.photo.grid(row=0, column=0)

        self.root.title('Home')
        self.root.iconbitmap('C:\\Users\\Shreyas\\PycharmProjects\\DBMS_python\\Images\\Admin2.ico')
        self.root.geometry('700x600')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        #Buttons
        self.Admin_btn = tk.Button(self.frame, text="Admin Access", command=self.Admin)
        self.Admin_btn.grid(row=0,column=1, columnspan=2)

        self.Faculty_btn = tk.Button(self.frame, text="Faculty Access", command=self.Faculty)
        self.Faculty_btn.grid(row=1, column=1, columnspan=2)

        self.Student_btn = tk.Button(self.frame, text="Student Access", command=self.Student)
        self.Student_btn.grid(row=2,column=1, columnspan=2)

    def Admin(self):
        self.frame.destroy()
        self.another=login(self.root)

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

            self.C_id_label = Label(self.frame, text='Select Course Id : ')
            self.C_id_label.grid(row=0, column=0)
            self.USN_label = Label(self.frame, text='Select Valid USN :')
            self.USN_label.grid(row=1, column=0)
            self.F_id_label = Label(self.frame, text='Select Valid Faculty Id :')
            self.F_id_label.grid(row=2, column=0)
            self.At_id_label = Label(self.frame, text='Enter Attendance Id : ')
            self.At_id_label.grid(row=3, column=0)
            self.At_pct_label = Label(self.frame, text='Enter Attendance Percentage: ')
            self.At_pct_label.grid(row=4, column=0)

            self.At_id = Entry(self.frame, width=30)
            self.At_id.grid(row=3, column=1, padx=10)
            self.At_pct = Entry(self.frame, width=30)
            self.At_pct.grid(row=4, column=1, padx=10)

            self.create_btn = Button(self.frame, text='Submit Attendance', bg='cyan', command=self.create)
            self.create_btn.grid(row=5, column=1, padx=10, pady=10)

            # drop down for usn
            mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = mydb.cursor()
            sql = "Select C_id from Course"
            c.execute(sql)
            # records = c.fetchall()
            values = [item[0] for item in c.fetchall()]
            mydb.commit()
            self.options1 = values
            self.clicked1 = StringVar(self.frame)
            # self.clicked.set(self.options[0])  # default option
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
            # self.clicked.set(self.options[0])  # default option
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
            # self.clicked.set(self.options[0])  # default option

            self.drop = OptionMenu(self.frame, self.clicked3, *self.options)
            self.drop.grid(row=2, column=1, columnspan=2)

            # go back
            self.cancel_btn = tk.Button(self.frame, text='go back', command=self.back)
            self.cancel_btn.grid(row=6, column=2, columnspan=1)

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
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x500')
        self.root.title('View Attendance')

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.config(background='white')

        self.USN_label = Label(self.frame, text='Select Valid USN :')
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
        self.drop.grid(row=0, column=1)

        self.cols = ('Course_id', 'USN', 'Faculty_id', 'Attendance_id', 'Attendance_Percent')
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

        self.create_btn = Button(self.frame, text='Check Attendance', bg='cyan', command=self.create)
        self.create_btn.grid(row=1, column=1, padx=10, pady=10)

        self.cancel_btn = tk.Button(self.frame, text='go back', command=self.back)
        self.cancel_btn.grid(row=2, column=1, columnspan=1)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Home(self.root)

    def create(self):
        self.usn = self.clicked1.get()

        if(self.clicked1==''):
            messagebox.showinfo('Error','USN required!!')
        else:
            mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            c = mydb.cursor()
            sql = f"Select * from Attendance where USN = '{self.usn}' "
            c.execute(sql)
            self.records = c.fetchall()
            for i, (C_id, USN, F_id, At_id, At_Percent) in enumerate(self.records, start=1):
                self.listBox.insert("", "end", values=(C_id, USN, F_id, At_id, At_Percent))
            mydb.commit()
            #messagebox.showinfo('Course Assign', 'Successfully Inserted')
            mydb.close()


class login:
    def __init__(self, root):
        self.root = root
        self.root.config(background='White')
        self.root.title('Admin Login')
        self.root.iconbitmap('C:\\Users\\Shreyas\\PycharmProjects\\DBMS_python\\Images\\Admin2.ico')
        self.root.geometry('700x600')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.config(background='white')

        self.photo2 = PhotoImage(file='login.png')
        self.photo = tk.Label(self.frame, image=self.photo2, bg='white')
        self.photo.grid(row=0, column=0)

        # Labels
        self.username_label = tk.Label(self.frame, text="Username:", font=('Helvetica', 15), bg='white')
        self.username_label.grid(row=4, column=0)
        self.username = tk.Entry(self.frame,bg='grey')
        self.username.grid(row=5, column=0, columnspan=2)

        self.password_label = tk.Label(self.frame, text="Password:", font=('Helvetica', 15), bg='white')
        self.password_label.grid(row=6, column=0)
        self.password = tk.Entry(self.frame, bg='grey')
        self.password.grid(row=7, column=0, columnspan=2)
        self.password.config(show="*")

        # Login button
        self.login_btn = tk.Button(self.frame, text="Login", command=self.Login)
        self.login_btn.grid(row=8, columnspan=2)

        # cancel button
        # self.cancel_btn = tk.Button(self.frame, text='Cancel', command=self.cancel)
        # self.cancel_btn.grid(row=4, columnspan=2)

        self.back_btn = tk.Button(self.frame, text='Go back', command=self.back)
        self.back_btn.grid(row=9, columnspan=2)

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
        elif (self.uname == "123" and self.pwd == "123"):
            messagebox.showinfo('Welcome', 'Login Successful')
            self.frame.destroy()
            self.another = Records(self.root)

        else:
            messagebox.showinfo('LoginError', 'Incorrect Username and Password')

    # def cancel(self):
    #     self.root.destroy()
    #     sys.exit()


class Records:
    def __init__(self, root):
        self.root = root
        self.root.title('Insert Profile')
        self.root.iconbitmap('C:\\Users\\Shreyas\\PycharmProjects\\DBMS_python\\Images\\Admin2.ico')
        self.root.geometry('700x600')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # create btns
        self.Student_btn = Button(self.frame, text='Insert Student Profile', command=self.Student)
        self.Student_btn.grid(row=1, column=1, columnspan=2)

        self.Faculty_btn = Button(self.frame, text='Insert Faculty Profile', command=self.Faculty)
        self.Faculty_btn.grid(row=2, column=1, columnspan=2)

        self.AddBranch_btn = Button(self.frame, text='Add Branch', command=self.Branch)
        self.AddBranch_btn.grid(row=3, column=1, columnspan=2)

        self.AddCourse_btn = Button(self.frame, text='Add Course', command=self.Course)
        self.AddCourse_btn.grid(row=4, column=1, columnspan=2)

        self.back_btn = tk.Button(self.frame, text='Go back', command=self.back)
        self.back_btn.grid(row=5,column=1, columnspan=2)

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
        self.USN_label = Label(self.frame, text='Enter USN', font=('bold', 11))
        self.USN_label.grid(row=0, column=0)
        self.S_Name_label = Label(self.frame, text='Enter Name', font=('bold', 11))
        self.S_Name_label.grid(row=2, column=0)
        self.S_Phone_label = Label(self.frame, text='Enter Phone Number', font=('bold', 11))
        self.S_Phone_label.grid(row=4, column=0)
        self.S_Email_label = Label(self.frame, text='Enter mail', font=('bold', 11))
        self.S_Email_label.grid(row=6, column=0)
        self.S_Address_label = Label(self.frame, text='Enter Address', font=('bold', 11))
        self.S_Address_label.grid(row=8, column=0)

        # Create Text boxes
        self.USN = Entry(self.frame, width=30)
        self.USN.grid(row=0, column=1, padx=20)
        self.S_Name = Entry(self.frame, width=30)
        self.S_Name.grid(row=2, column=1)
        self.S_Phone = Entry(self.frame, width=30)
        self.S_Phone.grid(row=4, column=1)
        self.S_Email = Entry(self.frame, width=30)
        self.S_Email.grid(row=6, column=1)
        self.S_Address = Entry(self.frame, width=30)
        self.S_Address.grid(row=8, column=1)


        # Submit button
        self.submit_btn = Button(self.frame, text='Submit your Profile', font=('Italic', 12), command=self.submit)
        self.submit_btn.grid(row=0, column=2, columnspan=1, padx=10, pady=10, ipadx=100)

        # Delete button
        self.delete_btn = Button(self.frame, text='Delete Profile', font=('Italic', 12), command=self.DelProfile)
        self.delete_btn.grid(row=2, column=2, columnspan=1, padx=10, pady=10, ipadx=118)

        # Query Button
        self.query_btn = Button(self.frame, text='Show Profile', font=('Italic', 12), command=self.GetProfile)
        self.query_btn.grid(row=4, column=2, columnspan=1, padx=10, pady=10, ipadx=122)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='go back', command=self.back)
        self.cancel_btn.grid(row=5,column=2, columnspan=1)

    def back(self):
        self.frame.destroy()
        self.root=root
        self.another=Records(self.root)


        # database connection
        # conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        # print('sql db initialized')


    # Submit fn
    def submit(self):
        # global USN, S_Name, S_Phone, S_Email, S_Address
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
            sql = "Insert into student(USN, S_Name, S_Phone, S_Email, S_Address, User_id) values (%s,%s,%s,%s,%s,%s)"
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
        if (self.usn == " " ):
            messagebox.showinfo("Delete Status", "USN not found")
        else:
            conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
            # mydb.cmd_debug()
            c = conn.cursor()
            #sql = "DELETE FROM student WHERE USN=%s"
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

        # list box
        self.list_box = Listbox(self.frame)
        self.list_box.grid(row=10,column=1)

        conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = conn.cursor()
        c.execute('Select USN from student')
        USN = c.fetchall()
        for i in USN:
            self.list_box.insert(END, i)


        def view():
            cur = conn.cursor()
            pointer = self.list_box.get(ANCHOR)
            query = f"Select * from student where USN = '{pointer[0]}'"
            cur.execute(query)
            records = c.fetchall()
            precord = records[0]
            cur.close()

            #unpack the tuple
            t_usn, t_name, t_phone, t_email, t_add = precord

            stuDetails = f''' 
                    USN: {t_usn}
                    S_name: {t_name}
                    S_phone: {t_phone}
                    S_Email: {t_email}
                    S_Address: {t_add}
                    
            '''

            self.view_label.config(text=textwrap.dedent(stuDetails))

        def delete():
            self.list_box.delete(ANCHOR)
            self.view_label.config(text='')

        conn.commit()

        # button to view student records
        self.viewitems = Button(self.frame, text='View', command=view)
        self.viewitems.grid(row=12, column=1)

        # creating a delete command for the list
        self.deletelist = Button(self.frame, text='Delete', command=delete)
        self.deletelist.grid(row=12,column=2)

        # label to get the details
        self.view_label = Label(self.frame, text='',bg='yellow')
        self.view_label.grid(row=14, column=1)


class FacultyRec:
    def __init__(self, root):
        self.root = root
        self.root.title('FacultyRecords')
        self.root.geometry('600x400')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create Text Box Labels
        self.F_id_label = Label(self.frame, text='Enter Faculty Id', font=('bold', 11))
        self.F_id_label.grid(row=0, column=0)
        self.F_Name_label = Label(self.frame, text='Enter Faculty Name', font=('bold', 11))
        self.F_Name_label.grid(row=2, column=0)
        self.F_Phone_label = Label(self.frame, text='Enter Phone Number', font=('bold', 11))
        self.F_Phone_label.grid(row=4, column=0)
        self.F_Email_label = Label(self.frame, text='Enter mail', font=('bold', 11))
        self.F_Email_label.grid(row=6, column=0)
        self.F_Address_label = Label(self.frame, text='Enter Address', font=('bold', 11))
        self.F_Address_label.grid(row=8, column=0)

        # Create Text boxes
        self.F_id = Entry(self.frame, width=30)
        self.F_id.grid(row=0, column=1, padx=20)
        self.F_Name = Entry(self.frame, width=30)
        self.F_Name.grid(row=2, column=1)
        self.F_Phone = Entry(self.frame, width=30)
        self.F_Phone.grid(row=4, column=1)
        self.F_Email = Entry(self.frame, width=30)
        self.F_Email.grid(row=6, column=1)
        self.F_Address = Entry(self.frame, width=30)
        self.F_Address.grid(row=8, column=1)

        # Submit button
        self.submit_btn = Button(self.frame, text='Submit your Profile', font=('Italic', 12), command=self.submit)
        self.submit_btn.grid(row=0, column=2, columnspan=1, padx=10, pady=10, ipadx=100)

        # Delete button
        self.delete_btn = Button(self.frame, text='Delete Profile', font=('Italic', 12), command=self.DelProfile)
        self.delete_btn.grid(row=2, column=2, columnspan=1, padx=10, pady=10, ipadx=118)

        # Query Button
        self.query_btn = Button(self.frame, text='Show Profile', font=('Italic', 12), command=self.GetProfile)
        self.query_btn.grid(row=4, column=2, columnspan=1, padx=10, pady=10, ipadx=122)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='go back', command=self.back)
        self.cancel_btn.grid(row=5, column=2, columnspan=1)

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
            # mydb.cmd_debug()
            c = conn.cursor()
            # sql = "DELETE FROM student WHERE USN=%s"
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

        # list box
        self.list_box = Listbox(self.frame)
        self.list_box.grid(row=10, column=1)

        conn = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = conn.cursor()
        c.execute('Select F_id from Faculty')
        FacId = c.fetchall()
        for i in FacId:
            self.list_box.insert(END, i)

        def view():
            cur = conn.cursor()
            pointer = self.list_box.get(ANCHOR)
            query = f"Select * from faculty where F_id = '{pointer[0]}'"
            cur.execute(query)
            records = c.fetchall()
            precord = records[0]
            cur.close()

            # unpack the tuple
            t_fid, t_fname, t_fphone, t_femail, t_fadd = precord

            stuDetails = f''' 
                     F_id : {t_fid}
                    F_Name : {t_fname}
                    F_phone : {t_fphone}
                    F_Email : {t_femail}
                    F_Address : {t_fadd}

            '''

            self.view_label.config(text=textwrap.dedent(stuDetails))

        def delete():
            self.list_box.delete(ANCHOR)
            self.view_label.config(text='')

        conn.commit()

        # button to view student records
        self.viewitems = Button(self.frame, text='View', command=view)
        self.viewitems.grid(row=12, column=1)

        # creating a delete command for the list
        self.deletelist = Button(self.frame, text='Delete', command=delete)
        self.deletelist.grid(row=12, column=2)

        # label to get the details
        self.view_label = Label(self.frame, text='', bg='yellow')
        self.view_label.grid(row=14, column=1)


class AddBranch:
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x400')
        self.root.title('Add Branch')
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.config(background='white')

        # creating Text Labels
        self.Branch_Name_label = Label(self.frame, text='Select Branch Name')
        self.Branch_Name_label.grid(row=1, column=0)
        self.USN_label = Label(self.frame, text='Select Valid USN:')
        self.USN_label.grid(row=2, column=0)
        self.F_id_label = Label(self.frame, text='Select Valid Faculty Id:')
        self.F_id_label.grid(row=3, column=0)

        # creating a Create button
        self.create_btn = Button(self.frame, text='Register', bg='cyan', command=self.create)
        self.create_btn.grid(row=4, column=1, padx=10, pady=10)

        #dropdown for Branch Name
        self.options = [
            "Computer Science",
            "Electronics",
            "Mechanical",
            "Information Science"
        ]
        self.clicked = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked, *self.options)
        self.drop.grid(row=1, column=1, columnspan=2)

        #drop down for USN
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select USN from Student"
        c.execute(sql)
        records = c.fetchall()
        mydb.commit()
        self.options1 = list(item[0] for item in records)
        self.clicked1 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked1, *self.options1)
        self.drop.grid(row=2, column=1)

        #drop down for Fac_id
        mydb = ms.connect(host='localhost', user='root', passwd='Shrey@145', database='sams')
        c = mydb.cursor()
        sql = "Select F_id from Faculty"
        c.execute(sql)
        result = c.fetchall()
        mydb.commit()
        self.options = list(item[0] for item in result)
        self.clicked2 = StringVar()

        self.drop = OptionMenu(self.frame, self.clicked2, *self.options)
        self.drop.grid(row=3, column=1, columnspan=2)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='go back', command=self.back)
        self.cancel_btn.grid(row=5, column=2, columnspan=1)

    def back(self):
        self.frame.destroy()
        self.root = root
        self.another = Records(self.root)

    def create(self):
        self.Branch_Name = self.clicked.get()
        self.USN = self.clicked1.get()
        self.Fac_id = self.clicked2.get()
        records = ( self.Branch_Name, self.USN, self.Fac_id)
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
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x500')
        self.root.title('Course')

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.config(background='white')

        self.C_id_label = Label(self.frame, text='Enter Course Id : ')
        self.C_id_label.grid(row=0, column=0)
        self.C_Name_label = Label(self.frame, text='Enter Course Name :')
        self.C_Name_label.grid(row=1, column=0)
        self.USN_label = Label(self.frame, text='Enter Valid USN :')
        self.USN_label.grid(row=2, column=0)
        self.F_id_label = Label(self.frame, text='Enter Valid Faculty Id :')
        self.F_id_label.grid(row=3, column=0)

        self.C_id = Entry(self.frame, width=30)
        self.C_id.grid(row=0, column=1, padx=10)
        self.C_Name = Entry(self.frame, width=30)
        self.C_Name.grid(row=1, column=1, padx=10)

        self.create_btn = Button(self.frame, text='Register', bg='cyan', command=self.create)
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
        self.drop.grid(row=2, column=1)

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
        self.drop.grid(row=3, column=1, columnspan=2)

        # go back
        self.cancel_btn = tk.Button(self.frame, text='go back', command=self.back)
        self.cancel_btn.grid(row=5, column=2, columnspan=1)

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