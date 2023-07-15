from tkinter import*
import cv2
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import webbrowser
import random
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
        
#-----------------------------------------------------------------------Image Initialization------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Image Initialization------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Image Initialization------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Image Initialization------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Image Initialization------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Image Initialization------------------------------------------------------------------------------------------


        #self.bg_icon = ImageTk.PhotoImage(file="img//1222596.jpg")
        #bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window
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

        #**********************************************Variables F!****************************************************************************
        self.fname=StringVar()
        self.lname=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.Role= StringVar()
        self.code=IntVar()
        self.pasw=StringVar()
        self.address=StringVar()
        self.furl=StringVar()
        self.furl.set("#")
        self.Iurl=StringVar()
        self.Iurl.set("#")
        self.Lurl=StringVar()
        self.Lurl.set("#")
        self.Yurl=StringVar()
        self.Yurl.set("#")
        self.turl=StringVar()
        self.turl.set("#")
        self.EmpID=StringVar()
        self.EmpID.set(str(random.randint(200000,1000000)))
        
        
        now = datetime.now()
        self.Time1=now.strftime('%H:%M:%S')

        self.today= now.strftime("%d-%b-%Y")

        self.label1, self.calendar1 = "", ""
        now = datetime.now()
        
        

        #**********************************************Variables F2****************************************************************************
        self.f1name=StringVar()
        self.l1name=StringVar()
        self.email_=StringVar()
        self.Role_=StringVar()
        self.Gender_=StringVar()
        self.address_=StringVar()
        self.searchval=StringVar()
        self.searchby=StringVar()
        self.f_url=StringVar()
        self.lurl=StringVar()
        self.yurl=StringVar()
        self.t_url=StringVar()
        self.iurl=StringVar()
        self.link=StringVar()

        #--------------------------------------------------Variable Initial Setting------------------------------------------------------------------
        self.searchby.set("Select Opt.")
        self.searchval.set("")
        self.gender.set("Choose Gender")
        self.Role.set("Choose Role")
        self.f1name.set("")
        self.l1name.set("")
        self.email_.set("")
        self.address_.set("")
        
        




#---------------------------------------------------------------------------------F1------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F1-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F1------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F1------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F1------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F1------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F1------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------



#*****************************************************************************************************************************************************************************



#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------

        self.FM1 = Frame(self.root,bg="black",bd=5,relief=RAISED)
        self.FM1.place(x=160,y=160,width=700,height=550 )

#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------




        FM11 =Frame(self.FM1,bd=5,relief=RAISED,bg="black")
        FM11.place(x=0,y=0,relwidth=1,height=60 )
        lbl_FM11= Label(FM11,text="Manage Employee",font=("times new roman",30,"bold"),fg="gold",bg="black")
        lbl_FM11.place(x=20,y=0)

        lblID_roll=Label(FM11,text="Emp ID",bg="black",fg="white",font=("times new roman",18,"bold"))
        lblID_roll.place(x=400,y=25,anchor="w")
        txtID_roll=Entry(FM11, textvariable=self.EmpID, width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txtID_roll.place(x=485,y=25,anchor="w")


#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------




        FM12 =Frame(self.FM1,bd=10,relief=SUNKEN,bg="black")
        FM12.place(x=0,y=440,relwidth=1,height=80 )

        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        
        
        but_Add=Button(self.FM1,text="ADD Data/ Upload Pic",bg="grey",command=self.add,bd=5,width=18,font=("times new roman",12,"bold")).place(x=500, y=390, anchor="w")
        btn_update2 = Button(FM12,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bd=6,text="Update",command=self.update1).grid(row=0,column=1,pady=6,padx=50,sticky="nesw")        
        btn_Delete = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Delete",command=self.delete).grid(row=0,column=2,pady=6,padx=50,sticky="nesw")
        btn_Clear = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Clear",command=self.clear).grid(row=0,column=3,pady=6,padx=50,sticky="nesw")        


        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------

        

        lbl_roll=Label(self.FM1,fg="white",text="First Name",font=("times new roman",18,"bold"),bg="black")
        lbl_roll.place(x=0,y=90,anchor="w")
        txt_roll=Entry(self.FM1, textvariable=self.fname, width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=90,anchor="w")

        #***************************************************************************************************

        lbl_roll=Label(self.FM1, fg="white",text="Last Name",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=140,anchor="w")
        txt_roll=Entry(self.FM1,textvariable=self.lname,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=140,anchor="w")
        
        #***************************************************************************************************


        lbl_roll=Label(self.FM1, fg="white",text="Email",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=190,anchor="w")
        txt_roll=Entry(self.FM1,textvariable=self.email,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=190,anchor="w")

        #***************************************************************************************************     

        lbl_roll=Label(self.FM1,fg="white", text="Contact",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0, y=240, anchor="w")
        self.code.set(0)
        combo_code = OptionMenu(self.FM1, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
        combo_code.place(x=118,y=240,anchor="w")
        #combo_code=ttk.Comboboxself.FM1, textvariable=self.code, font=("times new roman",16,"bold"),width=5,height = 15 ,state='readonly')
        #combo_code['values']=("+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61")
        #combo_code.place(x=185,y=330)
        txt_roll=Entry(self.FM1,width=14,textvariable=self.contact, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=175,y=240,anchor="w")

        #***************************************************************************************************
                
        lb_gender=Label(self.FM1, fg="white",text="Gender", font=("times new roman",18,"bold"),bg="black")
        lb_gender.place(x=0, y=290, anchor="w")
        combo_gender=ttk.Combobox(self.FM1,textvariable=self.gender,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Others")
        combo_gender.place(x=120, y=290, anchor="w")

        #***************************************************************************************************

        lbl_roll=Label(self.FM1,fg="white", text="Password",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=345,anchor="w")
        txt_roll=Entry(self.FM1,bg="white", width=17, textvariable=self.pasw,show="*", font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=345,anchor="w")

        #****************************************************************************************************

        lbl_roll=Label(self.FM1, fg="white",text="Address",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=400,anchor="w")
        txt_roll=Entry(self.FM1,textvariable=self.address, width=17,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=400,anchor="w")

        #***********************************************************************************************

        lbl_roll=Label(self.FM1,fg="white", text="LinkedIn URL",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=90,anchor="w")
        txt_roll=Entry(self.FM1, textvariable=self.Lurl,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=500,y=90,anchor="w")

        #***********************************************************************************************

        lbl_roll=Label(self.FM1,fg="white",text="Twitter URL",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=140,anchor="w")
        txt_roll=Entry(self.FM1, textvariable=self.turl,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=500,y=140,anchor="w")

        #***********************************************************************************************

        lbl_roll=Label(self.FM1, fg="white",text="Instagram URL",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=190,anchor="w")
        txt_roll=Entry(self.FM1, textvariable=self.Iurl,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=500,y=190,anchor="w")

        #***********************************************************************************************
 
        lbl_roll=Label(self.FM1,fg="white", text="Facebook URL",bg="black",font=("times new roman",18,"bold"))
        lbl_roll.place(x=320,y=240,anchor="w")
        txt_roll=Entry(self.FM1,textvariable=self.furl,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=500,y=240,anchor="w")

        #***********************************************************************************************

        lb_Role=Label(self.FM1,text="Role", font=("times new roman",18,"bold"),bg="black",fg="white")
        lb_Role.place(x=320, y=290, anchor="w")
        combo_Role=ttk.Combobox(self.FM1, textvariable=self.Role,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_Role['values']=("Ass. Porf.","Prof.","Jr. Prof","Lab. Ass.","Non Teaching","Principal","Dean Academics","Dean Administration")
        combo_Role.place(x=500, y=290, anchor="w")

        #***********************************************************************************************
        
        self.label1=(Label(self.FM1, text="D.O.B",bg="black",fg="white",font=("times new roman",18,"bold")))
        self.label1.place(x=320, y=340, anchor="w")

        self.calendar1=(DateEntry(self.FM1,textvariable=self.Yurl, font=("times new roman",13,"bold"),width=17, locale='en_GB',state="readonly"))
        self.calendar1.place(x=500, y=340, anchor="w")
        
        #***********************************************************************************************


        #lb_pic=Label(self.FM1,text="Upload Pic", font=("times new roman",18,"bold"),bg="#F5F5F5")
        #lb_pic.place(x=320, y=390, anchor="w")
        #lbl_but=Button(self.FM1,text="Upload Photo",bg="grey",command=self.upload,width=14,font=("times new roman",15,"bold"))
        #lbl_but.place(x=500, y=390, anchor="w")

        



#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM2-------------------------------------------------------------------------------------



        FM2 =Frame(self.root,bd=5,relief=GROOVE,bg="black")
        FM2.place(x=870,y=160,width=460,height=550 )
        lbl_FM2= Label(FM2,text=" Profile",font=("times new roman",20,"bold"),fg="white",bg="black")
        separator1 = ttk.Separator(FM2, orient='horizontal')
        separator1.place(x=10,width=430,y=40)
        lbl_FM2.place(x=0,y=0)

        lb_Search=Label(FM2,text="Search By: ", fg="white",font=("times new roman",15,"bold"),bg="black")
        lb_Search.place(x=10, y=60, anchor="w")
        
        combo_search=ttk.Combobox(FM2,font=("times new roman",13,"bold"),width=10,textvariable=self.searchby,state='readonly')
        combo_search['values']=("EmpID","Contact")
        combo_search.place(x=110, y=60, anchor="w")

        Ent_search = Entry(FM2,relief=GROOVE,width =12, textvariable=self.searchval,font=("times new roman",15,"bold")).place(x=230,y=60,anchor="w")

        btn_search = Button(FM2,relief=GROOVE,text="Search",command=self.search,font="bold",width =7, bg= "#F5F5F5").place(x=365,y=60,anchor="w")
        separator2 = ttk.Separator(FM2, orient='horizontal')
        separator2.place(x=10,width=430,y=80)
        
        self.FM21 =LabelFrame(FM2,bd=5,relief=GROOVE, text="Profile" ,fg="white",bg="black",font=20)
        self.FM21.place(x=0,y=100,relwidth=1,height=400 )
        
        self.imag_icon = ImageTk.PhotoImage(file="img//image_icon.png")
        self.FM22 =LabelFrame(self.FM21,bg=bg_color,bd=5,relief=SUNKEN)
        self.FM22.place(x=0,y=10,width=140,height=140 )
        lb_pic=Label(self.FM22,image=self.imag_icon)
        lb_pic.place(x=0, y=0,height=130,width=130)

        separator3 = ttk.Separator(FM2, orient='horizontal')
        separator3.place(x=10,width=430,y=290)

        
        Ent_fname = Entry(self.FM21,relief=FLAT,width =15,textvariable=self.f1name, font=("times new roman",15,"bold"), bg= "black",fg="white").place(x=260,y=20,anchor="w")
        lbl_fname = Label(self.FM21, font=("times new roman",15,"bold"),text= "First Name", bg= "black",fg="white").place(x=150,y=20,anchor="w")
        separator4 = ttk.Separator(self.FM21, orient='horizontal')
        separator4.place(x=260,width=150,y=35)

        Ent_lname = Entry(self.FM21,relief=FLAT,font=("times new roman",15,"bold"),textvariable=self.l1name,width =15,bg= "black",fg="white").place(x=260,y=60,anchor="w")
        lbl_lname = Label(self.FM21, font=("times new roman",15,"bold"),text= "Last Name",bg= "black",fg="white").place(x=150,y=60,anchor="w")
        separator5 = ttk.Separator(self.FM21, orient='horizontal')
        separator5.place(x=260,width=150,y=75)
        
        Ent_Email = Entry(self.FM21,relief=FLAT,width =15, textvariable=self.email_ ,font=("times new roman",15,"bold"), bg= "black",fg="white").place(x=260,y=100,anchor="w")
        lbl_Email = Label(self.FM21, font=("times new roman",15,"bold"),text= "Email Id",bg= "black",fg="white").place(x=150,y=100,anchor="w")
        separator6 = ttk.Separator(self.FM21, orient='horizontal')
        separator6.place(x=260,width=150,y=115)

        Ent_Role =  Entry(self.FM21,relief=FLAT,font=("times new roman",15,"bold"),textvariable=self.Role_ ,width =15,bg= "black",fg="white").place(x=260,y=140,anchor="w")
        lbl_Role = Label(self.FM21, font=("times new roman",15,"bold"),text= "Role",bg= "black",fg="white").place(x=150,y=140,anchor="w")
        separator7 = ttk.Separator(self.FM21, orient='horizontal')
        separator7.place(x=260,width=150,y=155)
        

        lbl_Gender = Label(self.FM21, font=("times new roman",15,"bold"),text= "Gender",bg= "black",fg="white").place(x=10,y=205,anchor="w")
        Ent_Gender1 =  Entry(self.FM21,relief=FLAT,font=("times new roman",15,"bold"),textvariable=self.Role_ ,width =15,bg= "black",fg="white")
        Ent_Gender1.place(x=100,y=200,anchor="w")        
        
        #Ent_Gender = Entry(self.FM21,relief=FLAT,width =15, font=("times new roman",15,"bold"), bg= "#F5F5F5").place(x=100,y=200,anchor="w")
        separator8 = ttk.Separator(self.FM21, orient='horizontal')
        separator8.place(x=102,width=155,y=215)
        #lbl_Gender = Label(self.FM21, font=("times new roman",15,"bold"),text= "Gender", bg= "#F5F5F5").place(x=10,y=205,anchor="w")
        

        Ent_Address = Entry(self.FM21,relief=FLAT,textvariable=self.address_,font=("times new roman",15,"bold"),width =15, bg= "black",fg="white").place(x=100,y=240,anchor="w")
        separator8 = ttk.Separator(self.FM21, orient='horizontal')
        separator8.place(x=100,width=150,y=255)
        lbl_Address = Label(self.FM21, font=("times new roman",15,"bold"),text= "Address",bg= "black",fg="white").place(x=10,y=245,anchor="w")


        lbl_Social = Label(self.FM21, font=("times new roman",20,"bold"),text= "Social Media Links", bg= "black",fg="white").place(x=10,y=300,anchor="w")

        btn_link1 = Button(self.FM21, image=self.icon2 ,relief=RAISED, font=("times new roman",14,"bold"),command=self.link1,bg= "black",foreground="#FEFCFF").place(x=10 ,y=343,anchor="w"  )
        btn_link2 = Button(self.FM21, image=self.icon3, relief=RAISED, font=("times new roman",14,"bold"),command=self.link2,bg= "black",foreground="#FEFCFF").place(x=60 ,y=342,anchor="w"  )
        btn_link3 = Button(self.FM21, image=self.icon1, relief=RAISED, font=("times new roman",14,"bold"),command=self.link3,bg= "black",foreground="#FEFCFF").place(x=110 ,y=343,anchor="w" )
        btn_link4 = Button(self.FM21, image=self.icon4, relief=RAISED, font=("times new roman",14,"bold"),command=self.link4,bg= "black",foreground="#FEFCFF").place(x=160 ,y=343,anchor="w" )
        btn_link5 = Button(self.FM21, image=self.icon5, relief=RAISED, font=("times new roman",14,"bold"),command=self.link5,bg= "black",foreground="#FEFCFF").place(x=210 ,y=340,anchor="w" )
        btn_showall = Button(FM2, text="Show All Data", relief=RAISED, font=("times new roman",14,"bold"),command=self.showall,bg="navy blue",foreground="black").place(x=300 ,y=510,anchor="w" )


    
        

#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
        
    def add(self):
        messagebox.showinfo("Info","Image mage be to Small to Load min(130x100)")  
        
        self.filename = filedialog.askopenfilename(initialdir = "/", title ="Upload Image", filetype=(("jpeg","*jpg"),("All Files","*.*"))) 
        self.lbl=Label(self.FM1,text="")
        
        
        if self.filename=="":
            return messagebox.showerror("Error!","Please Upload Photo ")

        if self.fname.get()=="" and self.pasw.get()=="" and self.email.get()=="" and self.gender.get()=="" and self.contact.get()=="" and self.code.get()==0 and self.address.get()=="" or self.Role.get()=="Choose Role" :
            return messagebox.showerror("Error!","All Feilds Required")
        
        if self.fname.get()=='':
            return messagebox.showinfo('Error','Enter a firstname')
        
        if self.address.get()=='':
            return messagebox.showinfo('Error','Enter a address')
            
        if self.pasw.get()=='':
            return messagebox.showinfo('Error','Enter a password')

        if len(str(self.pasw.get()))<8:
            return messagebox.showwarning("Warning","Password should be Minimum 8 charactrs")
        
        if self.contact.get()=='':
            return messagebox.showinfo('Error','Enter a contact')
        
        try:
            tmp=self.contact.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer')
        
        if len(self.contact.get()+str(self.code.get()))<10 and len(self.contact.get()+str(self.code.get()))>15:
            return messagebox.showinfo('Error','Enter a valid contact')      
        
        if self.email.get()=='':
            return messagebox.showinfo('Error','Enter an email')
        
            
        if self.gender.get()=='':
            return messagebox.showinfo('Error','Choose Gender')

        if self.code.get()=='':
            return messagebox.showinfo('Error','Choose Country Code')

        if "@" not in self.email.get():
            return messagebox.showwarning("Warrning","Email should have '@' Character")

        if self.Role.get()=="Choose Role":
            return messagebox.showwarning("Warrning","Choose Role Please!!!")

        if self.today<self.Yurl.get():
            return messagebox.showwarning("Error","D.O.B not Possible")

        else:
            self.con2 = str(region_code_for_country_code(self.code.get()))
    
            self.emp_code=self.fname.get()+str(random.randint(1000,40000))

            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS Emp(EmpID TEXT UNIQUE NOT NULL ,first_name TEXT NOT NULL, last_name TEXT , emp_code TEXT PRIMARY KEY UNIQUE NOT NULL, pasw TEXT NOT NULL,Role TEXT,email TEXT NOT NULL, gender TEXT NOT NULL, code TEXT NOT NULL, contact TEXT NOT NULL, country TEXT,address TEXT NOT NULL, Joining TEXT, Time1 TIME,L_URL TEXT,T_URL TEXT,I_URL TEXT,F_URL TEXT,Y_URL TEXT, PIC_LINK TEXT )")
            self.find_user = ("SELECT * FROM Emp WHERE email= ?  or contact = ?")
            self.c.execute(str(self.find_user),(self.email.get(),self.contact.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                #try:
                self.c.execute("INSERT INTO Emp (EmpID ,first_name,last_name,emp_code, pasw , Role, email, gender , code , contact , country , address,Joining , Time1, L_URL, T_URL, I_URL,F_URL,Y_URL, PIC_LINK ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (self.EmpID.get(),self.fname.get(),self.lname.get(),self.emp_code,self.pasw.get(),self.Role.get(),self.email.get(),self.gender.get(),self.code.get(),self.contact.get(),self.con2,self.address.get(),self.today,self.Time1,self.Lurl.get(),self.turl.get(),self.Iurl.get(),self.furl.get(),self.Yurl.get(),self.filename))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                messagebox.showinfo("Successfull","Successfully Added Data")
                self.clear()
                #except Exception:
                #    return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
                #    self.clear()        


    def update1(self):
        return messagebox.showinfo("Info","This Function Available only For Admin")

    def showall(self):
        if self.searchby.get()=="Select Opt." or self.searchval.get()=="":
            return messagebox.showerror("Error","All Entry Field Required")
        if self.searchby.get()=="Select Opt." :
            return messagebox.showerror("Error","Search Type Value Required")
        if self.searchval.get()=="":
            return messagebox.showerror("Error","All Search Field  Required")
        else:    
            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            if self.searchby.get() == "EmpID":
                self.c.execute("SELECT * from Emp WHERE EmpID="+str(self.searchval.get()))
                self.data=self.c.fetchall()
                #print(50*"&")
                #print(self.data)
                #self.EmpID.set(a)
                if self.data:
                        for i in self.data:
                            print(i)    
                        self.EmpID.set(i[0])               
                        self.fname.set(i[1])
                        self.lname.set(i[2])
                        self.pasw.set(i[4])
                        self.Role.set(i[5])
                        self.email.set(i[6])                        
                        self.gender.set(i[7])
                        self.code.set(i[8])
                        self.contact.set(i[9])
                        self.address.set(i[11])
                        self.Lurl.set(i[14])
                        self.turl.set(i[15])
                        self.Iurl.set(i[16])
                        self.furl.set(i[17])
                        self.Yurl.set(i[18])                        
                
                else:
                    return messagebox.showerror("Error","Invalid Employee ID")
            
            elif self.searchby.get() == "Contact":
                self.c.execute("SELECT * from Emp WHERE contact="+str(self.searchval.get()))
                self.data=self.c.fetchall()
                #print(50*"&")
                #print(self.data)
                #self.EmpID.set(a)
                if self.data:
                        for i in self.data:
                            print(i)    
                        self.EmpID.set(i[0])               
                        self.fname.set(i[1])
                        self.lname.set(i[2])
                        self.pasw.set(i[4])
                        self.Role.set(i[5])
                        self.email.set(i[6])                        
                        self.gender.set(i[7])
                        self.code.set(i[8])
                        self.contact.set(i[9])
                        self.address.set(i[11])
                        self.Lurl.set(i[14])
                        self.turl.set(i[15])
                        self.Iurl.set(i[16])
                        self.furl.set(i[17])
                        self.Yurl.set(i[18])                        
                else:
                    return messagebox.showerror("Error","Invalid Employee ID")        
            else:
                return messagebox.showerror("Error","Something Wrong Please Check!!!")
    def search(self):
        cv2.destroyAllWindows()
        if self.searchby.get()=="Select Opt." or self.searchval.get()=="":
            return messagebox.showerror("Error","All Entry Field Required")
        if self.searchby.get()=="Select Opt." :
            return messagebox.showerror("Error","Search Type Value Required")
        if self.searchval.get()=="":
            return messagebox.showerror("Error","All Search Field  Required")
        else:    
            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            if self.searchby.get() == "EmpID":
                self.c.execute("SELECT * from Emp WHERE EmpID="+str(self.searchval.get()))
                self.data=self.c.fetchall()
                #print(50*"&")
                #print(self.data)
                #self.EmpID.set(a)
                if self.data:
                        for i in self.data:
                            print(i)                   
                        self.f1name.set(i[1])
                        self.l1name.set(i[2])
                        self.Role_.set(i[5])
                        self.address_.set(i[11])
                        self.email_.set(i[6])
                        self.Gender_.set(i[7])
                        self.f_url.set(i[17])
                        self.lurl.set(i[14])
                        self.iurl.set(i[16])
                        self.yurl.set(i[18])
                        self.t_url.set(i[15])
                        self.link.set(i[19])
                        btn_link1 = Button(self.FM21, image=self.icon2, relief=RAISED, font=("times new roman",14,"bold"),command=self.link1,bg="#1569C7",foreground="#FEFCFF").place(x=60 ,y=342,anchor="w"  )
                        btn_link2 = Button(self.FM21, image=self.icon3, relief=RAISED, font=("times new roman",14,"bold"),command=self.link11,bg="#1569C7",foreground="#FEFCFF").place(x=60 ,y=342,anchor="w"  )
                        btn_link3 = Button(self.FM21, image=self.icon1, relief=RAISED, font=("times new roman",14,"bold"),command=self.link12,bg="#1569C7",foreground="#FEFCFF").place(x=110 ,y=343,anchor="w" )
                        btn_link4 = Button(self.FM21, image=self.icon4, relief=RAISED, font=("times new roman",14,"bold"),command=self.link13,bg="#1569C7",foreground="#FEFCFF").place(x=160 ,y=343,anchor="w" )
                        btn_link5 = Button(self.FM21, image=self.icon5, relief=RAISED, font=("times new roman",14,"bold"),command=self.link14,bg="#1569C7",foreground="#FEFCFF").place(x=210 ,y=343,anchor="w" )
                
                        winname=(str(i[1])+" "+str(i[2]))
                        c=i[19]
                        d=str(c)
                        a=list(d)
                        #print (a)
                        #a.pop()
                        f=''.join(a)
                        print("\n********************************\n")

                        img =cv2.imread(f)
                        try:
                            img1=cv2.resize(img,(130,100))
                            cv2.namedWindow(winname)        # Create a named window
                            cv2.moveWindow(winname, 885,330)  # Move it to (217,327)
                            cv2.imshow(winname, img1)
                            lbl = Label(self.FM21, text="Click anywhere on\n Screen to \nHide image", font=("times new roman",14,"bold"),bg="black",foreground="white").place(x=270 ,y=243,anchor="w" )

                            #cv2.waitKey()
                        except Exception:
                            return messagebox("Error","Image mage be to Small to Load")            
                
                else:
                    return messagebox.showerror("Error","Invalid Employee ID")
            
            elif self.searchby.get() == "Contact":
                self.c.execute("SELECT * from Emp WHERE contact="+str(self.searchval.get()))
                self.data=self.c.fetchall()
                #print(50*"&")
                #print(self.data)
                #self.EmpID.set(a)
                if self.data:
                        for i in self.data:
                            print(i)                   
                        self.f1name.set(i[1])
                        self.l1name.set(i[2])
                        self.Role_.set(i[5])
                        self.address_.set(i[11])
                        self.email_.set(i[6])
                        self.Gender_.set(i[7])
                        self.f_url.set(i[17])
                        self.lurl.set(i[14])
                        self.iurl.set(i[16])
                        self.yurl.set(i[18])
                        self.t_url.set(i[15])
                        self.link.set(i[19])
                        btn_link1 = Button(self.FM21, image=self.icon2, relief=RAISED, font=("times new roman",14,"bold"),command=self.link1,bg="#1569C7",foreground="#FEFCFF").place(x=60 ,y=342,anchor="w"  )
                        btn_link2 = Button(self.FM21, image=self.icon3, relief=RAISED, font=("times new roman",14,"bold"),command=self.link11,bg="#1569C7",foreground="#FEFCFF").place(x=60 ,y=342,anchor="w"  )
                        btn_link3 = Button(self.FM21, image=self.icon1, relief=RAISED, font=("times new roman",14,"bold"),command=self.link12,bg="#1569C7",foreground="#FEFCFF").place(x=110 ,y=343,anchor="w" )
                        btn_link4 = Button(self.FM21, image=self.icon4, relief=RAISED, font=("times new roman",14,"bold"),command=self.link13,bg="#1569C7",foreground="#FEFCFF").place(x=160 ,y=343,anchor="w" )
                        btn_link5 = Button(self.FM21, image=self.icon5, relief=RAISED, font=("times new roman",14,"bold"),command=self.link14,bg="#1569C7",foreground="#FEFCFF").place(x=210 ,y=343,anchor="w" )
                
                        winname=(str(i[1])+" "+str(i[2]))
                        c=i[19]
                        d=str(c)
                        a=list(d)
                        #print (a)
                        #a.pop()
                        f=''.join(a)
                        print("\n********************************\n")

                        img =cv2.imread(f)
                        try:
                            img1=cv2.resize(img,(130,100))
                            cv2.namedWindow(winname)        # Create a named window
                            cv2.moveWindow(winname, 885,330)  # Move it to (217,327)
                            cv2.imshow(winname, img1)
                            lbl = Label(self.FM21, text="Click anywhere on\n Screen to \nHide image", font=("times new roman",14,"bold"),bg="black",foreground="white").place(x=270 ,y=243,anchor="w" )

                            #cv2.waitKey()
                        except Exception:
                            return messagebox("Error","Image mage be to Small to Load or not Exist")
                        
                else:
                    return messagebox.showerror("Error","Invalid Contact No.")
            
            else:
                return messagebox.showerror("Error","Invalid Option")


    def delete(self):
        return messagebox.showinfo("Info","This Function Available only For Admin")
 
    def clear(self):
        self.fname.set("")
        self.lname.set("")
        self.pasw.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.Role.set("")
        self.code.set(0)
        self.address.set("")
        self.furl.set("#")
        self.Iurl.set("#")
        self.Lurl.set("#")
        self.Yurl.set("#")
        self.turl.set("#")
        self.searchby.set("Select Opt.")
        self.searchval.set("")
        self.gender.set("Choose Gender")
        self.Role.set("Choose Role")
        self.f1name.set("")
        self.l1name.set("")
        self.email_.set("")
        self.address_.set("")
        self.Role_.set("")
        cv2.destroyAllWindows()
        self.EmpID.set(str(random.randint(200000,1000000)))
        btn_link1 = Button(self.FM21, image=self.icon2 ,relief=RAISED, font=("times new roman",14,"bold"),command=self.link1,bg="#1569C7",foreground="#FEFCFF").place(x=10 ,y=343,anchor="w"  )
        btn_link2 = Button(self.FM21, image=self.icon3, relief=RAISED, font=("times new roman",14,"bold"),command=self.link2,bg="#1569C7",foreground="#FEFCFF").place(x=60 ,y=342,anchor="w"  )
        btn_link3 = Button(self.FM21, image=self.icon1, relief=RAISED, font=("times new roman",14,"bold"),command=self.link3,bg="#1569C7",foreground="#FEFCFF").place(x=110 ,y=343,anchor="w" )
        btn_link4 = Button(self.FM21, image=self.icon4, relief=RAISED, font=("times new roman",14,"bold"),command=self.link4,bg="#1569C7",foreground="#FEFCFF").place(x=160 ,y=343,anchor="w" )
        btn_link5 = Button(self.FM21, image=self.icon5, relief=RAISED, font=("times new roman",14,"bold"),command=self.link5,bg="#1569C7",foreground="#FEFCFF").place(x=210 ,y=343,anchor="w" )
        #btn_link6 = Button(self.FM21, image=self.icon6, relief=RAISED, font=("times new roman",14,"bold"),command=self.link6,bg="#1569C7",foreground="#FEFCFF").place(x=260 ,y=340,anchor="w" )


    def upload(self):
        if self.fname.get()=="" and self.pasw.get()=="" and self.email.get()=="" and self.gender.get()=="" and self.contact.get()==""  :
            return messagebox.showerror("Error!","Frist Name,Password,Email,Contact Required see the missing feilds")
       
        if self.fname.get()=="" :
            return messagebox.showerror("Error!","Frist Name Required ")
        
        if  self.email.get()==""  :
            return messagebox.showerror("Error!","Email Required") 
        if "@" not in self.email.get():
            return messagebox.showwarning("Warrning","Email should have '@' Character")
       
        if self.contact.get()=="":
            return messagebox.showerror("Error!","Contact Required")

        if  self.pasw.get()=="" :
            return messagebox.showerror("Error!","Password Required")
        
        else:
            self.filename = filedialog.askopenfilename(initialdir = "/", title ="Upload Image", filetype=(("jpeg","*jpg"),("All Files","*.*")))
            self.lbl=Label(self.FM1,text="")
            self.lbl.place(x=0,y=415)
            self.lbl.configure(text="Uploaded: " + self.filename)
    
    def link1(self):
        webbrowser.open_new("http://www.google.com")

    def link2(self):
        webbrowser.open_new("https://www.instagram.com/?hl=en")
    
    def link3(self):
        webbrowser.open_new("http://www.facebook.com")

    def link4(self):
        webbrowser.open_new("http://www.twitter.com")

    def link5(self):
        webbrowser.open_new("http://www.linkedin.com")

    def link11(self):
        if self.iurl.get()=="#":
            return messagebox.showinfo("Info","Emloyee Have no Instagram Link")
        else:
            webbrowser.open_new("http://"+str(self.iurl.get()))

    def link12(self):
        if self.f_url.get()=="#":
            return messagebox.showinfo("Info","Emloyee Have no Facebook Link")
        else:
            webbrowser.open_new("http://"+str(self.f_url.get()))
    
    def link13(self):
        if self.t_url.get()=="#":
            return messagebox.showinfo("Info","Emloyee Have no Twitter Link")
        else:
            webbrowser.open_new("http://"+str(self.t_url.get()))

    def link14(self):
        if self.yurl.get()=="#":
            return messagebox.showinfo("Info","Emloyee Have no Youtube Link")
        else:
            webbrowser.open_new("http://"+str(self.yurl.get()))

    def link15(self):
        if self.lurl.get()=="#":
            return messagebox.showinfo("Info","Emloyee Have no linkedIn Link")
        else:
            webbrowser.open_new("http://"+str(self.lurl.get()))




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
        cv2.destroyAllWindows()
        self.root.destroy()
        import Home_Emp_Dark

    def Emp_Manag(self):
        cv2.destroyAllWindows()
        pass

    def Std_Manag(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import M_std_emp_dark

    def view_all(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import View_all_emp_dark

    def Stdview(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import Std_view_emp_dark

    def change_pasw(self):
        cv2.destroyAllWindows()
        self.root.destroy()
        import C_pasw_emp_dark
    
    def dark(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply dark mode")
        if a>0:
            cv2.destroyAllWindows()
            self.root.destroy()
            import M_Emp_emp_dark
        else:
            pass

    def light(self):
        a= messagebox.askyesnocancel("Ques","Do you want to apply light mode")
        if a>0:
            cv2.destroyAllWindows()
            self.root.destroy()
            import os
            sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
            import M_Emp_emp
        else:
            pass
    def Exit(self):
        cv2.destroyAllWindows()
        self.root.destroy()
            
#create Window    
root = Tk()
obj = win1(root)
root.mainloop()
