from tkinter import*
from PIL import ImageTk,Image
import cv2
import imutils
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import random
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import pycountry
import webbrowser
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
from matplotlib import pyplot as plt


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
        self.icon1=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download.jpg")
        self.icon2=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//linked_in.png")
        #----------------------------------------------------------------

        self.home_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Home.png")
        self.mangEmp_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Manage_Emp.png")
        self.mangStd_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Manage_Stud.png")
        self.ViewStd_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//View_Stud.png")
        self.viewall_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//View.jpg")
        
        self.change_pasw_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Change_pasw.png")
        self.exit_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Exit.png")

#-----------------------------------------Variables---------------------------------------------

        self.searchby=StringVar()
        self.fname=StringVar()
        self.lname=StringVar()
        self.Std_Id=StringVar()
        self.class_=StringVar()
        self.Roll_no=StringVar()
        self.email=StringVar()
        self.DOB=StringVar()
        self.code=StringVar()
        self.contact=StringVar()
        self.address=StringVar()
        self.country=StringVar()
        self.Gender=StringVar()
        self.L_Url=StringVar()
        self.F_Url=StringVar()
        self.searchent=StringVar()
        self.link=StringVar()
        self.l1=StringVar()
        self.l2=StringVar()
        

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
        F3.place(x=150,y=100,relwidth=1,height=80 )
        lbl_1= Label(F3,text="Dashboard / Admin",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

        F4 = LabelFrame(F3,bd=5,relief=RAISED)
        F4.place(x=0,y=30,width=1205,height=45 )

        lb_search=Label(F4,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=10 ,y=15, anchor="w")
        
        combo_search=ttk.Combobox(F4, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("Roll_No","Student_ID","Contact")
        combo_search.place(x=100, y=15, anchor="w")

        lb_search=Entry(F4,textvariable=self.searchent, font=("times new roman",15,"bold"))
        lb_search.place(x=320 ,y=15, anchor="w")
        
        lb_search_btn=Button(F4,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=540 ,y=15, height=35,anchor="w")
        
        lb_clear_btn=Button(F4,text="Clear", bd=6, relief=GROOVE,command=self.clear,font=("times new roman",15,"bold"),fg="dark blue",bg="light green")
        lb_clear_btn.place(x=665 ,y=15, width=120,height=35,anchor="w")
        
        lb_close_btn=Button(F4,text="Close", bd=6, relief=GROOVE,command=self.close,font=("times new roman",15,"bold"),fg="white",bg="red")
        lb_close_btn.place(x=795 ,y=15, width=120,height=35,anchor="w")
        

#-----------------Main Screen Frames------------------------------------------------------------------------------
#-----------------Main Screen Frames------------------------------------------------------------------------------
#-----------------Main Screen Frames------------------------------------------------------------------------------
#-----------------Main Screen Frames------------------------------------------------------------------------------
#-----------------Main Screen Frames------------------------------------------------------------------------------

        self.F5 = LabelFrame(self.root,bd=5,relief=FLAT,bg="light gray")
        self.F5.place(x=190,y=190,width=1100,height=500 )

        txt1 = Label(self.F5,text="Student Profile",font=("times new roman",30,"bold"),bg="light gray")
        txt1.place(x=20,y=10 )
        
        seprator1_style = ttk.Style()
        separator1 = ttk.Separator(self.F5, orient='horizontal',style="Line.TSeparator")
        separator1.place(x=20,width=1050,y=70)
        seprator1_style.configure("Line.TSeparator")

        self.F6 = Frame(self.F5,bd=5,relief=SUNKEN,bg="light gray")
        self.F6.place(x=20,y=100,width=215,height=200 )

        txt2 = Label(self.F6,text="Student ID: ",width=20,anchor="w",font=("times new roman",13,"bold"),bg="gray")
        txt2.place(x=0,y=165)
        txt2_lbl = Entry(self.F6,width=12,state="readonly",textvariable=self.Std_Id,font=("times new roman",13,"bold"),bg="gray")
        txt2_lbl.place(x=90,y=165)


        txt_lbl = Label(self.F5,text="Social Links ",font=("times new roman",30,"bold"),bg="light gray")
        txt_lbl.place(x=20,y=310)

      
             
        self.F7 = Frame(self.F5,bd=5,relief=SUNKEN,bg="light gray")
        self.F7.place(x=270,y=100,width=345,height=250 )

        txt3 = Label(self.F7,text="Personal Details ",width=33,anchor="w",font=("times new roman",13,"bold"),bg="gray")
        txt3.place(x=0,y=0)

        ent1_lbl = Label(self.F7,text="Roll No.",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent1_lbl.place(x=0,y=30)
        ent1_txt = Entry(self.F7,textvariable=self.Roll_no,font=("times new roman",13,"bold"),bg="light gray")
        ent1_txt.place(x=100,y=30)

        ent2_lbl = Label(self.F7,text="Class",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent2_lbl.place(x=0,y=60)
        ent2_txt = Entry(self.F7,textvariable=self.class_,font=("times new roman",13,"bold"),bg="light gray")
        ent2_txt.place(x=100,y=60)

        ent2_lbl = Label(self.F7,text="First Name",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent2_lbl.place(x=0,y=90)
        ent2_txt = Entry(self.F7,textvariable=self.fname,font=("times new roman",13,"bold"),bg="light gray")
        ent2_txt.place(x=100,y=90)

        ent4_lbl = Label(self.F7,text="Last Name",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent4_lbl.place(x=0,y=120)
        ent4_txt = Entry(self.F7,textvariable=self.lname,font=("times new roman",13,"bold"),bg="light gray")
        ent4_txt.place(x=100,y=120)


        ent5_lbl = Label(self.F7,text="Email",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent5_lbl.place(x=0,y=150)
        ent5_txt = Entry(self.F7,textvariable=self.email,font=("times new roman",13,"bold"),bg="light gray")
        ent5_txt.place(x=100,y=150)

        ent6_lbl = Label(self.F7,text="Gender",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent6_lbl.place(x=0,y=180)
        ent6_txt = Entry(self.F7,textvariable=self.Gender,font=("times new roman",13,"bold"),bg="light gray")
        ent6_txt.place(x=100,y=180)

        ent7_lbl = Label(self.F7,text="D.O.B",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent7_lbl.place(x=0,y=210)
        ent7_txt = Entry(self.F7,textvariable=self.DOB,font=("times new roman",13,"bold"),bg="light gray")
        ent7_txt.place(x=100,y=210)

        ent7_lbl = Label(self.F7,text="D.O.B",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent7_lbl.place(x=0,y=210)
        ent7_txt = Entry(self.F7,textvariable=self.DOB,font=("times new roman",13,"bold"),bg="light gray")
        ent7_txt.place(x=100,y=210)

        self.F8 = Frame(self.F5,bd=5,relief=SUNKEN,bg="light gray")
        self.F8.place(x=650,y=100,width=345,height=200 )

        txt4 = Label(self.F8,text="Location ",width=33,anchor="w",font=("times new roman",13,"bold"),bg="gray")
        txt4.place(x=0,y=0)       
       
        ent8_lbl = Label(self.F8,text="Contact",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent8_lbl.place(x=0,y=30)
        ent8_txt = Entry(self.F8,textvariable=self.contact,width=14,font=("times new roman",13,"bold"),bg="light gray")
        ent8_txt.place(x=150,y=30)


        ent9_txt = Entry(self.F8,width=5,textvariable=self.code,font=("times new roman",13,"bold"),bg="light gray")
        ent9_txt.place(x=100,y=30)

        ent10_lbl = Label(self.F8,text="Country",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent10_lbl.place(x=0,y=90)
        ent10_txt = Entry(self.F8,textvariable=self.country,font=("times new roman",13,"bold"),bg="light gray")
        ent10_txt.place(x=100,y=90)

        ent11_lbl = Label(self.F8,text="Address",anchor="w",font=("times new roman",13,"bold"),bg="light gray")
        ent11_lbl.place(x=0,y=150)
        ent11_txt = Entry(self.F8,textvariable=self.address,font=("times new roman",13,"bold"),bg="light gray")
        ent11_txt.place(x=100,y=150)

        btn_Fb = Button(self.F5,relief=RAISED,command=self.link2,image=self.icon1).place(x=80,y=410,anchor="w")
        btn_LI = Button(self.F5,relief=RAISED,command=self.link1,height=23,image=self.icon2).place(x=20,y=410,anchor="w") 


#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------


        seprator2_style = ttk.Style()
        separator2 = ttk.Separator(self.F5, orient='horizontal',style="Line.TSeparator")
        separator2.place(x=20,width=1050,y=370)
        seprator2_style.configure("Line.TSeparator")

    def clear(self):
        self.Std_Id.set("")
        self.searchby.set("")
        self.searchent.set("")
        self.fname.set("")
        self.lname.set("")
        self.Roll_no.set("")
        self.code.set("0")
        self.contact.set("")
        self.country.set("")
        self.class_.set("")
        self.address.set("")
        self.DOB.set("")
        self.email.set("")
        self.Gender.set("")
        self.L_Url.set(self.link1)
        self.F_Url.set(self.link2)
        self.link.set("")
        cv2.destroyAllWindows()
        btn_Fb = Button(self.F5,relief=RAISED,command=self.link2,image=self.icon1).place(x=80,y=410,anchor="w")
        btn_LI = Button(self.F5,relief=RAISED,command=self.link1,height=23,image=self.icon2).place(x=20,y=410,anchor="w")
        self.F6 = Frame(self.F5,bd=5,relief=SUNKEN,bg="light gray")
        self.F6.place(x=20,y=100,width=215,height=200 )

    def close(self):
        self.root.destroy()
        import darkMode.Home_Dark as Home_Dark

    
    def search(self):
        cv2.destroyAllWindows()
        self.conn=sqlite3.connect("sdms.db")
        self.c=self.conn.cursor()
    
        if self.searchby.get() == "Roll_No":
            self.c.execute("SELECT * from Std WHERE Roll="+str(self.searchent.get()))
            self.data=self.c.fetchall()
            #print(50*"&")
            #print(self.data)
            if self.data:
                    for i in self.data:
                        print(i)
                    a=(i[0])
                    self.Std_Id.set(a)
                    self.fname.set(i[1])
                    self.lname.set(i[2])
                    self.Roll_no.set(i[3])
                    self.code.set("+"+str(i[4]))
                    self.contact.set(i[5])
                    self.country.set(i[6])
                    self.class_.set(i[7])
                    self.address.set(i[8])
                    self.DOB.set(i[10])
                    self.email.set(i[11])
                    self.Gender.set(i[13])
                    self.L_Url.set(i[14])
                    self.F_Url.set(i[15])
                    self.link.set(i[16])

                    btn_Fb = Button(self.F5,relief=RAISED,command=self.link12,image=self.icon1).place(x=80,y=410,anchor="w")
                    btn_LI = Button(self.F5,relief=RAISED,command=self.link11,height=23,image=self.icon2).place(x=20,y=410,anchor="w")
                    lbl = Label(self.F5,text="",font=("times now roman",25,"bold"),bg="light gray").place(x=250,y=410,anchor="w")
                    #print((i[16]))
                    
                    import io
                    image_data = i[16]
                    image = Image.open(io.BytesIO(image_data))

                    # Resize the image to fit the desired frame size with anti-aliasing
                    desired_width = 205
                    desired_height = 160
                    image = image.resize((desired_width, desired_height), Image.LANCZOS)

                    self.imag_icon = ImageTk.PhotoImage(image)
                    self.F6 = Frame(self.F5,bd=5,relief=SUNKEN,bg="light gray")
                    self.F6.place(x=20,y=100,width=215,height=200 )
                    lb_pic = Label(self.F6, image=self.imag_icon)
                    lb_pic.place(x=0, y=0, height=desired_height, width=desired_width)    
                    txt2 = Label(self.F6,text="Student ID: ",width=20,anchor="w",font=("times new roman",13,"bold"),bg="gray")
                    txt2.place(x=0,y=165)
                    txt2_lbl = Entry(self.F6,width=12,state="readonly",textvariable=self.Std_Id,font=("times new roman",13,"bold"),bg="gray")
                    txt2_lbl.place(x=90,y=165)
                      
            else:
                return messagebox.showerror("Error","Invalid Roll No.")

        elif self.searchby.get() == "Student_ID":
            self.c.execute("SELECT * from Std WHERE Std_ID="+str(self.searchent.get()))
            self.data=self.c.fetchall()
            #print(50*"&")
            #print(self.data)
            if self.data:
                    for i in self.data:
                        print(i)
                    a=(i[0])
                    self.Std_Id.set(a)
                    self.fname.set(i[1])
                    self.lname.set(i[2])
                    self.Roll_no.set(i[3])
                    self.code.set("+"+str(i[4]))
                    self.contact.set(i[5])
                    self.country.set(i[6])
                    self.class_.set(i[7])
                    self.address.set(i[8])
                    self.DOB.set(i[10])
                    self.email.set(i[11])
                    self.Gender.set(i[13])
                    self.L_Url.set(i[14])
                    self.F_Url.set(i[15])
                    self.link.set(i[16])
                                    
                    btn_Fb = Button(self.F5,relief=RAISED,command=self.link12,image=self.icon1).place(x=80,y=410,anchor="w")
                    btn_LI = Button(self.F5,relief=RAISED,command=self.link11,height=23,image=self.icon2).place(x=20,y=410,anchor="w")
                    lbl = Label(self.F5,text="",font=("times now roman",25,"bold"),bg="light gray").place(x=250,y=410,anchor="w")
                    #print((i[16]))
                    import io
                    image_data = i[16]
                    image = Image.open(io.BytesIO(image_data))

                    # Resize the image to fit the desired frame size with anti-aliasing
                    desired_width = 205
                    desired_height = 160
                    image = image.resize((desired_width, desired_height), Image.LANCZOS)

                    self.imag_icon = ImageTk.PhotoImage(image)
                    self.F6 = Frame(self.F5,bd=5,relief=SUNKEN,bg="light gray")
                    self.F6.place(x=20,y=100,width=215,height=200 )
                    lb_pic = Label(self.F6, image=self.imag_icon)
                    lb_pic.place(x=0, y=0, height=desired_height, width=desired_width)    
                    txt2 = Label(self.F6,text="Student ID: ",width=20,anchor="w",font=("times new roman",13,"bold"),bg="gray")
                    txt2.place(x=0,y=165)
                    txt2_lbl = Entry(self.F6,width=12,state="readonly",textvariable=self.Std_Id,font=("times new roman",13,"bold"),bg="gray")
                    txt2_lbl.place(x=90,y=165)
            else:
                return messagebox.showerror("Error","Invalid Student ID")
        
        elif self.searchby.get() == "Contact":
            try:
                tmp=self.searchent.get()
                int(tmp)
                self.c.execute("SELECT * from Std WHERE contact="+str(self.searchent.get()))
                self.data=self.c.fetchall()
            #print(50*"&")
            #print(self.data)
                if self.data:
                        for i in self.data:
                            print(i)
                        a=(i[0])
                        self.Std_Id.set(a)
                        self.fname.set(i[1])
                        self.lname.set(i[2])
                        self.Roll_no.set(i[3])
                        self.code.set("+"+str(i[4]))
                        self.contact.set(i[5])
                        self.country.set(i[6])
                        self.class_.set(i[7])
                        self.address.set(i[8])
                        self.DOB.set(i[10])
                        self.email.set(i[11])
                        self.Gender.set(i[13])
                        self.L_Url.set(i[14])
                        self.F_Url.set(i[15])
                        self.link.set(i[16])
                        btn_Fb = Button(self.F5,relief=RAISED,command=self.link12,image=self.icon1).place(x=80,y=410,anchor="w")
                        btn_LI = Button(self.F5,relief=RAISED,command=self.link11,height=23,image=self.icon2).place(x=20,y=410,anchor="w")
                        lbl = Label(self.F5,text="",font=("times now roman",25,"bold"),bg="light gray").place(x=250,y=410,anchor="w")
                        #print((i[16]))
                        import io
                        image_data = i[16]
                        image = Image.open(io.BytesIO(image_data))

                        # Resize the image to fit the desired frame size with anti-aliasing
                        desired_width = 205
                        desired_height = 160
                        image = image.resize((desired_width, desired_height), Image.LANCZOS)

                        self.imag_icon = ImageTk.PhotoImage(image)
                        self.F6 = Frame(self.F5,bd=5,relief=SUNKEN,bg="light gray")
                        self.F6.place(x=20,y=100,width=215,height=200 )
                        lb_pic = Label(self.F6, image=self.imag_icon)
                        lb_pic.place(x=0, y=0, height=desired_height, width=desired_width)    
                        txt2 = Label(self.F6,text="Student ID: ",width=20,anchor="w",font=("times new roman",13,"bold"),bg="gray")
                        txt2.place(x=0,y=165)
                        txt2_lbl = Entry(self.F6,width=12,state="readonly",textvariable=self.Std_Id,font=("times new roman",13,"bold"),bg="gray")
                        txt2_lbl.place(x=90,y=165)
                else:
                    return messagebox.showerror("Error","Invalid Contact")
            except ValueError:
                return messagebox.showinfo('Error','Contact No. Should Be Integer')
            
        else:
            return messagebox.showerror("Error","Invalid Option")

    
    def link1(self):
        webbrowser.open_new("http://www.linkedin.com")

    def link2(self):
        webbrowser.open_new("http://www.facebook.com")

    def link11(self):
        if self.L_Url.get()=="#":
            return messagebox.showinfo("Info","Emloyee Have no LinkedIn Link")
        else:
            webbrowser.open_new("http://"+str(self.L_Url.get())) 

    def link12(self):
        if self.F_Url.get()=="#":
            return messagebox.showinfo("Info","Emloyee Have no Facebook Link")
        else:
            webbrowser.open_new("http://"+str(self.F_Url.get())) 


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
            y="UPDATE Last_Login set last_login_time=\""+str(self.Timex2)+"\", last_login_date=\""+str(self.today1)+"\" where email =\""+str(self.read1)+"\""
            print(y)
            self.c.execute(y)
            self.conn.commit()
            import login
        else:
            pass

    
    def home(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import Home


    def Emp_Manag(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import M_Emp

    def Std_Manag(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import M_Std

    def view_all(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import View_all

    def Stdview(self):
       cv2.destroyAllWindows()
       pass

    def change_pasw(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import C_pasw
    
    def Exit(self):
        cv2.destroyAllWindows()
        self.root.destroy()
            
    def dark(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply dark mode")
        if a>0:
            self.root.destroy()
            import darkMode.Std_View_Dark
        else:
            pass

    def light(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply mode")
        if a>0:
            self.root.destroy()
            import Std_view
        else:
            pass
#create Window    
root = Tk()
obj = win1(root)
root.mainloop()
