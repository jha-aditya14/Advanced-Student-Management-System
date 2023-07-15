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
#self.F2 = ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download1.jpeg") # here we store image to a variable using PIL module help 

class win1:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System".center(420))  # title for Window 
        self.root.configure(background = "black")  # background color for window 
        self.root.geometry("1360x768+0+0")

        bg_color ="#FFFFF6"
        
        #-----------F1----------------------------------------------------------------------------------------------------
        self.bg_icon = ImageTk.PhotoImage(file="ASMS_Project_Folder//img//1222596.jpg")
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window
        self.clock_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download (2).png")
        self.student_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//images (1).jpg")

        #----------------------------------------------------------------

        self.home_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Home.png")
        self.mangEmp_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Manage_Emp.png")
        self.mangStd_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Manage_Stud.png")
        self.ViewStd_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//View_Stud.png")
        self.viewall_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//View.jpg")
        
        self.change_pasw_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Change_pasw.png")
        self.exit_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Exit.png")

        

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
        lbl_1= Label(F3,text="Dashboard / Employee",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

#-----------------Main Screen Frames---------------------------------
        self.conn=sqlite3.connect("sdms.db")
        self.c=self.conn.cursor()
        

        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,bg="#DC143C")
        F4.place(x=300,y=170,width=400,height=250 )

        F41 = LabelFrame(F4,bd=5,relief=SUNKEN,bg="#DC143C")
        F41.place(x=0,y=0,width=380,height=60 )
        lbl_2= Label(F41,text="Total Students",bg="#DC143C",font=("times new roman",25,"bold"),fg="White")
        lbl_2.place(x=0,y=0)

        
        F42 = LabelFrame(F4,bd=5,relief=GROOVE)
        F42.place(x=0,y=60,width=380,height=180 )

        text1=Text(F42,bd=5, font=("times new roman",30,"bold"))
        self.c.execute("SELECT COUNT(*) FROM Std")
        self.results1 = ((self.c).fetchall())        
        text1.insert(INSERT,("\n             Total\n         Students: "))
        text1.insert(INSERT,self.results1)
        text1.place(x=0,y=0,width=370,height=170)
        text1.configure(state="disabled")


        F5 = LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=800,y=170,width=400,height=250 )

        F51 = LabelFrame(F5,bd=5,relief=SUNKEN, bg="#3B9C9C")
        F51.place(x=0,y=0,width=380,height=60 )
        lbl_3= Label(F51,text="Last Login",bg="#3B9C9C",font=("times new roman",30,"bold"),fg="White")
        lbl_3.place(x=0,y=0)

        
        F52 = LabelFrame(F5,bd=5,relief=GROOVE)
        F52.place(x=0,y=60,width=380,height=180 )

        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        text2=Text(F52,bd=5, fg="white",font=("times new roman",15,"bold"),bg="#151B54")
        self.c.execute("SELECT * FROM Last_Login1 WHERE email =\""+str(self.read1)+"\"")
        self.results2 = ((self.c).fetchall())        
        text2.insert(INSERT,(""))
        if self.results2:
            for i in self.results2:
                print(i)    
            #self.EmpID.set(i[0])  
            text2.insert(INSERT,("Name                   :   "+str(i[1])+" "))
            text2.insert(INSERT,(str(i[2])+"\n"))
            text2.insert(INSERT,("Joined On            :   "+str(i[3])+"\n"))
            text2.insert(INSERT,("Email                   :   "+str(i[4])+"\n"))
            text2.insert(INSERT,("Last Login Time :   "+str(i[5])+"\n"))
            text2.insert(INSERT,("Last Login Date :   "+str(i[6])+"\n"))

            text2.place(x=0,y=0,width=370,height=170)
            text2.configure(state="disabled")

        
        
        F6 = LabelFrame(self.root,bd=10,relief=GROOVE)
        F6.place(x=300,y=450,width=400,height=250 )

        F61 = LabelFrame(F6,bd=5,relief=SUNKEN,bg="black")
        F61.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F61,text="Total Employees",bg="black",font=("times new roman",30,"bold"),fg="White")
        lbl_4.place(x=0,y=0)


        F62 = LabelFrame(F6,bd=5,relief=GROOVE)
        F62.place(x=0,y=60,width=380,height=180 )

        text3=Text(F62,bd=5, fg="white",font=("times new roman",30,"bold"),bg="#151B54")
        self.c.execute("SELECT COUNT(*) FROM Emp")
        self.results3 = ((self.c).fetchall())        
        text3.insert(INSERT,("\n             Total\n         Employees: "))
        text3.insert(INSERT,self.results3)
        text3.place(x=0,y=0,width=370,height=170)
        text3.configure(state="disabled")

        
        
        F7 = LabelFrame(self.root,bd=10,relief=GROOVE)
        F7.place(x=800,y=450,width=400,height=250 )
        
        F71 = LabelFrame(F7,bd=5,relief=SUNKEN,bg="white")
        F71.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F71,text="Developer",bg="white",font=("times new roman",30,"bold"),fg="#DC143C")
        lbl_4.place(x=0,y=0)


        F72 = LabelFrame(F7,bd=5,relief=RAISED)
        F72.place(x=0,y=60,width=380,height=180 )

        text7=Text(F72,bd=5,fg="white",font=("times new roman",15, "italic"), bg="#DC143C",relief=GROOVE)
        text7.insert(INSERT,("                       Developed By\n\n   Aditya Jha \n   Email Id:aj147ps@gmail.com\n   Email Id:gauravgupta1999kr@gmail.com\n   Follow on #codewithajofficial on insta "))
        text7.place(x=0,y=0,width=370,height=170)
        text7.configure(state="disabled")




    def logout(self):
        self.read1=StringVar()
        with open("Temp1.txt","r+") as file:
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
            y="UPDATE Last_Login1 set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where email =\""+str(self.read1)+"\""
            print(y)
            self.c.execute(y)
            self.conn.commit()
            import logine
        else:
            pass

    
    def home(self):
        pass

    def Emp_Manag(self):
        self.root.destroy()
        import M_Emp_emp

    def Std_Manag(self):
        self.root.destroy()
        import M_Std_emp

    def view_all(self):
        self.root.destroy()
        import View_all_emp

    def Stdview(self):
        self.root.destroy()
        import Std_view_emp

    def change_pasw(self):
        self.root.destroy()
        import C_pasw_emp
    
    def Exit(self):
        self.root.destroy()
            
    def dark(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply dark mode")
        if a>0:
            self.root.destroy()
            import darkMode.Home_Emp_Dark
        else:
            pass

    def light(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply light mode")
        if a>0:
            self.root.destroy()
            import Home_Emp as Home_Emp
        else:
            pass
#create Window    
root = Tk()
obj = win1(root)
root.mainloop()
