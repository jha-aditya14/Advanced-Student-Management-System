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

        bg_color ="black"
        
        #-----------F1----------------------------------------------------------------------------------------------------
    
        self.clock_icon=ImageTk.PhotoImage(file="img//Clock_Dark.png")
        self.student_icon=ImageTk.PhotoImage(file="img//images (1).jpg")


        self.icon1=ImageTk.PhotoImage(file="img//download.jpg")
        self.icon2=ImageTk.PhotoImage(file="img//download (1).png")
        self.icon3=ImageTk.PhotoImage(file="img//download.png")
        self.icon4=ImageTk.PhotoImage(file="img//images.jpg")
        self.icon5=ImageTk.PhotoImage(file="img//linked_in.png")

        
        self.home_icon=ImageTk.PhotoImage(file="img//Home_dark.png")
        self.mangEmp_icon=ImageTk.PhotoImage(file="img//Manage_Emp_dark.png")
        self.mangStd_icon=ImageTk.PhotoImage(file="img//Manage_Student_dark.png")
        self.ViewStd_icon=ImageTk.PhotoImage(file="img//View_Std_dark.png")
        self.viewall_icon=ImageTk.PhotoImage(file="img//View_All_dark.png")
        
        self.change_pasw_icon=ImageTk.PhotoImage(file="img//Reset_dark.png")
        self.exit_icon=ImageTk.PhotoImage(file="img//Exit_dark.png")


        self.CPwin_icon=ImageTk.PhotoImage(file="img//C_pasw_dark.png")
        
        self.val=IntVar() 
        self.val.set("2")

        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )
        lbl = Label(F1,text="Student Management System", fg="white",bg=bg_color, font= ("times new roman",25,"bold")).place(x=120, y=15)

        R1 = Radiobutton(F1,fg="white", text="Light Mode",bg="black",value=1,variable=self.val,command=self.light)
        R1.place(x=700,y=20)
        R2 = Radiobutton(F1, text="Dark Mode", bg="black",variable=self.val,value=2,command=self.dark)
        R2.place(x=700,y=40)
        R3 = Label(F1, fg="white",text="Dark Mode", bg="black")
        R3.place(x=720,y=42)
        self.font=("times new roman",20,"bold")
        self.calendar = []

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"),bg="black", locale='en_GB',state="readonly", width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")
        #print (self.calendar)

        self.time_string = time.strftime('(%H:%M:%S:%p)')
        time1 = Label(F1,text=self.time_string,font=("times new roman",15,"bold"),bg="black",fg="white")
        time1.place(x=850,y=40)
        time2 = Label(F1,image=self.clock_icon,bg=bg_color)
        time2.place(x=820,y=40)

        lbl2 = Label(F1,text="CodewithAJ@",font=("times new roman",15),fg="white",bg=bg_color)
        lbl2.place(x=1050,y=0)

        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black",command=self.logout).place(x=1145,y=50,anchor="w")

        lbl2 = Label(F1,image=self.student_icon,bg=bg_color)
        lbl2.place(x=25,y=0)

#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F2-------------------------------------------------------------------------------------------

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
        
        
        btn_home = Button(F21,image= self.home_icon,relief=RAISED,bg="black",width =115,height=77,command=self.home).place(x=0,y=37,anchor="w")
        btn_mangEmp = Button(F22,image= self.mangEmp_icon,relief=RAISED,width =115,height=77,bg="black",command=self.Emp_Manag ).place(x=0,y=37,anchor="w")
        btn_lmandStd = Button(F23,relief=RAISED,image=self.mangStd_icon,bg="black",width =115,height=77,command=self.Std_Manag ).place(x=0,y=37,anchor="w")
        btn_viewstd = Button(F24,relief=RAISED,width =115,height=77,bg="black",image=self.ViewStd_icon,command=self.Stdview ).place(x=0,y=37,anchor="w")
        btn_viewall = Button(F25,relief=RAISED,width =115,height=77,bg="black", image=self.viewall_icon,command=self.view_all).place(x=0,y=37,anchor="w")
        btn_changepas = Button(F26,relief=RAISED,width =115,height=77,bg="black",image=self.change_pasw_icon,command=self.change_pasw ).place(x=0,y=37,anchor="w")
        btn_Exit = Button(F27,relief=RAISED,width =115,height=77,bg="black", image=self.exit_icon,command=self.Exit).place(x=0,y=37,anchor="w")



#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------


        F3 = Frame(self.root,bd=5,relief=GROOVE,bg="black")
        F3.place(x=150,y=100,relwidth=1,height=60 )
        lbl_1= Label(F3,text="Dashboard / Admin",fg="white",font=("comic sans",25,"italic"),bg="black")
        lbl_1.place(x=0,y=5)

#-----------------Main Screen Frames---------------------------------
        F4 = LabelFrame(self.root,bd=5,relief=FLAT,bg="grey")
        F4.place(x=390,y=230,width=700,height=400 )
        lbl_4= Label(F4,image=self.CPwin_icon,font=("comic sans",15,"italic"))
        lbl_4.place(x=265,y=20)

#--------------------Variable---------------------------
        self.contact=StringVar()
        self.opasw=StringVar()
        self.npasw=StringVar()
        #self.contact.set("Contact Number")
        
        lbl6 = Label(F4, text = "Contact No.",bg="grey", font= ("times new roman",20,"bold")).place(x=115,y=180,anchor="w")
        txtu = Entry(F4,bd=5,textvariable=self.contact, relief = GROOVE,font=("",15)).place(x=300,y=180,anchor="w")
        
        
        lbl7 = Label(F4, text = "Old Password", bg="grey",font= ("times new roman",20,"bold")).place(x=115,y=230,anchor="w")
        txtp = Entry(F4,bd=5,textvariable=self.opasw,show="*",relief = GROOVE,font=("",15)).place(x=300,y=230,anchor="w")
        
        lbl7 = Label(F4, text = "New Password",bg="grey", font= ("times new roman",20,"bold")).place(x=115,y=280,anchor="w")
        txtp = Entry(F4,bd=5,textvariable=self.npasw,show="*",relief = GROOVE,font=("",15)).place(x=300,y=280,anchor="w")

        btn_update = Button(F4,relief=RAISED,bg="#000080",text="Change",font=("",15,"bold"),fg="yellow",height=1,width =14,command=self.Update).place(x=350,y=330,anchor="w")


    def Update(self):
        if self.contact.get()=="" or self.npasw.get()=="" or self.opasw.get=="":
            messagebox.showerror("Error!","All field should be filled")

        elif len(str(self.npasw.get()))<8:
            messagebox.showerror("Error!","Minimun 8 characters required")

        else:
            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            self.c.execute("SELECT * from admin WHERE contact="+str(self.contact.get()))
            self.data=self.c.fetchall()
            #print(50*"&")
            #print(self.data)
            #print(self.data)
            if self.data:
                for i in self.data:
                    print(i)
                a=(str(i[4])) 
                print (a)
                print(type(a)) 
                print(type(self.opasw.get()))  
                print(type(self.npasw.get()))  
                if a==self.opasw.get():
                    a=self.opasw.get()
                    b=self.contact.get()
                    print(a)
                    print(b)
                    print("True")
                    y="UPDATE admin SET pasw="+self.npasw.get()
                    y=y+" WHERE contact="+self.contact.get()
                    print(str(y))              
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    return messagebox.showinfo("Info","Successfully Changed!!")
                else:
                    return messagebox.showinfo("Info","Password Cann't Changed current password may not match!!")

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
        import M_Emp_Dark

    def home(self):
        self.root.destroy()
        import darkMode.Home_Dark as Home_Dark

    def Std_Manag(self):
        self.root.destroy()
        import Std_Manag_Dark

    def change_pasw(self):
        pass

    def Stdview(self):
        self.root.destroy()
        import Std_View_Dark

    def view_all(self):
        self.root.destroy()
        import View_all_dark
    
    def Exit(self):
        self.root.destroy()

            
    def dark(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply dark mode")
        if a>0:
            self.root.destroy()
            import C_pasw_dark
        else:
            pass

    def light(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply light mode")
        if a>0:
            self.root.destroy()
            import os
            sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
            from C_pasw import C_pasw
        else:
            pass
            
#create Window    
root = Tk()
obj = win1(root)
root.mainloop()
