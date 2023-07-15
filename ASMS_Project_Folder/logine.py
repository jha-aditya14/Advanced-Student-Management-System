from tkinter import*    #For GUI
from tkinter import ttk  
from tkinter import messagebox
from PIL import ImageTk  # for Image related work 
import os   #for file 
import webbrowser
import sys,sqlite3
from datetime import datetime

#--------

class win1:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Form".center(420))  # title for Window 
        self.root.configure(background = "black")  # background color for window 
        self.root.geometry("1360x768+0+0")

        bg_color ="#2B547E"
        
        #-----------Storing -------image to variables-------------------
        self.bg_icon = ImageTk.PhotoImage(file="ASMS_Project_Folder//img//beautiful-landscape-nature-scenery-1d-1360x768.jpg")
        self.F2 = ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download1.jpeg") # here we store image to a variable using PIL module help 
        self.icon1=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download.jpg")
        self.icon2=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download (1).png")
        self.icon3=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//download.png")
        self.icon4=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//images.jpg")
        self.user_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//images.png")
        self.pasw_icon=ImageTk.PhotoImage(file="ASMS_Project_Folder//img//images (1).png")


        self.email=StringVar()
        self.pasw=StringVar()
        self.email.set("Email Id(eg:a@ab.com)")
        
        
        
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window

        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=195,y=95,width=600,height=480 )
        lbl = Label(F1,text="LOGIN As Employee ", bg=bg_color, fg="gold", font= ("times new roman",30,"bold")).grid(row=0, column=0,padx=50,pady=30)
        
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE, bg="")
        F2.place(x=790,y=95,width=310,height=480 )
        lbl2 = Label(F2,bg=bg_color, image = self.F2).grid(row=0, column=0,padx=100,pady=20)
        lbl3 = Label(F2, text = "Also Sign Up fot the new Users",bg="white",fg="green", font= ("times new roman",10,"italic")).grid(row=1, column=0,padx=10)
        lbl4 = Label(F2, text = "CodewithAJ@",fg="green",bg="white", font= ("times new roman",10,"italic")).grid(row=2, column=0,padx=10)

        lbl5 = Label(F2, text = "Follow Us On",fg="red",bg="white", font= ("times new roman",15)).place(x=150,y=350,anchor="c")

        lbl6 = Label(F2, text = "Developed by Aditya Jha ",fg="#4863A0",bg="white", font= ("times new roman",12)).place(x=0,y=440)


        btn_login = Button(F2, text="Login",relief=FLAT,width =20,height=1,command=self.login2, font=("times new roman",14,"bold"),bg="#348017",foreground="#FEFCFF").grid(row = 3,column=0,padx=10,pady=25 )
        btn_SignUp = Button(F2, text="SignUp",width =20,height=1,command=self.signup,relief=RAISED, font=("times new roman",14,"bold"),bg="#1569C7",foreground="#FEFCFF").grid(row = 4,column=0 )
        
        btn_link1 = Button(F2, image=self.icon2 ,relief=RAISED, font=("times new roman",14,"bold"),command=self.link1,bg="#1569C7",foreground="#FEFCFF").place(x=20 ,y=400,anchor="w" )
        btn_link2 = Button(F2, image=self.icon3, relief=RAISED, font=("times new roman",14,"bold"),command=self.link2,bg="#1569C7",foreground="#FEFCFF").place(x=90 ,y=400,anchor="w"  )
        btn_link3 = Button(F2, image=self.icon1, relief=RAISED, font=("times new roman",14,"bold"),command=self.link3,bg="#1569C7",foreground="#FEFCFF").place(x=160 ,y=400,anchor="w" )
        btn_link4 = Button(F2, image=self.icon4, relief=RAISED, font=("times new roman",14,"bold"),command=self.link4,bg="#1569C7",foreground="#FEFCFF").place(x=230 ,y=400,anchor="w" )
        

#        link4 = Label(F2, image=self.icon4, fg="blue",anchor="w",cursor="hand2")
#        link4.grid(row = 6,column=3) 
#        link4.bind("<Button-1>", lambda e: webbrowser.open_new("http://www.twitter.com"))



        logolbl=Label(F1, image=self.user_icon).place(x=80,y=200,anchor="w")
        lbl6 = Label(F1, text = "Email Id",fg="white",bg=bg_color, font= ("times new roman",20,"bold")).place(x=115,y=200,anchor="w")
        txtu = Entry(F1,bd=5,textvariable=self.email, relief = GROOVE,font=("",15)).place(x=250,y=200,anchor="w")
        

        logolbl2=Label(F1, image=self.pasw_icon).place(x=80,y=260,anchor="w")
        lbl7 = Label(F1, text = "Password",fg="white",bg=bg_color, font= ("times new roman",20,"bold")).place(x=115,y=260,anchor="w")
        txtp = Entry(F1,bd=5,textvariable=self.pasw, show="*",relief = GROOVE,font=("",15)).place(x=250,y=260,anchor="w")
        
        
        btn_login = Button(F1, text="Login",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="green",foreground="#FEFCFF",command=self.login).place(x=480,y=330,anchor="e")
        btn_login1 = Button(F1, text="Login as Admin",relief=GROOVE,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",command=self.login3).place(x=480,y=120,anchor="e")

        now = datetime.now()
        self.Time1=now.strftime('%H:%M:%S')
        self.date= now.strftime("%d-%b-%Y")


    def link1(self):
        webbrowser.open_new("http://www.google.com")
    
    def link2(self):
        webbrowser.open_new("https://www.instagram.com/?hl=en")
    
    def link3(self):
        webbrowser.open_new("http://www.facebook.com")

    def link4(self):
        webbrowser.open_new("http://www.twitter.com")
    


    def login(self):
        with open("Temp1.txt","w+") as file:
            file.write(self.email.get())
        if self.email.get()=="" or self.pasw.get()=="":
            messagebox.showerror("Error!","All field should be filled")
        if "@" not in self.email.get():
            messagebox.showwarning("Error","Email should have '@' Character")
        else:
            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            #self.c.execute("CREATE TABLE IF NOT EXISTS admin1(UID TEXT UNIQUE NOT NULL ,name TEXT NOT NULL, uname TEXT PRIMARY KEY UNIQUE NOT NULL, LoginT TIME NOT NULL, LoginDate DATE")
            #self.c.execute("SELECT admin.UID,admin.name,admin.uname, admin1.UID,admin1.name,admin1.uname, LoginT, LoginDate FROM admin INNER JOIN admin1 ON admin.UID=admin1.UID,admin.uname=admin1.uname,admin.name=admin1.name")
            self.find_user = ("SELECT * FROM Emp WHERE email = ?  AND pasw = ?")
            self.c.execute(str(self.find_user),(str(self.email.get()),str(self.pasw.get())))
            results = (self.c).fetchall()
            if results:
                for i in results:
             #       self.c.execut("UPDATE admin1 LoginT=?, LoginDate =?",(self.Time1,self.date))
             #       self.conn.commit()
             #       self.c.close()
             #       self.conn.close()
                    self.root.destroy()
                    import Home    
            else:
                messagebox.showerror("Error!","Username or Password may be wrong")
    
    def login2(self):
        self.root.destroy()
        import login
    
    def login3(self):
        self.root.destroy()
        import login
    
    def signup(self):
        self.root.destroy()
        import signup
                

    
    

            
#create Window    
root = Tk()
obj = win1(root)
root.mainloop()
