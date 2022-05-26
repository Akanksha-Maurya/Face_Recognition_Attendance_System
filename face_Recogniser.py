from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np


class FaceRecogniser:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face_attendance.ico")

        titleLabel = Label(self.root, text="FACE RECOGNISER", font=("Rubik", 30, "bold"), bg="#525252", fg="black")
        titleLabel.place(x=0, y=0, width=1300, height=55)

        Back_Button = Button(titleLabel, text="Back", command=self.root.destroy, font=("Rubik", 13, "bold"), width=14,bg="black", fg="white")
        Back_Button.pack(side=RIGHT)

        def time():
            string = strftime("%H:%M:%S %p")
            label.config(text=string)
            label.after(1000, time)

        label = Label(titleLabel, font=("Rubik", 18, "bold"), background="#525252", foreground="#293462")
        label.place(x=5, y=5, width=140, height=40)
        time()

        #background image
        BngImg = Image.open(r"ImageFolder\faceRecognition2.jpg")
        BngImg = BngImg.resize((1300, 670), Image.ANTIALIAS)
        self.BngImgPhoto = ImageTk.PhotoImage(BngImg)
        first_label = Label(self.root, image=self.BngImgPhoto)
        first_label.place(x=0, y=55, width=1300, height=670)

        #face recogniser button
        btn = Button(first_label, text="Face Recognition", cursor="hand2",command=self.faceRec,font=("Rubik", 20, "bold"), bg="#112B3C", fg="white")
        btn.place(x=480, y=460, width=300, height=50)

    #for marking attendance
    def markAttendance(self,dep,i,em,name):
        with open("attendance_Report/attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split((","))
                nameList.append(entry[0])

            if((dep not in nameList) and (i not in nameList) and (em not in nameList) and (name not in nameList)):
                now=datetime.now()
                date=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{dep},{name},{em},{date},{dtString},Present")

   # for face recognition
    def faceRec(self):
          def drawBoundary(img,classifier,scaleFactor,minNeighbors,color,text,clsf):
                grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(grayImage,scaleFactor,minNeighbors)

                coordinates=[]

                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
                    id,predict=clsf.predict(grayImage[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    connection = mysql.connector.connect(host="localhost", username="root", password="ak201020",database="myproject")
                    cur = connection.cursor()

                    cur.execute("select Department from student where Student_Id="+str(id))
                    dep = cur.fetchone()
                    dep = "+".join(dep)

                    cur.execute("select Email_Id from student where Student_Id="+str(id))
                    em = cur.fetchone()
                    em = "+".join(em)

                    cur.execute("select Name from student where Student_Id=" + str(id))
                    name = cur.fetchone()
                    name = "+".join(name)

                    cur.execute("select Student_Id from student where Student_Id=" + str(id))
                    i = cur.fetchone()
                    i = "+".join(i)

                    if confidence>77:
                        cv2.putText(img,f"Department:{dep}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                        cv2.putText(img, f"Id:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255, 255, 255),4)
                        cv2.putText(img, f"Email:{em}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),4)
                        cv2.putText(img, f"Name:{name}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),4)
                        self.markAttendance(dep,i,em,name)


                    else:
                        cv2.rectangle(img,(x, y),(x+w, y+h), (0, 0, 255), 4)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)

                    coordinates=[x,y,w,h]

                return coordinates

          def recognize(img,clsf,faceCas):
                coordinates=drawBoundary(img,faceCas,1.1,10,(255,255,255),"Face",clsf)
                return img

          faceCas=cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
          clsf = cv2.face.LBPHFaceRecognizer_create()
          clsf.read("classifier.xml")

          cap=cv2.VideoCapture(0)

          while True:
                ret,img=cap.read()
                img=recognize(img,clsf,faceCas)
                cv2.imshow("Welcome",img)

                if cv2.waitKey(1)==13 :
                    break
          cap.release()
          cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=FaceRecogniser(root)
    root.mainloop()
