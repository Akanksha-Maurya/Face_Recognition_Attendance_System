from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from connector import *

class registerWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790")
        self.root.iconbitmap("face_attendance.ico")

        self.fNameVar = StringVar()
        self.lNameVar = StringVar()
        self.EmailVar = StringVar()
        self.ContactVar = StringVar()
        self.PassWVar = StringVar()
        self.CPassWVar = StringVar()
        self.SecurityQVar = StringVar()
        self.SecurityAVar = StringVar()

        bimg = Image.open("ImageFolder/register.jpg")
        self.bngImg = ImageTk.PhotoImage(bimg)
        lbl_bng = Label(self.root, image=self.bngImg)
        lbl_bng.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root,bg="#73777B")
        frame.place(x=130,y=140,width=550,height=400)

        #label for creating a new account
        regLabel=Label(frame,text="Create a new account......",font=("Rubik",20,"bold"),bg="#73777B",fg="black")
        regLabel.place(x=20,y=20)

        #label and entry for first name
        fName=Label(frame,text="First Name",font=("Rubik",15,"bold"),bg="#73777B",fg="black")
        fName.place(x=30,y=70)

        fNameEntry=ttk.Entry(frame,textvariable=self.fNameVar,font=("Rubik",11,"bold"))
        fNameEntry.place(x=30,y=98,width=200)

        #label and entry for last name
        lName = Label(frame, text="Last Name", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        lName.place(x=300, y=70)

        lNameEntry = ttk.Entry(frame,textvariable=self.lNameVar, font=("Rubik", 11, "bold"))
        lNameEntry.place(x=300, y=98, width=200)

        #label and entry for email id
        Email= Label(frame, text="Email Id", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        Email.place(x=30, y=135)

        EmailEntry = ttk.Entry(frame,textvariable=self.EmailVar, font=("Rubik", 11, "bold"))
        EmailEntry.place(x=30, y=163, width=200)

        #label and entry for contact number
        Cont = Label(frame, text="Contact No", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        Cont.place(x=300, y=135)

        ContEntry = ttk.Entry(frame,textvariable=self.ContactVar, font=("Rubik", 11, "bold"))
        ContEntry.place(x=300, y=163, width=200)

        #label and entry for password
        PassW = Label(frame, text="Password", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        PassW.place(x=30, y=200)

        PassWEntry = ttk.Entry(frame,textvariable=self.PassWVar,show="*", font=("Rubik", 11, "bold"))
        PassWEntry.place(x=30, y=228, width=200)

        #label and entry for confirm password
        CPassW = Label(frame, text="Confirm Password", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        CPassW.place(x=300, y=200)

        CPassWEntry = ttk.Entry(frame,textvariable=self.CPassWVar,show="*",font=("Rubik", 11, "bold"))
        CPassWEntry.place(x=300, y=228, width=200)

        #label and combobox for security question
        SecQ = Label(frame, text="Security Questions", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        SecQ.place(x=30, y=265)

        SecQCombo = ttk.Combobox(frame,textvariable=self.SecurityQVar, font=("Rubik", 11, "bold"),state="readonly")
        SecQCombo["values"] = ("Select","Your Favourite Book","Your Favourite Author","Your Favourite Food")
        SecQCombo.place(x=30,y=293,width=200)
        SecQCombo.current(0)

        #label and entry for security answer
        SecA= Label(frame, text="Security Answer", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        SecA.place(x=300, y=265)

        SecAEntry = ttk.Entry(frame, textvariable=self.SecurityAVar,font=("Rubik", 11, "bold"))
        SecAEntry.place(x=300, y=293, width=200)

        #button for register
        btnR = Button(frame, text="CREATE ACCOUNT", cursor="hand2", command=self.regData,font=("Rubik", 10, "bold"), bg="#112B3C", fg="white",activebackground="#112B3C", activeforeground="white")
        btnR.place(x=200, y=330, width=150, height=24)

        #label for already have an account
        Alaccount = Label(frame, text="Already have an account??", font=("Rubik", 15, "bold"), bg="#73777B", fg="black")
        Alaccount.place(x=50, y=360)

        #button for login
        btnR = Button(frame, text="LOGIN", cursor="hand2",command=self.login_reg, font=("Rubik", 10, "bold"), bg="#112B3C", fg="white",activebackground="#112B3C", activeforeground="white")
        btnR.place(x=360, y=360, width=130, height=26)

        #for background image
        bimg = Image.open("ImageFolder/register-bng.jpg")
        self.bngImg1 = ImageTk.PhotoImage(bimg)
        lbl_bng1 = Label(self.root, image=self.bngImg1)
        lbl_bng1.place(x=680, y=140,width=400,height=400 )

        #function for registering the data
    def regData(self):
        if self.fNameVar.get()=="" or self.ContactVar.get()=="" or self.EmailVar.get()=="" or self.PassWVar.get()=="" or self.CPassWVar.get()=="" or self.SecurityQVar.get()=="Select" or self.SecurityAVar.get()=="":
            messagebox.showwarning("Warning","All fields are required",parent=self.root)
        elif self.PassWVar.get()!=self.CPassWVar.get():
            messagebox.showerror("Error","Password and confirm password must be same",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host=m, username=t, password=k, database="login")
                cur = conn.cursor()
                cur.execute(("select * from reg where Email_ID=%s"), (self.EmailVar.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showwarning("Warning", "This Email is already registered")
                else:
                    cur.execute("insert into reg values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                               self.fNameVar.get(),
                                                                                               self.lNameVar.get(),
                                                                                               self.EmailVar.get(),
                                                                                               self.ContactVar.get(),
                                                                                               self.PassWVar.get(),
                                                                                               self.SecurityQVar.get(),
                                                                                               self.SecurityAVar.get()
                                                                                         ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "You have registered successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def login_reg(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=registerWindow(root)
    root.mainloop()
