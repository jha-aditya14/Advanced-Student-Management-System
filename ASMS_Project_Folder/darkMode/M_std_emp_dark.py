from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import random
import os, pickle
#import sqlite3
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
from tkinter import filedialog
#--------


class win1:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System".center(420))  # title for Window 
        self.root.configure(background = "black")  # background color for window 
        self.root.geometry("1360x768+0+0")

        bg_color ="black"
        
#----------------------------------------------Images---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Images---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Images---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Images---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Images---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Images---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------Images---------------------------------------------------------------------------------------------------------------------


        self.clock_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Clock_Dark.png")
        self.student_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//images (1).jpg")


        self.icon1=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download.jpg")
        self.icon2=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download (1).png")
        self.icon3=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download.png")
        self.icon4=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//images.jpg")
        self.icon5=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//linked_in.png")

        
        self.home_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Home_dark.png")
        self.mangEmp_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Manage_Emp_dark.png")
        self.mangStd_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Manage_Student_dark.png")
        self.ViewStd_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//View_Std_dark.png")
        self.viewall_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//View_All_dark.png")
        
        self.change_pasw_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Reset_dark.png")
        self.exit_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//Exit_dark.png")


        #**********************************************Variables F!****************************************************************************
        self.fname=StringVar()
        self.fname.set("")
        self.lname=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.gender.set("Gender")
        self.contact=StringVar()
        self.class_= StringVar()
        self.class_.set("Choose Class")
        self.dept=StringVar()
        self.sem=StringVar()
        self.code=IntVar()
        self.Roll_no=StringVar()
        self.address=StringVar()
        self.furl=StringVar()
        self.furl.set("#")
        self.Lurl=StringVar()
        self.Lurl.set("#")
        self.DOB=StringVar()
        self.searchby=StringVar()
        self.searchby.set("Choose Option")
        self.searchval=StringVar()
        self.dept.set("Choose Department")
        self.sem.set("Choose Semester")
        self.url=StringVar()
        self.filename=StringVar()
        self.url=self.filename.get()
        self.dele=StringVar()
        self.dele.set("Available for Admin")
        self.Std_ID=StringVar()
        r=random.randint(200000,1000000)
        self.Std_ID.set(str(r))
        
        self.con2=""
        
        now = datetime.now()
        self.Time1=now.strftime('%H:%M:%S')

        self.today= now.strftime("%d/%m/%Y")

        self.label, self.calendar = "",""


#----------------------------------------------F1---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------F1---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------F1---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------F1---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------F1---------------------------------------------------------------------------------------------------------------------
        

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


        F3 = Frame(self.root,bd=5,relief=FLAT,bg="black")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / Employee",fg="white",font=("comic sans",15,"italic"),bg="black")
        lbl_1.place(x=0,y=0)

#-----------------------------------------------------------------------Main Screen------------------------------------------------------------------------------
#-----------------------------------------------------------------------Main Screen------------------------------------------------------------------------------
#-----------------------------------------------------------------------Main Screen------------------------------------------------------------------------------
#-----------------------------------------------------------------------Main Screen------------------------------------------------------------------------------
#-----------------------------------------------------------------------Main Screen------------------------------------------------------------------------------
#-----------------------------------------------------------------------Main Screen------------------------------------------------------------------------------
#-----------------------------------------------------------------------Main Screen------------------------------------------------------------------------------


        self.F4 = Frame(self.root,bd=5,relief=FLAT,bg="black")
        self.F4.place(x=151,y=132,relwidth=1,height=600)
        lbl_1= Label(self.F4,text="Manage Students",fg="#008080",bg="black",font=("geometric sans-serif",30,"bold"))
        lbl_1.place(x=0,y=0)
    
        seprator1_style = ttk.Style()
        separator1 = ttk.Separator(self.F4, orient='horizontal',style="Line.TSeparator")
        separator1.place(x=0,width=700,y=50)
        seprator1_style.configure("Line.TSeparator")
        
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------

        

        lbl_roll=Label(self.F4,text="Student ID",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=90,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.Std_ID,state="readonly", width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=90,anchor="w")

        #**************************************************************************************************

        lbl_roll=Label(self.F4,text="First Name",font=("times new roman",18,"bold"),bg="black",fg="white")
        lbl_roll.place(x=0,y=140,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.fname, width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=140,anchor="w")

        #***************************************************************************************************

        lbl_roll=Label(self.F4,text="Last Name",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=190,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.lname,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=190,anchor="w")
        
        #***************************************************************************************************


        lbl_roll=Label(self.F4,text="Roll No",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=240,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.Roll_no,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=240,anchor="w")

        #***************************************************************************************************     

        lbl_roll=Label(self.F4,text="Contact",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0, y=290, anchor="w")
        self.code.set("Code")
        combo_code = OptionMenu(self.F4, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
        combo_code.place(x=118,y=290,anchor="w")
        #combo_code=ttk.Comboboxself.F4, textvariable=self.code, font=("times new roman",16,"bold"),width=5,height = 15 ,state='readonly')
        #combo_code['values']=("+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61")
        #combo_code.place(x=185,y=330)
        txt_roll=Entry(self.F4, width=14,textvariable=self.contact, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=175,y=290,anchor="w")

        #***************************************************************************************************
        lbl_roll=Label(self.F4,text="Class",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.place(x=0, y=340, anchor="w")
        self.code.set(0)
        combo_class = OptionMenu(self.F4, self.class_,"CSE-A_1st","CSE-A_2nd","CSE-A_3rd","CSE-A_4th","CSE-B_1st","CSE-B_2nd","CSE-B_3rd","CSE-B_4th","IT_1st","IT_2nd","IT_3rd","IT_4th","ECE-A_1st","ECE-A_2nd","ECE-A_3rd","ECE-A_4th","ECE-B_1st","ECE-B_2nd","ECE-B_3rd","ECE-B_4th","EEE_1st","EEE_2nd","EEE_3rd","EEE_4th")
        combo_class.place(x=118,y=340,anchor="w")
        combo_class.configure(width=23,relief=RAISED,bg="grey")
        
        #lb_gender=Label(self.F4,text="Class", font=("times new roman",18,"bold"),bg="#F5F5F5")
        #lb_gender.place(x=0, y=290, anchor="w")
        #combo_gender=ttk.Combobox(self.F4, textvariable=self.class_,width=17, font=("times new roman",13,"bold"),state='readonly')
        #combo_gender['values']=("CSE-A_1st","CSE-A_1st","CSE-A_1st","CSE-A_1st","CSE-A_1st","CSE-A_1st","CSE-A_1st","CSE-A_1st")
        #combo_gender.place(x=120, y=290, anchor="w")

        #***************************************************************************************************

        lbl_roll=Label(self.F4,text="Address",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=395,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.address, width=17,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=395,anchor="w")

        #***********************************************************************************************

        lb_dep=Label(self.F4,text="Department", bg="black",fg="white",font=("times new roman",16,"bold"))
        lb_dep.place(x=0, y=445, anchor="w")
        combo_dep=ttk.Combobox(self.F4, textvariable=self.dept,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_dep['values']=("Computer Science and Engineering","Information Technology","Electronics and Communication Engineering","Electrical and Electronics Engineering")
        combo_dep.place(x=120, y=445, anchor="w")

        #*******************************************************************************************************
        
        self.font=("times new roman",18,"bold")
        labels = ('DOB')
        self.label=(Label(self.F4, text="D.O.B",bg="black",fg="white", font=self.font))
        self.label.place(x=320, y=90, anchor="w")

        self.calendar=(DateEntry(self.F4, textvariable=self.DOB,font=("times new roman",15,"bold"), locale='en_GB', width=15,state="readonly"))
        self.calendar.place(x=505, y=85, anchor="w")
        #print (self.calendar)

        #***********************************************************************************************

        lbl_roll=Label(self.F4,text="Email",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=140,anchor="w")
        txt_roll=Entry(self.F4,width=17, textvariable=self.email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=500,y=140,anchor="w")

        #***********************************************************************************************
        lb_dep=Label(self.F4,text="Semester",bg="black",fg="white", font=("times new roman",18,"bold"))
        lb_dep.place(x=320, y=190, anchor="w")
        combo_dep=ttk.Combobox(self.F4, textvariable=self.sem,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_dep['values']=("1st Sem","2nd Sem","3rd Sem","4th Sem","5th Sem","6th Sem","7th Sem","8th Sem")
        combo_dep.place(x=500, y=190, anchor="w")

        #***********************************************************************************************
        lb_dep=Label(self.F4,text="Gender", font=("times new roman",18,"bold"),bg="black",fg="white")
        lb_dep.place(x=320, y=240, anchor="w")
        combo_dep=ttk.Combobox(self.F4, textvariable=self.gender,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_dep['values']=("Male","Female","Others")
        combo_dep.place(x=500, y=240, anchor="w")

        #*****************************************************************************************************
        
        #self.con2.set("Generate By Code")
        lbl_roll=Label(self.F4,text="Social Links",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=290,anchor="w")
        #txt_roll=Entry(self.F4,width=17, textvariable=self.con2, state="readonly",font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        #txt_roll.place(x=500,y=290,anchor="w")



        lbl_roll=Label(self.F4,text="Facebook URL",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=340,anchor="w")
        txt_roll=Entry(self.F4,width=17, textvariable=self.furl,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=500,y=340,anchor="w")

        #***********************************************************************************************

        lbl_roll=Label(self.F4,text="LinkedIn URL",bg="black",fg="white",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=390,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.Lurl,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=500,y=390,anchor="w")


        #***********************************************************************************************

        #lb_pic=Label(self.F4,text="Upload Pic", font=("times new roman",18,"bold"),bg="#F5F5F5")
        #lb_pic.place(x=320, y=440, anchor="w")
        #lbl_but=Button(self.F4,text="Upload Photo",fg="white",bg="red",command=self.upload,width=14,font=("times new roman",15,"bold"))
        #lbl_but.place(x=500, y=440, anchor="w")

#----------------------------------------------Buttons---------------------------------------------------------------------------------
#----------------------------------------------Buttons---------------------------------------------------------------------------------
#----------------------------------------------Buttons---------------------------------------------------------------------------------
#----------------------------------------------Buttons---------------------------------------------------------------------------------
#----------------------------------------------Buttons---------------------------------------------------------------------------------
#----------------------------------------------Buttons---------------------------------------------------------------------------------

        F5 =Frame(self.F4,bd=10,relief=SUNKEN,bg="black")
        F5.place(x=0,y=480,width=700,height=80 )

        btn_Add = Button(self.F4,relief=GROOVE,width=15, font=("times new roman",13,"bold"),bg="red",fg="white",bd=6, text="ADD/UPLOAD PIC",command=self.add).place(x=510, y=440, anchor="w")
        btn_update2 = Button(F5,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bg="navy blue",fg="white",bd=6,text="Update",command=self.update).grid(row=0,column=0,pady=6,padx=50,sticky="nesw")        
        btn_Delete = Button(F5,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bg="navy blue",fg="white",bd=6,text="Delete",command=self.delete).grid(row=0,column=1,pady=6,padx=50,sticky="nesw")
        self.txt_roll12=Entry(F5, textvariable=self.dele,state="readonly",width=22, font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        self.txt_roll12.grid(row=0,column=2,pady=6,padx=5,sticky="nesw")
        btn_Clear = Button(self.F4,relief=GROOVE, width=15,font=("times new roman",13,"bold"),bg="navy blue",fg="white",bd=6,text="Clear ALL",command=self.clear).place(x=320,y=440,anchor="w")       

        seprator2_style = ttk.Style()
        separator2 = ttk.Separator(self.F4, orient='vertical',style="Line.TSeparator")
        separator2.place(x=700,height=590,y=0)
        seprator2_style.configure("Line.TSeparator")

#----------------------------------------------------self.F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------self.F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------self.F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------self.F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------self.F4 Partion2-----------------------------------------------------------------------------

        seprator2_style = ttk.Style()
        separator2 = ttk.Separator(self.F4, orient='horizontal',style="Line.TSeparator")
        separator2.place(x=700,width=675,y=80)
        seprator2_style.configure("Line.TSeparator")

        lb_search=Label(self.F4,text="Search By", font=("times new roman",15,"bold"),bg="black",fg="white")
        lb_search.place(x=720 ,y=17, anchor="w")
        combo_search=ttk.Combobox(self.F4, textvariable=self.searchby,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll","Std_Id")
        combo_search.place(x=830, y=17, anchor="w")

        lb_search2=Entry(self.F4,textvariable=self.searchval,width=15,relief=SUNKEN,bd=5,font=("times new roman",15,"bold"),bg="#F5F5F5")
        lb_search2.place(x=1030, y=15, anchor="w")
        

        btn_searchall = Button(self.F4,relief=RAISED,width=30, command=self.search,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6, text="Search All")
        btn_searchall.place(x=720,y=60,anchor="w")
        btn_search = Button(self.F4,relief=RAISED,width=30,command=self.search_data ,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6,text="Search")        
        btn_search.place(x=970,y=60,anchor="w")

#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------            
#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------        
        F6 =Frame(self.F4,bd=10,relief=SUNKEN,bg="white")
        F6.place(x=720,y=85,width=475,height=500 )

        Table_Frame=Frame(F6,bd=4, relief=RIDGE,bg=bg_color)
        Table_Frame.place(x=0,y=0,width=455,height=480)

        style=ttk.Style(Table_Frame)
        #style.theme_use("calm")
        style.configure("Treeview",background="black",fieldbackground="black",foreground="white")


        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Std_ID" ,"First_name"  , "Last_name"  , "Roll", "code"  , "contact"  , "country" , "Class"  , "address"  , "Department"  , "DOB" , "Email"  , "Semester"  , "Gender"  , "L_URL" ,"F_URL","PIC_LINK"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

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

        self.Student_table.column("Std_ID", width=150)
        self.Student_table.column("First_name", width=150)
        self.Student_table.column("Last_name", width=150)
        self.Student_table.column("Roll", width=140)
        self.Student_table.column("code", width=70)
        self.Student_table.column("contact", width=120)
        self.Student_table.column("country", width=50)
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
        self.Student_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

        


#----------------------------------------------------------------FUNCTIONS--------------------------------------------------------
#----------------------------------------------------------------FUNCTIONS--------------------------------------------------------
#----------------------------------------------------------------FUNCTIONS--------------------------------------------------------
#----------------------------------------------------------------FUNCTIONS--------------------------------------------------------
#----------------------------------------------------------------FUNCTIONS--------------------------------------------------------
#----------------------------------------------------------------FUNCTIONS--------------------------------------------------------
    
    #messagebox.showinfo("Info","Add Data First then Upload Pic")
    def add(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title ="Upload Image", filetype=(("jpeg","*jpg"),("All Files","*.*"))) 
        self.lbl=Label(self.F4,text="")

        if self.filename=="":
            return messagebox.showerror("Error!","Please Upload Photo ")
        
        if self.fname.get()=="" and self.Roll_no.get()=="" and self.contact.get()=="" and self.class_.get()=="Choose Class" and self.code.get()== "Code" and self.filename=="" and self.address.get()=="" and self.dept.get=="Choose Department" and self.sem.get=="Choose Semester" :
            return messagebox.showerror("Error!","All Feilds Required")
        
        if self.fname.get()=='':
            return messagebox.showinfo('Error','Enter a firstname')
        
        if self.Roll_no.get()=='':
            return messagebox.showinfo('Error','Enter a Roll_no.') 
        
        a=len(str(self.Roll_no.get()))
        if  a<9 and a>11 :
            return messagebox.showerror("Error!","Invalid Roll No it must consist of 11 digits")    

        if self.code.get=="Code":
            return messagebox.showinfo("Error","Choose Code")
        
        
        if self.contact.get()=='Choose Class':
            return messagebox.showinfo('Error','Enter a contact')
        
        try:
            tmp=self.contact.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer')
        
        if len(self.contact.get()+str(self.code.get()))<10 and len(self.contact.get()+str(self.code.get()))>15:
            return messagebox.showinfo('Error','Enter a valid contact')      
        
        if self.class_.get()=='':
            return messagebox.showinfo('Error','Enter Class')
        
        
        if self.address.get()=='':
            return messagebox.showinfo('Error','Enter an Address')
        
            
        if self.dept.get()=='Choose Department':
            return messagebox.showinfo('Error','Enter Department')

        if self.sem.get()=='Choose Semester':
            return messagebox.showinfo('Error','Semester in which stusent studies')

        if self.DOB.get()>self.today:
            return messagebox.showwarning("Error","D.O.B not Possible")

        if "@" not in self.email.get():
            return messagebox.showwarning("Warrning","Email should have '@' Character")
        

        else:
            self.con2 = str(region_code_for_country_code(self.code.get()))

            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS Std(Std_ID TEXT UNIQUE NOT NULL ,First_name TEXT NOT NULL, Last_name TEXT , Roll TEXT PRIMARY KEY UNIQUE NOT NULL, code TEXT NOT NULL, contact TEXT NOT NULL, country TEXT, Class TEXT NOT NULL, address TEXT NOT NULL, Department TEXT NOT NULL, DOB TEXT, Email TEXT , Semester TEXT NOT NULL, Gender TEXT , L_URL TEXT,F_URL TEXT, PIC_LINK TEXT)")
            self.find_user = ("SELECT * FROM Std WHERE  Email= ?  or contact = ? or Roll = ? ")
            self.c.execute(str(self.find_user),(self.email.get(),self.contact.get(),self.Roll_no.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Roll No. or Contact or Email is already Used")
            else:
                try:
                    self.c.execute("INSERT INTO Std (Std_ID ,First_name  , Last_name  , Roll, code  , contact  , country , Class  , address  , Department  , DOB , Email  , Semester  , Gender  , L_URL ,F_URL , PIC_LINK  ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.Std_ID.get(),self.fname.get(),self.lname.get(),self.Roll_no.get(),self.code.get(),self.contact.get(),self.con2,self.class_.get(),self.address.get(),self.dept.get(),self.DOB.get(),self.email.get(),self.sem.get(),self.gender.get(), self.Lurl.get(),self.furl.get(),self.filename))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    messagebox.showinfo("Successfull","Successfully Added Data")
                    self.clear()
                except Exception:
                    messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
                    #messagebox.showinfo("Error!!", "May be your Roll No. already exist. Please Check")        


    def search(self):
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def search_data(self):
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.getcursor)
        self.search_data1()

    def search_data1(self):
        if self.searchby.get()=="" and self.searchval.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchval.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            if self.searchby.get() == "Roll":
                self.conn=sqlite3.connect("sdms.db")
                self.c=self.conn.cursor()
                self.c.execute("select * from Std where Roll="+self.searchval.get())
                rows=self.c.fetchall()
                if len(rows)!=0:
                        self.Student_table.delete(*self.Student_table.get_children())
                        for row in rows:
                                self.Student_table.insert('',END,values=row)
                        self.conn.commit()
                        self.conn.close()

                else:
                    return messagebox.showerror("Error","Roll No. Not Exist")        
                #self.conn.close()
            if self.searchby.get() == "Std_Id":
                self.conn=sqlite3.connect("sdms.db")
                self.c=self.conn.cursor()
                self.c.execute("select * from Std where Std_ID ="+self.searchval.get())
                rows=self.c.fetchall()
                if len(rows)!=0:
                        self.Student_table.delete(*self.Student_table.get_children())
                        for row in rows:
                                self.Student_table.insert('',END,values=row)
                        self.conn.commit()
                        self.conn.close()
                else:
                    return messagebox.showerror("Error","Student Id Not Exist")  
                    self.clear()  

            
            

    def update(self):
        return messagebox.showinfo("Info","This Function Available only For Admin")
    
    def delete(self):
        return messagebox.showinfo("Info","This Function Available only For Admin")
            
    def clear(self):
        r=random.randint(200000,1000000)
        self.Std_ID.set(str(r))
        self.fname.set("")
        self.lname.set("") 
        self.email.set("")
        self.gender.set("Gender")
        self.contact.set("")
        self.class_.set("Choose Class")
        self.dept.set("Choose Department")
        self.sem.set("Choose Semester")
        self.code.set(0)
        self.Roll_no.set("")
        self.address.set("")
        self.furl.set("#")
        self.Lurl.set("#")
        self.DOB.set(self.today)
        self.searchby.set("Search Option")
        self.searchval.set("")
        self.Student_table.delete(*self.Student_table.get_children())
        self.dele.set("Available for Admin")
        
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

    def Emp_Manag(self):
        self.root.destroy()
        import M_Emp_emp_dark

    def home(self):
        self.root.destroy()
        import Home_Emp_Dark

    def Std_Manag(self):
        pass

    def view_all(self):
        self.root.destroy()
        import View_all_emp_dark

    def Stdview(self):
        self.root.destroy()
        import Std_view_emp_dark

    def change_pasw(self):
        self.root.destroy()
        import C_pasw_emp_dark
    
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
        a = row[0]
        self.Std_ID.set(a)
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

    def dark(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply dark mode")
        if a>0:
            self.root.destroy()
            import M_std_emp_dark
        else:
            pass

    def light(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply light mode")
        if a>0:
            self.root.destroy()
            import os
            sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
            import M_Std_emp
        else:
            pass

            
 
#create Window    
root = Tk()
obj = win1(root)
root.mainloop()


