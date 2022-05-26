import tkinter.messagebox
from tkinter import*
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from train import Train
from face_Recogniser import FaceRecogniser
from attendance import Attendance

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
        imge1 = imge1.resize((1300, 610), Image.ANTIALIAS)
        self.imgPhoto1 = ImageTk.PhotoImage(imge1)
        bng_img= Label(self.root, image=self.imgPhoto1)
        bng_img.place(x=0, y=70, width=1300, height=610)

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
    root=Tk()
    obj=FaceRecognition_Sysytem(root)
    root.mainloop()
