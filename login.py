from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from register import registerWindow
import tkinter
import mysql.connector
import os
from student import Student
from train import Train
from face_Recogniser import FaceRecogniser
from attendance import Attendance
from connector import *



class loginWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790")
        self.root.wm_iconbitmap(bitmap="face_attendance.ico")

        #background image
        bimg = Image.open("ImageFolder\login-bng.jpg")
        self.bngImg = ImageTk.PhotoImage(bimg)
        lbl_bng = Label(self.root, image=self.bngImg)
        lbl_bng.place(x=0, y=0,relwidth=1, relheight=1)

        frame=Frame(self.root,bg="#4E4F50")
        frame.place(x=470,y=100,width=340,height=450)

        #login icon
        img=Image.open("ImageFolder\login-icon.jpg")
        img=img.resize((100,100),Image.ANTIALIAS)
        self.imgPhoto = ImageTk.PhotoImage(img)
        img_label = Label(image=self.imgPhoto,bg="#4E4F50",borderwidth=0)
        img_label.place(x=586, y=105, width=100, height=100)

        #label for get started
        getStr=Label(frame,text="Get Started",font=("Rubik",20,"bold"),bg="#4E4F50",fg="black")
        getStr.place(x=90,y=100)

        #label  and entry for username
        self.userVar=StringVar()
        userNameLbl=Label(frame,text="Username",font=("Rubik",16,"bold"),bg="#4E4F50",fg="black")
        userNameLbl.place(x=50,y=150)

        userEntry=ttk.Entry(frame,textvariable=self.userVar,font=("Rubik",12,"bold"))
        userEntry.place(x=20,y=190,width=300,height=25)

        #label and entry for password
        self.passWVar=StringVar()
        passwordlbl = Label(frame,text="Password", font=("Rubik", 16, "bold"), bg="#4E4F50", fg="black")
        passwordlbl.place(x=50, y=230)

        passEntry = ttk.Entry(frame,textvariable=self.passWVar,show="*" ,font=("Rubik", 14, "bold"))
        passEntry.place(x=20, y=270, width=300, height=25)

        #username icon
        img1 = Image.open("ImageFolder\login-icon.jpg")
        img1 = img1.resize((30, 30), Image.ANTIALIAS)
        self.imgPhoto1 = ImageTk.PhotoImage(img1)
        img_label = Label(image=self.imgPhoto1, bg="#4E4F50", borderwidth=0)
        img_label.place(x=490, y=250, width=25, height=25)

        #password icon
        img2 = Image.open("ImageFolder\password1.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.imgPhoto2 = ImageTk.PhotoImage(img2)
        img2_label = Label(image=self.imgPhoto2, bg="#4E4F50", borderwidth=0)
        img2_label.place(x=490, y=335, width=25, height=25)

        #login button
        loginButton=Button(frame,command=self.login,text="Login",font=("Rubik", 16, "bold"),bd=4,relief=GROOVE,fg="white",bg="#112B3C",activeforeground="white",activebackground="#112B3C")
        loginButton.place(x=110,y=315,width=120,height=30)

        # for signup
        signUplabel = Label(frame, text="Don't have an account??", font=("Rubik", 12, "bold"), bg="#4E4F50", fg="black")
        signUplabel.place(x=20, y=360)
        signUpButton = Button(frame, text="Sign Up",command=self.reg, font=("Rubik", 14, "bold"),relief=GROOVE, fg="white", bg="#112B3C", activeforeground="white", activebackground="#112B3C")
        signUpButton.place(x=230, y=358, width=90,height=30)

        #for forgot password
        passButton = Button(frame, text="Forgot Password",command=self.forget_pwd, font=("Rubik", 12, "bold"),borderwidth=0, fg="black", bg="#4E4F50",activeforeground="black", activebackground="#4E4F50")
        passButton.place(x=20, y=395, width=140)

    def reg(self):
        self.newWindow = Toplevel(self.root)
        self.obj = registerWindow(self.newWindow)

    def login(self):
        if self.userVar.get()=="" or self.passWVar.get()=="":
            messagebox.showwarning("Warning","Both fields are required")

        else:
            conn = mysql.connector.connect(host=m, username=t, password=k, database="login")
            cur = conn.cursor()
            cur.execute("select * from reg where Email_ID=%s and PassWord=%s", (
                                                                                 self.userVar.get(),
                                                                                 self.passWVar.get()
                                                                       ))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                messagebox.showinfo("Success", "Welcome to Attendance Management System Using Facial Recognition ")
                self.newWindow = Toplevel(self.root)
                self.obj = FaceRecognition_Sysytem(self.newWindow)

            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.userVar.set("")
        self.passWVar.set("")

    def resetPassW(self):
        if self.SecQVar.get() == "Select":
            messagebox.showwarning("Warning", "Select the Security Question", parent=self.root2)
        elif (self.SecAVar.get() == ""):
            messagebox.showerror("Error", "Please Enter the Answer", parent=self.root2)
        elif (self.PassWVar.get() == ""):
            messagebox.showerror("Error", "Please Enter the New Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host=m, username=t, password=k, database="login")
            cur = conn.cursor()
            cur.execute(("select * from reg where Email_ID=%s and SecurityQ=%s and SecurityA=%s"),(
                                                                                      self.userVar.get(),
                                                                                      self.SecQVar.get(),
                                                                                      self.SecAVar.get()
                                                                                    ))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter the Correct Answer of security question", parent=self.root2)
            else:
                cur.execute(("update reg set PassWord=%s where Email_ID=%s"),(self.PassWVar.get(), self.userVar.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.root2.destroy()

    def forget_pwd(self):
        if self.userVar.get() == "":
            messagebox.showerror("Error", "Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(host=m, username=t, password=k, database="login")
            cur = conn.cursor()
            cur.execute(("select * from reg where Email_ID=%s"), (self.userVar.get(),))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Please Enter the Valid Email ID")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("500x500+400+100")
                self.root.iconbitmap("face_attendance.ico")
                label = Label(self.root2, text="Reset Password", font=("Rubik", 28, "bold"), fg="white",bg="black")
                label.place(x=0, y=0, relwidth=1)

                imge = Image.open(r"ImageFolder\forgot.jpg")
                imge = imge.resize((500, 450), Image.ANTIALIAS)
                self.imgPhoto = ImageTk.PhotoImage(imge)
                img_label = Label(self.root2, image=self.imgPhoto)
                img_label.place(x=0, y=50, width=500, height=450)

                frame = Frame(self.root2, bg="#525E75")
                frame.place(x=78, y=100, width=350, height=350)

                #label and combobox for security question
                self.SecQVar=StringVar()
                SecQ = Label(frame, text="Security Questions", font=("Rubik", 15, "bold"), bg="#525E75", fg="black")
                SecQ.place(x=20, y=30)

                SecQCombo = ttk.Combobox(frame, textvariable=self.SecQVar,font=("Rubik", 12, "bold"),state="readonly")
                SecQCombo["values"] = ("Select", "Your Favourite Book", "Your Favourite Author", "Your Favourite Food")
                SecQCombo.place(x=20, y=60, width=250)
                SecQCombo.current(0)

                # label and entry for security answer
                self.SecAVar=StringVar()
                SecA = Label(frame, text="Security Answer", font=("Rubik", 15, "bold"), bg="#525E75", fg="black")
                SecA.place(x=20, y=95)

                SecAEntry = ttk.Entry(frame,textvariable=self.SecAVar ,font=("Rubik", 11, "bold"))
                SecAEntry.place(x=20, y=125, width=250)

                #label and entry for password
                self.PassWVar=StringVar()
                PassW = Label(frame, text="Password", font=("Rubik", 15, "bold"), bg="#525E75", fg="black")
                PassW.place(x=20, y=160)

                PassWEntry = ttk.Entry(frame,textvariable=self.PassWVar,font=("Rubik", 11, "bold"))
                PassWEntry.place(x=20, y=190, width=250)

                #button for reset
                resetbtn = Button(frame, command=self.resetPassW, text="Reset Password",font=("Rubik", 18, "bold") ,bd=0, relief=GROOVE, fg="white", bg="red" ,activeforeground="white", activebackground="red")
                resetbtn.place(x=50, y=250, width=200, height=35)

class FaceRecognition_Sysytem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face_attendance.ico")

        label_title = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM USING FACE RECOGNITION",font=("Rubik", 21, "bold"), bg="#525252", fg="black")
        label_title.place(x=0, y=0, width=1300, height=70)

        #for background image
        imge1 = Image.open(r"ImageFolder\bng-img.jpg")
        imge1 = imge1.resize((1300, 580), Image.ANTIALIAS)
        self.imgPhoto1 = ImageTk.PhotoImage(imge1)
        bng_img= Label(self.root, image=self.imgPhoto1)
        bng_img.place(x=0, y=70, width=1300, height=580)

        def time():
            string=strftime("%H:%M:%S %p")
            label.config(text=string)
            label.after(1000,time)

        label=Label(label_title,font=("Rubik",18,"bold"),background="#525252",foreground="#293462")
        label.place(x=5,y=10,width=160,height=50)
        time()

        #for students management
        imge2 = Image.open(r"ImageFolder\students.jpg")
        imge2 = imge2.resize((250, 120), Image.ANTIALIAS)
        self.imgPhoto2 = ImageTk.PhotoImage(imge2)

        btn1=Button(bng_img,image=self.imgPhoto2,command=self.s_dt,cursor="hand2")
        btn1.place(x=140,y=120,width=250,height=120)

        btn1_1 = Button(bng_img, text="Student Details",command=self.s_dt, cursor="hand2",font=("Rubik",12,"bold"),bg="#73777B",fg="black")
        btn1_1.place(x=140, y=240, width=250, height=25)

        # for photos
        imge3 = Image.open(r"ImageFolder\photos.jpg")
        imge3 = imge3.resize((250, 120), Image.ANTIALIAS)
        self.imgPhoto3 = ImageTk.PhotoImage(imge3)

        btn2 = Button(bng_img, image=self.imgPhoto3, cursor="hand2", command=self.openImg, )
        btn2.place(x=490, y=120, width=250, height=120)

        btn2_1 = Button(bng_img, text="Photos", cursor="hand2", command=self.openImg, font=("Rubik", 12, "bold"), bg="#73777B", fg="black")
        btn2_1.place(x=490, y=240, width=250, height=25)

        # train the data
        imge4 = Image.open(r"ImageFolder\train-data.jpg")
        imge4 = imge4.resize((250, 120), Image.ANTIALIAS)
        self.imgPhoto4 = ImageTk.PhotoImage(imge4)

        btn3 = Button(bng_img, image=self.imgPhoto4, command=self.trainData, cursor="hand2")
        btn3.place(x=840, y=120, width=250, height=120)

        btn3_1 = Button(bng_img, text="Train Data", cursor="hand2", command=self.trainData, font=("Rubik", 12, "bold"),bg="#73777B", fg="black")
        btn3_1.place(x=840, y=240, width=250, height=25)

        #for face recognition
        imge5 = Image.open(r"ImageFolder\detector.jpg")
        imge5 = imge5.resize((250, 120), Image.ANTIALIAS)
        self.imgPhoto5 = ImageTk.PhotoImage(imge5)

        btn4 = Button(bng_img, image=self.imgPhoto5, cursor="hand2",command=self.facerec)
        btn4.place(x=140, y=350, width=250, height=120)

        btn4_1 = Button(bng_img, text="Face Recogniser", cursor="hand2",command=self.facerec, font=("Rubik", 12, "bold"), bg="#73777B",fg="black")
        btn4_1.place(x=140, y=470, width=250, height=25)

        #for attendance
        imge6 = Image.open(r"ImageFolder\Attendance.jpg")
        imge6 = imge6.resize((250, 120), Image.ANTIALIAS)
        self.imgPhoto6 = ImageTk.PhotoImage(imge6)

        btn5 = Button(bng_img, image=self.imgPhoto6, cursor="hand2",command=self.att)
        btn5.place(x=490, y=350, width=250, height=120)

        btn5_1 = Button(bng_img, text="Attendance", cursor="hand2", command=self.att,font=("Rubik", 12, "bold"), bg="#73777B",fg="black")
        btn5_1.place(x=490, y=470, width=250, height=25)

        #exit
        imge7 = Image.open(r"ImageFolder\exit.jpg")
        imge7 = imge7.resize((180, 120), Image.ANTIALIAS)
        self.imgPhoto7 = ImageTk.PhotoImage(imge7)

        btn6 = Button(bng_img, image=self.imgPhoto7, cursor="hand2",command=self.exit)
        btn6.place(x=840, y=350, width=250, height=120)

        btn6_1 = Button(bng_img, text="Exit", cursor="hand2",command=self.exit, font=("Rubik", 12, "bold"), bg="#73777B", fg="black")
        btn6_1.place(x=840, y=470, width=250, height=25)

    #for photos
    def openImg(self):
        os.startfile("mydata")

    #student details
    def s_dt(self):
        self.n_window=Toplevel(self.root)
        self.app=Student(self.n_window)

    #for training the data
    def trainData(self):
        self.n_window=Toplevel(self.root)
        self.app=Train(self.n_window)

    #for recognising the face
    def facerec(self):
        self.n_window=Toplevel(self.root)
        self.app=FaceRecogniser(self.n_window)

    #for attendance
    def att(self):
        self.n_window=Toplevel(self.root)
        self.app=Attendance(self.n_window)

    #for exit
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = loginWindow(root)
    root.mainloop()