from tkinter import *
from tkinter import ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x600+600+20")
        self.root.title("Email")
        self.root.iconbitmap("face_attendance.ico")

        self.Rmail = StringVar()
        self.Rpswrd = StringVar()
        self.Rsender = StringVar()
        self.Rsubject = StringVar()


        Label_0 = Label(self.root, text="SEND MAIL", width=18, bg="black", fg="white", font=("Rubik", 28, "bold"))
        Label_0.place(x=0, y=0, relwidth=1)

        mainFrame = Frame(self.root, bd=3, bg="#395B64")
        mainFrame.place(x=0, y=50, width=500, height=550)

        #label and entry for your email account
        Label_1 = Label(mainFrame, text="Your Email Account:",font=("Rubik", 13, "bold"),bg="#395B64", fg="black")
        Label_1.place(x=30, y=10)

        emailE = ttk.Entry(mainFrame, textvariable=self.Rmail,font=("Rubik", 10, "bold"))
        emailE.place(x=30, y=40,width=280)

        #label and entry for your password
        Label_2 = Label(mainFrame, text="Your Password:", font=("Rubik", 13, "bold"),bg="#395B64", fg="black")
        Label_2.place(x=30, y=80)

        passwordE = ttk.Entry(mainFrame, show="*", textvariable=self.Rpswrd,font=("Rubik", 10, "bold"))
        passwordE.place(x=30, y=110,width=280)

        compose = Label(mainFrame, text="COMPOSE",font=("Rubik", 18, "bold"),bg="#395B64", fg="black")
        compose.place(x=170, y=150)

        #label and entry for email id to which you have to send the mail
        Label_3 = Label(mainFrame, text="Send to Email:", font=("Rubik", 13, "bold"), bg="#395B64", fg="black")
        Label_3.place(x=30, y=190)

        senderE = ttk.Entry(mainFrame,textvariable=self.Rsender,font=("Rubik", 10, "bold"))
        senderE.place(x=30, y=220,width=280)

        #label and entry for subject
        Label_4 = Label(mainFrame, text="Subject:", font=("Rubik", 13, "bold"), bg="#395B64", fg="black")
        Label_4.place(x=30, y=260)

        subjectE = ttk.Entry(mainFrame,textvariable=self.Rsubject,font=("Rubik", 10, "bold"))
        subjectE.place(x=30, y=290,width=280)

        Label_5 = Label(mainFrame, text="Message:", font=("Rubik", 13, "bold"), bg="#395B64", fg="black")
        Label_5.place(x=30, y=330)

        self.msgbodyE = Text(self.root, width=50, height=10)
        self.msgbodyE.place(x=30, y=415)

       #button for sending the mail
        btn=Button(self.root, text="Send", command=self.sendemail,font=("Rubik", 12, "bold"),bd=4,relief=GROOVE,fg="white",bg="red",activeforeground="white",activebackground="red")
        btn.place(x=390, y=10,width=100)

    def sendemail(self):
        try:
            mymsg = MIMEMultipart()
            mymsg['From'] = str(self.Rmail.get())
            mymsg['To'] = str(self.Rsender.get())
            mymsg['Subject'] = str(self.Rsubject.get())

            mymsg.attach(MIMEText(self.msgbodyE.get(1.0, 'end'), 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(str(self.Rmail.get()), str(self.Rpswrd.get()))
            text = mymsg.as_string()
            server.sendmail(str(self.Rmail.get()), str(self.Rsender.get()), text)

            Label_6 = Label(self.root, text="Done!", width=20, fg='green', font=("bold", 15))
            Label_6.place(x=140, y=550)

            server.quit()
        except:
            Label_6 = Label(self.root, text="something went wrong!", width=20, fg='red', font=("bold", 15))
            Label_6.place(x=140, y=550)

if __name__ == "__main__":
    root=Tk()
    obj=Email(root)
    root.mainloop()
