from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import random
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code

#--------
#self.F2 = ImageTk.PhotoImage(file="img//download1.jpeg") # here we store image to a variable using PIL module help 

class win1:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System".center(420))  # title for Window 
        self.root.configure(background = "black")  # background color for window 
        self.root.geometry("1360x768+0+0")

        bg_color ="#FFFFF6"
        
        #-----------F1----------------------------------------------------------------------------------------------------
        self.bg_icon = ImageTk.PhotoImage(file="img//1222596.jpg")
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window
        self.clock_icon=ImageTk.PhotoImage(file="img//download (2).png")
        self.student_icon=ImageTk.PhotoImage(file="img//images (1).jpg")

        #----------------------------------------------------------------

        self.home_icon=ImageTk.PhotoImage(file="img//Home.png")
        self.mangEmp_icon=ImageTk.PhotoImage(file="img//Manage_Emp.png")
        self.mangStd_icon=ImageTk.PhotoImage(file="img//Manage_Stud.png")
        self.ViewStd_icon=ImageTk.PhotoImage(file="img//View_Stud.png")
        self.viewall_icon=ImageTk.PhotoImage(file="img//View.jpg")
        
        self.change_pasw_icon=ImageTk.PhotoImage(file="img//Change_pasw.png")
        self.exit_icon=ImageTk.PhotoImage(file="img//Exit.png")

        #-------------------------Variables------------------------------
        self.searchby = StringVar()
        

        self.val=IntVar() 
        self.val.set("1")

        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )
        lbl = Label(F1,text="Student Management System", bg=bg_color, font= ("times new roman",25,"bold")).place(x=120, y=15)

        R1 = Radiobutton(F1, text="Light Mode",bg=bg_color,value=1,variable=self.val,command=self.light)
        R1.place(x=700,y=20)
        R2 = Radiobutton(F1, text="Dark Mode",bg=bg_color, variable=self.val,value=2,command=self.dark)
        R2.place(x=700,y=40)


        self.font=("times new roman",20,"bold")
        self.calendar = []

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly", width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")
        #print (self.calendar)

        self.time_string = time.strftime('(%H:%M:%S:%p)')
        time1 = Label(F1,text=self.time_string,font=("times new roman",15,"bold"),bg=bg_color)
        time1.place(x=850,y=40)
        time2 = Label(F1,image=self.clock_icon,bg=bg_color)
        time2.place(x=820,y=40)

        lbl2 = Label(F1,text="CodewithAJ@",font=("times new roman",15),bg=bg_color)
        lbl2.place(x=1050,y=0)

        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black",command=self.logout).place(x=1145,y=50,anchor="w")

        lbl2 = Label(F1,image=self.student_icon,bg=bg_color)
        lbl2.place(x=25,y=0)

     #----------------------------------F2------------------------------------
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=640 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=90 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=90,width=130,height=90 )
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=180,width=130,height=90 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=270,width=130,height=90 )
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=360,width=130,height=90 )
         
        F26 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F26.place(x=0,y=450,width=130,height=90 )
        
        F27 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F27.place(x=0,y=540,width=130,height=90 )
        
        
        btn_home = Button(F21,image= self.home_icon,relief=RAISED,width =115,height=77,command=self.home).place(x=0,y=37,anchor="w")
        btn_mangEmp = Button(F22,image= self.mangEmp_icon,relief=RAISED,width =115,height=77,command=self.Emp_Manag ).place(x=0,y=37,anchor="w")
        btn_lmandStd = Button(F23,relief=RAISED,image=self.mangStd_icon,width =115,height=77,command=self.Std_Manag ).place(x=0,y=37,anchor="w")
        btn_viewstd = Button(F24,relief=RAISED,width =115,height=77,image=self.ViewStd_icon,command=self.Stdview ).place(x=0,y=37,anchor="w")
        btn_viewall = Button(F25,relief=RAISED,width =115,height=77, image=self.viewall_icon,command=self.view_all).place(x=0,y=37,anchor="w")
        btn_changepas = Button(F26,relief=RAISED,width =115,height=77,image=self.change_pasw_icon,command=self.change_pasw ).place(x=0,y=37,anchor="w")
        btn_Exit = Button(F27,relief=RAISED,width =115,height=77, image=self.exit_icon,command=self.Exit).place(x=0,y=37,anchor="w")



        
#------------------------------F3--------------------------------
        F3 = LabelFrame(self.root,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / Admin",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

#-----------------Main Screen Frames---------------------------------
        
        self.F4 =Frame(self.root,bd=10,relief=SUNKEN,bg="white")
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        lb_search=Label(self.root,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=185, anchor="w")
        combo_search=ttk.Combobox(self.root, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("Employee_Table","Student_Table")
        combo_search.place(x=273, y=185, anchor="w")

        lb_search_btn=Button(self.root,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=485 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self.root,text="Clear", bd=6, relief=GROOVE,command=self.clear,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=183, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE)
        Table_Frame.place(x=15,y=0,width=1080,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x1=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y1=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Std_ID" ,"First_name"  , "Last_name"  , "Roll", "code"  , "contact"  , "country" , "Class"  , "address"  , "Department"  , "DOB" , "Email"  , "Semester"  , "Gender"  , "L_URL" ,"F_URL","PIC_LINK"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.Employee_table = ttk.Treeview(Table_Frame,columns=("EmpID" ,"first_name"  , "last_name"  , "emp_code", "pasw"  , "Role"  , "email"  , "gender","code","contact","country" ,  "address"  , "Joining"  , "Time1"   , "L_URL" ,"T_URL","I_URL","F_URL","Y_URL","PIC_LINK"   ),xscrollcommand=scroll_x1.set, yscrollcommand=scroll_y1.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        scroll_x1.pack(side=BOTTOM,fill=X)
        scroll_y1.pack(side=RIGHT,fill=Y)
        scroll_x1.config(command=self.Employee_table.xview)
        scroll_y1.config(command=self.Employee_table.yview)

        self.Student_table.heading("Std_ID", text="Student_ID")
        self.Student_table.heading("First_name", text="First_name")
        self.Student_table.heading("Last_name", text="Last_Name")
        self.Student_table.heading("Roll", text="Roll_No")
        self.Student_table.heading("code", text="Phn.Code")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("country", text="Country")
        self.Student_table.heading("Class", text="Class")
        self.Student_table.heading("address", text="Address")
        self.Student_table.heading("Department", text="Department")
        self.Student_table.heading("DOB", text="D.O.B")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Semester", text="Semester")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("L_URL", text="L_URL")
        self.Student_table.heading("F_URL", text="F_URL")
        self.Student_table.heading("PIC_LINK", text="PictureLink")

        
        self.Employee_table.heading("EmpID", text="Employee_ID")
        self.Employee_table.heading("first_name", text="First_name")
        self.Employee_table.heading("last_name", text="Last_Name")
        self.Employee_table.heading("emp_code", text="Employee_Code")
        self.Employee_table.heading("pasw", text="Password")
        self.Employee_table.heading("Role", text="Role")
        self.Employee_table.heading("email", text="Email")
        self.Employee_table.heading("gender", text="Gender")
        self.Employee_table.heading("code", text="Code")
        self.Employee_table.heading("contact", text="Contact")
        self.Employee_table.heading("country", text="Country")
        self.Employee_table.heading("address", text="Address")
        self.Employee_table.heading("Joining", text="Joining_Date")
        self.Employee_table.heading("Time1", text="Joining_Time")
        self.Employee_table.heading("L_URL", text="L_URL")
        self.Employee_table.heading("T_URL", text="T_URL")
        self.Employee_table.heading("I_URL", text="I_URL")
        self.Employee_table.heading("F_URL", text="F_URL")
        self.Employee_table.heading("Y_URL", text="Y_URL")
        self.Employee_table.heading("PIC_LINK", text="PictureLink")

        self.Student_table.column("Std_ID", width=150)
        self.Student_table.column("First_name", width=150)
        self.Student_table.column("Last_name", width=150)
        self.Student_table.column("Roll", width=140)
        self.Student_table.column("code", width=70)
        self.Student_table.column("contact", width=120)
        self.Student_table.column("country", width=70)
        self.Student_table.column("Class", width=70)
        self.Student_table.column("address", width=400)
        self.Student_table.column("Department", width=170)
        self.Student_table.column("DOB", width=80)
        self.Student_table.column("Email", width=150)
        self.Student_table.column("Semester", width=70)
        self.Student_table.column("Gender", width=80)
        self.Student_table.column("L_URL", width=200)
        self.Student_table.column("F_URL", width=200)
        self.Student_table.column("PIC_LINK", width=300)     
    
        self.Student_table['show']='headings'

        self.Employee_table.column("EmpID", width = 150)
        self.Employee_table.column("first_name", width = 150)
        self.Employee_table.column("last_name", width = 150)
        self.Employee_table.column("emp_code", width = 140)
        self.Employee_table.column("pasw", width = 70)
        self.Employee_table.column("Role", width = 120)
        self.Employee_table.column("email", width = 150)
        self.Employee_table.column("gender", width = 80)
        self.Employee_table.column("code", width = 70)
        self.Employee_table.column("contact", width = 120)
        self.Employee_table.column("country", width = 70)
        self.Employee_table.column("address", width = 400)
        self.Employee_table.column("Joining", width = 100)
        self.Employee_table.column("Time1", width = 100)
        self.Employee_table.column("L_URL", width = 200)
        self.Employee_table.column("T_URL", width = 200)
        self.Employee_table.column("I_URL", width = 200)
        self.Employee_table.column("F_URL", width = 200)
        self.Employee_table.column("Y_URL", width = 200)
        self.Employee_table.column("PIC_LINK", width = 300)

        self.Employee_table['show']='headings'
        #---------------------------------F4--------------------------------------
       

    def search(self):
        
        if self.searchby.get() == "":
            messagebox.showerror("Error","Searhby Field Should be filled")
        
        elif self.searchby.get() == "Student_Table":
            #self.Employee_table.delete(*self.Employee_table.get_children())
            #elf.Student_table.delete(*self.Student_table.get_children())
            self.Employee_table.pack_forget()
            self.Student_table.pack(fill=BOTH,expand=1)
            self.Student_table.bind("<ButtonRelease-1>",self.getcursor)
            self.fetch_data()
        elif self.searchby.get() == "Employee_Table":
            #self.Employee_table.delete(*self.Employee_table.get_children())
            #self.Student_table.delete(*self.Student_table.get_children())
            self.Student_table.pack_forget()
            self.Employee_table.pack(fill=BOTH,expand=1)
            self.Employee_table.bind("<ButtonRelease-1>",self.getcursor1)
            self.fetch_data1()
        else:
            messagebox.showerror("Error","Something Wrong")


    def logout(self):
        self.read1=StringVar()
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%Y-%m-%d")
            self.root.destroy()
            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where email =\""+str(self.read1)+"\""
            print(y)
            self.c.execute(y)
            self.conn.commit()
            import login
        else:
            pass

 

    def Emp_Manag(self):
        self.root.destroy()
        import M_Emp

    def home(self):
        self.root.destroy()
        import Home

    def Std_Manag(self):
        self.root.destroy()
        import M_Std

    def view_all(self):
        pass

    def Stdview(self):
        self.root.destroy()
        import Std_view

    def change_pasw(self):
        self.root.destroy()
        import C_pasw
    
    def Exit(self):
        self.root.destroy()
            

    def fetch_data(self):
        self.conn=sqlite3.connect("sdms.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Std")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Student_table.focus()
        Content=self.Student_table.item(cursor_row)
        row=Content['values']
        #print(row)
        self.Std_ID.set(row[0])
        self.fname.set(row[1])
        self.lname.set(row[2])
        self.Roll_no.set(row[3])
        self.code.set(row[4])
        self.contact.set(row[5])
        #self.con2(row[6])
        self.class_.set(row[7])
        self.address.set(row[8])
        self.dept.set(row[9])
        self.DOB.set(row[10])
        self.email.set(row[11])
        self.sem.set(row[12])
        self.gender.set(row[13]) 
        self.Lurl.set(row[14])
        self.furl.set(row[15])

    def clear(self):
        self.Employee_table.delete(*self.Employee_table.get_children())
        self.Student_table.delete(*self.Student_table.get_children())
        self.Employee_table.pack_forget()
        self.Student_table.pack_forget()

    def fetch_data1(self):
        self.conn=sqlite3.connect("sdms.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Emp")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Employee_table.delete(*self.Employee_table.get_children())
                for row in rows:
                        self.Employee_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor1(self,ev):
        cursor_row=self.Employee_table.focus()
        Content=self.Employee_table.item(cursor_row)
        row=Content['values']
        #print(row)
        self.Employee_table.set(row[0])
        self.Employee_table.set(row[1])
        self.Employee_table.set(row[2])
        self.Employee_table.set(row[3])
        self.Employee_table.set(row[4])
        self.Employee_table.set(row[5])
        self.Employee_table.set(row[6])        
        self.Employee_table.set(row[7])
        self.Employee_table.set(row[8])
        self.Employee_table.set(row[9])
        self.Employee_table.set(row[10])
        self.Employee_table.set(row[11])
        self.Employee_table.set(row[12])
        self.Employee_table.set(row[14])
        self.Employee_table.set(row[15])
        self.Employee_table.set(row[16])
        self.Employee_table.set(row[17])
        self.Employee_table.set(row[18])
        self.Employee_table.set(row[19])        
        self.Employee_table.set(row[20])

        
    def dark(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply dark mode")
        if a>0:
            self.root.destroy()
            import darkMode.View_all_dark
        else:
            pass

    def light(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply light mode")
        if a>0:
            self.root.destroy()
            import View_all
        else:
            pass

#create Window    
root = Tk()
obj = win1(root)
root.mainloop()
